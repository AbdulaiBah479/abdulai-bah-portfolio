# 06. How to use Claude in this project

## The pieces, with an analogy
Imagine Claude is a smart new employee, and this folder is the company.
| Piece | Real-world analogy | Where it lives |
|---|---|---|
| `CLAUDE.md` | The employee handbook (rules, who you are) | root |
| **Skills** | Recipe cards for jobs ("how we write a proposal") | `.claude/skills/` |
| **Subagents (agents)** | Specialist colleagues (researcher, copywriter) Claude can hand work to | `.claude/agents/` |
| **Slash commands** | Shortcut buttons (`/gig`) that start a recipe | `.claude/commands/` |
| **Playbooks / cheatsheets** | Textbook / quick card Claude reads and you can read too | `playbooks/`, `cheatsheets/` |
| **Trackers** | Your spreadsheets Claude updates | `tracker/` |
| **Connectors (MCP)** | Phone lines to outside apps (Gmail, Drive, Canva, Notion) | `.mcp.example.json` + Claude settings |

You do not need to remember all names. Just describe what you want; Claude picks the right recipe. Commands are for speed.

## The commands
| Type | Use when |
|---|---|
| `/start` | First time, or to redo your personal plan |
| `/explain <word>` | Anything confusing, in simple words with an example |
| `/idea` | You want ideas that fit your skills |
| `/niche` | Choose and validate what to sell |
| `/gig <service>` | Fiverr gig |
| `/proposal <job post>` | Answer a job |
| `/audit <business>` | Free audit for outreach |
| `/case-study` | Turn a project into proof |
| `/chatbot` | Plan or deliver an AI chatbot project |
| `/product <idea>` | Create a digital product |
| `/course <topic>` | Create a mini-course |
| `/ebook <topic>` | Write and publish an ebook |
| `/launch-checklist <item>` | Quality check before publishing |
| `/weekly-review` | Numbers and next steps |

## How to talk to Claude (good prompts)
A good request has: **goal, who it is for, what you have, limits, what "done" looks like.**
- Weak: "make me a gig".
- Strong: "I'm a beginner on Fiverr. Build a gig for AI FAQ chatbots for small clinics using my 'AI Chatbot System' project as proof. Price Basic at the minimum that still pays me $15/hour. Use my voice: simple and friendly. Output the full text and tell me what images to make."

Useful phrases:
- "Explain like I'm new. Then do it."
- "Give me 3 options and recommend one with reasons."
- "Don't invent facts or numbers. Mark anything you're unsure of."
- "What do I need to do by hand after this?"
- "Check this against the red-flag list."

## Always check Claude's work
Claude can be wrong or too confident. Before you publish or send anything:
1. Is every claim true about YOU?
2. Are numbers, fees and rules current? (verify on the platform)
3. Does it sound like you?
4. Did it copy from somewhere? (Run a plagiarism check for text sold as original.)
5. Would you be comfortable if the client saw how it was made?

## Working with files
Claude saves outputs in folders (`products/`, `ebooks/`, `clients/`). Open them in VS Code. Edit freely. Tell Claude when you changed something ("I edited gig-chatbot.md, use that version").

## Permissions and safety
Approve actions you understand. Do not let Claude send emails, post publicly, or spend money without reading the exact content first. Do not paste passwords or client secrets into the chat. Keep `.env` files out of Git.

## Context tips (so Claude stays sharp)
Long chats get fuzzy. Use `/clear` between big tasks. Use `/compact` to summarise when a task is long. Keep key decisions written in files (`my-plan.md`) rather than only in chat.

## Connectors (optional power-ups)
If your Claude setup has connectors, they can: draft emails in Gmail (you press send), save docs to Google Drive, manage a CRM in Notion/Airtable, design thumbnails and covers in Canva, mock up apps in Figma, build automations in Zapier/Make. Read `resources/mcp-and-connectors.md` before enabling any.
