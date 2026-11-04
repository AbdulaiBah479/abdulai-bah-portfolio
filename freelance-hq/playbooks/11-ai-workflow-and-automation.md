# 11. AI workflow and automation: how Claude runs the business

Goal: Claude drafts and prepares; **you** decide, approve, publish and talk to humans.

## Autonomy levels
| Level | What Claude does | Examples |
|---|---|---|
| L0 Advise | Explains, plans | Strategy, pricing |
| L1 Draft | Produces text/files | Proposals, gigs, chapters |
| L2 Prepare | Builds assets & trackers | Product files, EPUB, reports |
| L3 Act with approval | Runs tools after you approve | Send emails, publish via API |
| L4 Autonomous | Not recommended for customer-facing or money actions | none |

Keep customer-facing and money actions at L1-L3.

## Daily loop (45-90 min of your time)
1. `/weekly-review` on Mondays; daily: open `tracker/leads.csv`.
2. Paste 5-10 fresh job posts -> `/proposal` -> approve and send.
3. Reply to messages with `client-success-manager` drafts.
4. Build one block: chapter, product component, gig asset, or content piece.
5. Log actions in trackers.

## Automation stack (all free/open-source options)
- **n8n** (self-host) or **Activepieces**: workflows (new lead -> CRM row -> Slack/email alert; new sale -> thank-you email; weekly metrics email). Mind licences: n8n's licence restricts offering it as a hosted service; use it for your own business or client-installed automations (see `../bah-digital/docs/LICENSING.md`).
- **Postiz**: schedule social posts across platforms.
- **listmonk**: self-hosted newsletters.
- **Twenty CRM** or a spreadsheet: leads pipeline.
- **Firecrawl / Crawl4AI / Browser Use**: web research and structured data collection (respect robots.txt, site TOS and law).
- **Whisper**: transcribe calls and videos for case studies and subtitles.
- **Ollama**: run local models for private drafts when client data is sensitive and hardware allows (8 GB RAM = small models only).
- **Stirling-PDF, OCRmyPDF, Gotenberg**: PDF toolkit for ebooks, invoices and deliverables.
- **Pandoc, Typst, Calibre, Sigil**: ebook building.
- **Rembg, Upscayl, FFmpeg**: image/video processing for product previews and creative gigs.

## MCP and connectors worth enabling when you need them
Google Drive/Docs (documents), Gmail (draft replies), Notion/Airtable (CRM and calendars), Canva (graphics/pitch decks), Figma (UI mockups), Zapier/Make (cross-app triggers), GitHub (repo hosting). Review each connector's permissions; start read-only; keep write actions approval-gated. See `.mcp.example.json`.

## Prompt hygiene
Give Claude: goal, audience, constraints, source material, format, examples, and a "done" definition. Ask for options plus a recommendation. Ask it to flag assumptions and `TODO(owner)` items. Prompt library: `cheatsheets/prompts-library.md`.

## Quality control
Every client deliverable gets a human review pass and a checklist (accuracy, requirements met, formatting, licences, no private data, file tested). For ebooks: fact-check every claim. For code: run it, test it, document it.

## Privacy rule
Don't paste confidential client material into any tool unless your agreement or the client allows it. Use local models or redaction for sensitive data.

## Build assets that compound
Every project leaves behind: a reusable template, an SOP, a prompt, a case study, a testimonial. Store them in `products/` and `templates/`.
