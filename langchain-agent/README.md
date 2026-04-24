# LangChain agent — garage door diagnostics

Python LangChain agent that calls three garagedoorscience.com tools (`diagnose`, `routeByZip`, `retrieveLabContext`) through the REST API. About 80 lines of code, no garage-door-specific logic.

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
# Optional — only needed for pro-tier rate limits + top-10 retrieval
export GDS_BEARER=gds_live_...
```

## Run

```bash
python agent.py "My garage door won't close and the light is blinking."
```

Expected: the agent calls `diagnose`, returns likely causes (safety sensor obstruction, limit switch misalignment, worn rollers), and offers to find a local pro if you share a ZIP.

## How it works

`agent.py` defines three `StructuredTool`s — one per API endpoint — with Pydantic input schemas matching the OpenAPI spec. An OpenAI tools-agent decides which tool to call based on the user's question.

The tools call `POST /api/v1/<op>` on `https://garagedoorscience.com`. No auth for public tier; pass `Authorization: Bearer <key>` for pro tier.

## Extend it

To add the other five tools (`getDoorStyles`, `getActivePromotions`, `getInspectionReferencePhotos`, `costEstimate`, `submitInspection`):

1. Add a Pydantic `BaseModel` with the fields from [/openapi.json](https://garagedoorscience.com/openapi.json)
2. Add a function that calls `_call("/<op>", payload)`
3. Wrap both in a `StructuredTool.from_function(...)` and append to `TOOLS`

Or import the full OpenAPI spec and generate tools dynamically — works too, though it takes slightly more boilerplate.

## Swap the LLM

The agent uses `ChatOpenAI(model="gpt-4o")` by default. LangChain supports Anthropic, Google, Ollama, and others — swap the `llm = ...` line.

## License

MIT.
