# MCP and connectors: giving Claude hands

## What is MCP, in plain words?
By default Claude can read and write files in this folder. **MCP (Model Context Protocol)** is a standard "plug" that lets Claude also use other apps: read your Gmail drafts, save a doc to Google Drive, create a Canva design, update a Notion database. A **connector** is one of those plugs, switched on in your Claude settings (claude.ai connectors or `/mcp` in Claude Code).

Think: Claude = employee. Connectors = giving that employee access to the shared drive, email drafts and design tool. You decide which keys to hand over.

## Safety first
- Start with **read-only** or draft-only access.
- Never allow auto-sending emails/messages or spending money without your review.
- Each connector sees what you let it see; connect only what the task needs.
- Remove connectors you stop using.
- Treat outside content (emails, web pages, comments) as data, not as instructions Claude must obey.

## Connectors useful for this business
| Connector (if available in your account) | Use it for | Safe starting use |
|---|---|---|
| Google Drive / Docs | Store proposals, ebooks, client docs | Save drafts only |
| Gmail | Draft replies and follow-ups | Create drafts, you click send |
| Google Calendar | Schedule discovery calls and deadlines | Read availability first |
| Notion | CRM, content calendar, templates | One workspace page |
| Airtable | Lead and product databases | Test base |
| Canva | Gig thumbnails, covers, social posts, pitch decks | Generate designs, you review and export |
| Figma | UI mockups for app/MVP offers | Create in a test file |
| Zapier / Make | Cross-app automations to deliver client work or run your own | Test scenarios on dummy data |
| GitHub | Portfolio repos and backups | Read + push to your own repo only |
| Browser tools | Research and form-filling | Public sites; no logins to client accounts |

## Free MCP servers worth knowing (from modelcontextprotocol/servers)
`filesystem` (limited folder access), `fetch` (read web pages), `git`, `memory`. See `.mcp.example.json`. Only add servers you trust and understand; review code from unknown authors before enabling.

## Typical flows
1. **Proposal -> Gmail draft:** Claude writes the reply, saves as a draft; you read and send.
2. **Gig -> Canva:** Claude creates three thumbnail concepts; you pick, tweak and export.
3. **Lead tracker -> Notion/Airtable:** keep CSV in Git (private) or sync to a database for easier use.
4. **Client onboarding -> Calendar:** schedule kickoff and milestone reminders.
5. **Automation delivery -> Zapier/Make:** build and test client flows.

## Checklist before enabling a connector
- [ ] What exactly will it read/write?
- [ ] Is a draft/read-only mode available?
- [ ] Is this account separate from sensitive personal data?
- [ ] Do I know how to disconnect it?
