# ChatGPT Custom GPT — Garage Door Doctor

Publish a Custom GPT that calls the garagedoorscience.com API to diagnose garage-door problems and route homeowners to local pros. Costs nothing to run — uses the public tier.

## Quick start

1. Open ChatGPT (Plus/Team/Enterprise) → Explore GPTs → **Create a GPT**
2. Click **Configure** (skip the conversational builder for precision)
3. Fill out:
   - **Name:** Garage Door Doctor (or your variant)
   - **Description:** *Diagnose garage-door problems and connect to a trusted local pro. Powered by garagedoorscience.com.*
   - **Instructions:** paste from [`instructions.md`](./instructions.md)
   - **Conversation starters:** listed at the bottom of [`instructions.md`](./instructions.md)
4. **Capabilities:** disable web browsing, DALL-E, and Code Interpreter. This GPT uses live tools, not general generation.
5. **Actions:**
   - **Schema → Import from URL:** `https://garagedoorscience.com/openapi.json`
   - **Authentication:** None (public tier — 60/min, 2000/day per IP)
   - **Privacy policy:** `https://garagedoorscience.com/privacy`
6. **Test** these prompts in the preview pane before publishing:
   - *"My door won't close"* — expect `diagnose`
   - *"ZIP 84770"* — expect `routeByZip`
   - *"What does a broken spring look like?"* — expect `getInspectionReferencePhotos`
   - *"Can I replace the spring myself?"* — expect refusal + route to a pro
7. **Publish** — share via link, or submit to the GPT Store (domain verification via DNS TXT required for Store).

## What it does

| Prompt pattern | Tool called | Response |
|---|---|---|
| Symptom description | `diagnose` | Likely causes + cost range + safety flags |
| ZIP code or city | `routeByZip` | Partner name + phone + booking URL |
| "What does X look like?" | `getInspectionReferencePhotos` | Severity-tagged reference images inline |
| "How does X work?" | `retrieveLabContext` | Grounded answer with citations |
| "How much does X cost?" | `getDoorStyles` or `costEstimate` | Pricing from structured data |
| Unsafe DIY request (springs, cables) | Refuses + calls `routeByZip` | Routes to a pro |

## Cost to run

**Free.** Calls the public tier. No user tokens. No rate-limit engineering.

If the GPT takes off and you hit rate limits, upgrade the Actions auth from "None" to an API Key with your `gds_live_` bearer — moves you to the pro tier (240/min, 10,000/day, top-10 retrieval) in 30 seconds.

## Domain verification (for Store publish)

Required only if you want the GPT listed on the public GPT Store. The builder gives you a TXT record value; you add it to DNS for `garagedoorscience.com`, click Verify. Propagates in 5-60 minutes.

## License

MIT.

## Related

- Full config pack with test-prompt checklist in the main repo: [`docs/custom-gpt/garage-door-doctor.md`](https://github.com/sethshoultes/garagedoorscience/blob/main/docs/custom-gpt/garage-door-doctor.md)
- The essay this recipe comes from: [The Pattern Held](https://sethshoultes.com/blog/pattern-held.html)
