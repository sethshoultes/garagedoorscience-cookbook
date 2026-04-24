# Claude Desktop MCP connector

Connect Claude Desktop to the garagedoorscience.com MCP endpoint so Claude can diagnose garage-door problems, route to local pros, and pull reference photos inside your regular Claude conversations.

## Two ways to connect

### Option 1 — Custom Connectors (recommended, no terminal)

1. Open Claude Desktop
2. Settings → Connectors → **Add Custom Connector**
3. URL: `https://garagedoorscience.com/mcp`
4. Auth: **None** (public tier) — or paste a `gds_live_` bearer token for the pro tier
5. Enable the connector in your chats

The connector appears in Claude's tool picker as "Garage Door Science."

### Option 2 — Config file (for older Claude Desktop or scripted setups)

Merge the contents of [`claude_desktop_config.json`](./claude_desktop_config.json) into your existing config:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Then restart Claude Desktop.

**Public tier** — no auth, 60/min, 2000/day: `mcpServers.garagedoorscience`
**Pro tier** — with `gds_live_` bearer: `mcpServers.garagedoorscience-pro`

## Sample prompts once connected

- *"Why is my garage door making a grinding noise?"* → calls `diagnose`
- *"Find a garage door pro near 84770."* → calls `routeByZip`
- *"What does a broken torsion spring look like?"* → calls `getInspectionReferencePhotos`
- *"How do garage door springs work?"* → calls `retrieveLabContext` for a grounded answer with source citations

## Troubleshooting

**`ReferenceError: ReadableStream is not defined`** — Node version issue. `mcp-remote` needs Node 18+. If you have multiple Node versions via nvm or Homebrew, point `command` at an absolute path to a recent Node binary.

**401 invalid token** — the bearer in your config has a trailing newline or extra whitespace. Regenerate the key at [/developers](https://garagedoorscience.com/developers) and paste carefully.

**Tools don't appear** — restart Claude Desktop fully (quit, reopen). Check `~/Library/Logs/Claude/mcp-server-garagedoorscience.log` for errors.

## Rate limits

- Public tier: 60 requests/min, 2,000/day per IP
- Pro tier: 240/min, 10,000/day + top-10 retrieval (vs top-3 on public)

Get a pro key free at [/developers](https://garagedoorscience.com/developers).
