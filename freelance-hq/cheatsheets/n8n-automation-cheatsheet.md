# n8n / automation cheat sheet

## Core concepts
- **Workflow**: a chain of nodes. **Trigger**: starts it (webhook, schedule, new email, form). **Node**: one step (Google Sheets, HTTP Request, Gmail, Code). **Execution**: one run.
- **Credentials**: saved logins for apps. Use the client's own account with least permissions. Never paste secrets into notes or share exports with credentials.
- **Expressions**: `{{ $json.email }}` reads data from the previous node.

## Common patterns (sellable)
1. Form -> Sheet row -> email confirmation -> reminder in 2 days.
2. New lead -> enrich -> CRM -> Slack/Telegram alert.
3. Invoice due -> polite reminder -> escalate after 7 days.
4. Positive review -> ask to post publicly; negative -> alert owner.
5. Weekly report: pull metrics -> summarize with AI -> email.
6. Support email -> classify -> draft reply for human approval.

## Good practice
Name nodes clearly; add notes; use error workflows and alerts; keep a test mode with sample data; limit retries; log runs; add a manual approval step before any customer-facing AI send.

## AI node tips
Provide a short system prompt, structured output (JSON), temperature low for consistent results, and a fallback if the AI fails. Keep prompts versioned in the workflow notes.

## Self-hosting on 8 GB RAM
Run only n8n + a lightweight database; use SQLite for testing; avoid running other heavy services at the same time. Back up the `.n8n` volume. Pin versions.

## Licence note
n8n uses a fair-code licence: build automations for yourself and clients; do not resell n8n itself as a hosted service. See `../bah-digital/docs/LICENSING.md`.

## Alternatives
Activepieces (open source), Make and Zapier (hosted free tiers), Huginn, Node-RED. Choose what the client can maintain.

## Deliverable checklist
Exported JSON (sanitized) | screenshots | credential list (what access is needed) | setup steps | test results | support terms.
