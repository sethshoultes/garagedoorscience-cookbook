"""LangChain agent that calls garagedoorscience.com's REST API.

Defines three tools with Pydantic schemas: diagnose, routeByZip,
retrieveLabContext. Uses an OpenAI tools agent to decide which to
call based on the user's question.

Usage:
    python agent.py "My garage door won't close."
"""

import json
import os
import sys
from typing import Optional

import requests
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import StructuredTool
from langchain_core.prompts import ChatPromptTemplate


API_BASE = "https://garagedoorscience.com/api/v1"
BEARER = os.environ.get("GDS_BEARER")  # optional pro-tier key


def _call(path: str, payload: dict) -> str:
    headers = {"Content-Type": "application/json"}
    if BEARER:
        headers["Authorization"] = f"Bearer {BEARER}"
    res = requests.post(f"{API_BASE}{path}", json=payload, headers=headers, timeout=15)
    res.raise_for_status()
    return json.dumps(res.json(), indent=2)


# --- diagnose ---
class DiagnoseArgs(BaseModel):
    description: str = Field(description="The homeowner's symptom description in their own words.")


def diagnose(description: str) -> str:
    return _call("/diagnose", {"description": description})


# --- routeByZip ---
class RouteByZipArgs(BaseModel):
    zipOrLocation: str = Field(description="A 5-digit ZIP or a city name, e.g. '84770' or 'St. George'.")
    issue: Optional[str] = Field(default=None, description="Optional issue key from diagnose, e.g. 'broken_spring'.")
    leadHeat: Optional[str] = Field(default="warm", description="'hot' emergency / 'warm' replacement / 'cold' research.")


def route_by_zip(zipOrLocation: str, issue: Optional[str] = None, leadHeat: Optional[str] = "warm") -> str:
    payload: dict = {"zipOrLocation": zipOrLocation, "leadHeat": leadHeat}
    if issue:
        payload["issue"] = issue
    return _call("/routeByZip", payload)


# --- retrieveLabContext ---
class RetrieveArgs(BaseModel):
    query: str = Field(description="The question or rephrased query for retrieval.")
    topK: Optional[int] = Field(default=5, description="Number of results to return (1-10).")


def retrieve_lab_context(query: str, topK: int = 5) -> str:
    return _call("/retrieveLabContext", {"query": query, "topK": topK})


TOOLS = [
    StructuredTool.from_function(
        func=diagnose,
        name="diagnose",
        description="Diagnose a garage-door symptom. Returns likely issues, urgency, cost ranges, and DIY-safety flags.",
        args_schema=DiagnoseArgs,
    ),
    StructuredTool.from_function(
        func=route_by_zip,
        name="routeByZip",
        description="Find the local garage-door partner for a homeowner's ZIP or city. Returns partner name, phone, booking URL.",
        args_schema=RouteByZipArgs,
    ),
    StructuredTool.from_function(
        func=retrieve_lab_context,
        name="retrieveLabContext",
        description="Search the garage-door science labs for grounded educational content with source citations.",
        args_schema=RetrieveArgs,
    ),
]


def main() -> None:
    query = " ".join(sys.argv[1:]) or "My garage door won't close and the light is blinking."

    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a garage-door diagnostic agent. Use the provided tools to answer accurately. "
            "When a user describes a symptom, call `diagnose` first. "
            "When given a ZIP or city, call `routeByZip`. "
            "Ground educational answers with `retrieveLabContext`. "
            "Never advise someone to work on torsion springs or cables themselves — always route to a pro.",
        ),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    agent = create_openai_tools_agent(llm, TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=TOOLS, verbose=True)
    result = executor.invoke({"input": query})

    print("\n=== Final answer ===")
    print(result["output"])


if __name__ == "__main__":
    main()
