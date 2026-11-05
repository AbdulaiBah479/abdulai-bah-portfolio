---
name: n8n-workflow-productizer
description: Turn a working client or personal automation (n8n, Make, Activepieces) into a sanitized, documented, sellable workflow pack. Use when productizing automations or building workflow templates for sale.
---

# n8n workflow productizer

## Steps
1. **Pick** an automation that solved a repeated problem for 2+ clients or is a clear universal need (lead follow-up, invoice reminders, review requests, weekly report).
2. **Sanitize:** export JSON; remove credentials, IDs, emails, URLs, names; replace with placeholders (`YOUR_SHEET_ID`); search the JSON for secrets (`apikey`, `token`, `Bearer`, emails). Check no client logic is exposed.
3. **Generalize:** make fields configurable (Set node with variables at the top), add notes on nodes, error handling and a test mode.
4. **Document:** README (what it does, requirements, setup in 10 steps, screenshots), credentials guide (least-privilege scopes), troubleshooting, FAQ, changelog, version and tested n8n version.
5. **Test** on a clean n8n instance with sample data; record a 2-minute walkthrough.
6. **Licence:** check n8n's licence and node/API terms; your pack is a template for users running their own n8n; do not resell hosted n8n. Choose a clear licence (personal/commercial).
7. **Package & price:** single workflow $9-29; niche pack (5-10 workflows) $29-99; setup service upsell (test these ranges). Create the listing with `digital-product-launch`.
8. **Marketing:** a free sample workflow on GitHub + a demo video drives traffic to the paid pack.

## Security note
Treat any exported workflow as a secret until sanitized. Scan with a regex pass, and have the owner confirm before publishing.
