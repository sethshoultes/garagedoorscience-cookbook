# Garage Door Science Cookbook

Runnable recipes for integrating with [garagedoorscience.com](https://garagedoorscience.com) — an AI-first diagnostic and lead-routing platform for residential garage doors.

Each recipe shows one way to call the platform's eight tools (`diagnose`, `routeByZip`, `getDoorStyles`, `getActivePromotions`, `getInspectionReferencePhotos`, `retrieveLabContext`, `costEstimate`, `submitInspection`) from a different AI-consumer context.

## Recipes

| Recipe | What it does | Best for |
|---|---|---|
| [`claude-desktop-mcp/`](./claude-desktop-mcp) | Connect Claude Desktop to the live MCP endpoint | Anyone using Claude — get live garage-door tools inside your existing chats |
| [`chatgpt-custom-gpt/`](./chatgpt-custom-gpt) | Publish a ChatGPT Custom GPT powered by our OpenAPI spec | Reach homeowners already in ChatGPT; no infrastructure |
| [`langchain-agent/`](./langchain-agent) | Python LangChain agent calling the REST API | Agent frameworks that import OpenAPI (LangChain, LlamaIndex) |
| [`contractor-embed/`](./contractor-embed) | Minimal HTML/JS widget embeddable on a contractor's site | Garage-door companies wanting AI diagnostics on their own website |

## Official packages (separate repos)

Beyond the copy-paste cookbook, two installable packages ship the most common integrations as ready-to-use plugins:

| Package | What it does | Install |
|---|---|---|
| [**wp-garagedoorscience**](https://github.com/sethshoultes/wp-garagedoorscience) | WordPress plugin — adds a `[gds-diagnose]` shortcode for any page | WP admin upload, or clone + zip |
| [**garagedoorscience-claude-plugin**](https://github.com/sethshoultes/garagedoorscience-claude-plugin) | Claude Code plugin — `diagnose-garage-door` skill + MCP connector | `git clone` into `~/.claude/plugins/` |

## What the platform exposes

- **MCP endpoint** (no auth, 60/min, 2000/day): `https://garagedoorscience.com/mcp`
- **MCP Pro** (bearer auth, 4× rate limit, top-10 retrieval): `https://garagedoorscience.com/mcp-pro`
- **REST API** (same tools at `/api/v1/<tool>`): [`/api/v1/diagnose`](https://garagedoorscience.com/api/v1/diagnose), etc.
- **OpenAPI 3.1 spec**: [`/openapi.json`](https://garagedoorscience.com/openapi.json)
- **Interactive docs**: [`/developers/api`](https://garagedoorscience.com/developers/api) (Scalar)
- **Agent guide**: [`/brain`](https://garagedoorscience.com/brain)

## Get an API key (for pro tier)

Sign up at [`/developers`](https://garagedoorscience.com/developers) with email magic-link. Paid plans coming — keys auto-upgrade when they land.

## License

MIT — copy anything you need.

## Related reading

- [Building in the Age of AI](https://sethshoultes.com/blog/building-in-the-age-of-ai.html) — the four-day build this platform came from
- [One Registry, Seven Surfaces](https://sethshoultes.com/blog/one-registry-seven-surfaces.html) — the pattern these recipes follow
- [The Pattern Held](https://sethshoultes.com/blog/pattern-held.html) — ChatGPT's Custom GPT Actions as the eighth surface, with zero new code
