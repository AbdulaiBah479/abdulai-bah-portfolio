# Claude Code cheat sheet for this project

## Start
```bash
cd freelance-hq
claude            # skills, agents, commands in .claude/ load automatically
```

## This project's commands
| Command | Does |
|---|---|
| `/niche [idea]` | Validate niche/offer with market evidence |
| `/gig [service]` | Build a complete Fiverr gig |
| `/proposal [job post]` | Triage and write a proposal |
| `/product [idea]` | Plan, build, launch a digital product |
| `/ebook [topic]` | Ebook pipeline |
| `/weekly-review` | Numbers, diagnosis, next-7-days plan |
| `/launch-checklist [item]` | Pre-launch audit |

## Useful built-ins
`/help`, `/clear` (reset context), `/compact` (summarise to save context), `/agents` (manage subagents), `/mcp` (connectors), `/memory`, `/permissions`, `/init`. Press `Esc` to interrupt; `Shift+Tab` to cycle permission modes (verify in your version).

## Working patterns
- "Use the proposal-specialist agent on this job: ..."
- "Run market-researcher on [niche] in parallel with gig-copywriter drafting titles."
- "Read playbooks/06-digital-products.md then plan my first product."
- "Update tracker/leads.csv with these proposals."

## Safety
Review file writes; keep `clients/` out of git; never paste API keys; approve network and MCP actions deliberately.
