# Contractor embed — minimal diagnostic widget

A zero-dependency HTML/JS snippet that garage-door contractors can paste into their own website to offer diagnostic Q&A powered by garagedoorscience.com's REST API.

## How it works

Homeowner types a symptom → widget calls `POST /api/v1/diagnose` → renders likely issues with cost ranges and safety flags.

## Demo

Open [`embed.html`](./embed.html) in a browser. Type *"My door won't close"* into the textarea and click Diagnose.

## Paste it on your site

Copy the contents of [`embed.html`](./embed.html) into any HTML page or CMS block. It's self-contained — no build step, no external dependencies, no framework. Works inside WordPress (Custom HTML block), Webflow (embed), plain static sites, anything.

Customize the top-of-file CSS variables to match your brand:

```css
:root {
  --accent: #d4541a;     /* your brand primary */
  --text: #1a1a18;
  --muted: #6b7280;
  --border: #e5e7eb;
  --surface: #fff;
}
```

## What this widget does not do (yet)

- Chat-style back-and-forth (this is single-shot diagnosis; no session)
- Reference photos (~10 lines to add a call to `getInspectionReferencePhotos`)
- Partner routing (add a ZIP field + call `/api/v1/routeByZip`)
- Cost estimation (add `/api/v1/costEstimate` with door size + zip)

Each is a small extension. Fork and add.

## Rate limits

The widget calls the public tier (no auth) — 60 requests/min, 2,000/day per IP (the visitor's IP, not yours). Plenty for a contractor site with modest traffic.

For higher volume, grab a free `gds_live_` key at [/developers](https://garagedoorscience.com/developers) and add to the fetch call:

```js
headers: {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer gds_live_YOUR_KEY',
},
```

But note: if you put the bearer in client-side JavaScript, anyone can steal it by viewing source. For pro-tier production use, proxy the call through your own backend.

## License

MIT. Paste it, rebrand it, ship it.

## Related

- The source tools this uses: [/openapi.json](https://garagedoorscience.com/openapi.json)
- Interactive docs: [/developers/api](https://garagedoorscience.com/developers/api)
