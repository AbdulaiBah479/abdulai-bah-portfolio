# Repo picker: "I want to ___, so I use ___"

`github-repos.md` has about 300 projects. That is far too many to learn. This page tells you which ONE or TWO to look at for each goal. Everything here is in `github-repos.md` (verified to exist on 2026-11-04). Before using any repo for paid work, open it on GitHub, read the README, check the licence and the date of the last update.

## How to judge a repo in 2 minutes
1. **Last update** within the last year? (Old = risky.)
2. **Archived?** A banner at the top says so. Archived = no more fixes; use only to learn.
3. **Licence?** MIT / Apache-2.0 / BSD are the friendliest. GPL/AGPL mean you must share changes in some cases, usually fine for internal use but careful if you ship it to clients. "Custom" or "fair-code" = read it.
4. **Stars?** Just a popularity signal, not quality.
5. **Does the README show a working demo?** If you can't run it in 30 minutes, skip it.
6. **Never run commands from a repo you don't understand.** Ask Claude to explain the install steps first.

## The starter pack: only learn these 10 first
| # | Repo | Why |
|---|---|---|
| 1 | n8n-io/n8n | The core of your automation offers |
| 2 | microsoft/markitdown | Turns client documents into clean text for chatbots |
| 3 | langflow-ai/langflow or langgenius/dify | Build chatbots visually |
| 4 | Mintplex-Labs/anything-llm | Fast "chat with your documents" demo for sales |
| 5 | jgm/pandoc | Your ebook factory |
| 6 | withastro/astro | Fast landing pages for clients |
| 7 | GoogleChrome/lighthouse | Audit a website for your free audits |
| 8 | knadh/listmonk or free email tools | Your newsletter |
| 9 | gitroomhq/postiz-app | Schedule your content |
| 10 | anthropics/claude-cookbooks | Recipes for the Claude API |

## By goal
### Get clients
- Find proof of demand: `f/prompts.chat` (see what people ask AI for), `remoteintech/remote-jobs` (companies to approach)
- Free website audits: `GoogleChrome/lighthouse`, `microsoft/playwright` (screenshots)
- Outreach organisation: `twentyhq/twenty` (CRM) or a spreadsheet
- Scheduling calls: `alextselegidis/easyappointments`
- Track client websites for a care plan: `louislam/uptime-kuma`

### Deliver AI chatbot work
- Build visually: `langflow-ai/langflow`, `langgenius/dify`
- Chat with documents: `Mintplex-Labs/anything-llm`, `infiniflow/ragflow`
- Convert files: `microsoft/markitdown`, `docling-project/docling`
- Store knowledge: `chroma-core/chroma` (simplest), `qdrant/qdrant`
- Test quality: `promptfoo/promptfoo`
- Watch usage: `langfuse/langfuse`
- Official examples: `anthropics/claude-cookbooks`, `anthropics/anthropic-sdk-python`
- Learn: `microsoft/generative-ai-for-beginners`

### Deliver automation work
- Main tool: `n8n-io/n8n`; alternatives `activepieces/activepieces`, `node-red/node-red`, `huginn/huginn`
- Learn from examples: `Zie619/n8n-workflows` (study, don't copy-resell)
- Background jobs: `triggerdotdev/trigger.dev`

### Build websites and apps
- Simple sites: `withastro/astro`, `gohugoio/hugo`, `11ty` alternatives
- Web apps: `vercel/next.js` + `shadcn-ui/ui` + `tailwindlabs/tailwindcss`
- Mobile: `expo/expo`
- Backend without much code: `supabase/supabase`, `appwrite/appwrite`
- Admin dashboards: `tabler/tabler`, `ColorlibHQ/AdminLTE`
- Starters: `ixartz/SaaS-Boilerplate`, `t3-oss/create-t3-app`
- Hosting yourself: `coollabsio/coolify`, `caddyserver/caddy`
- Client edits content easily: `decaporg/decap-cms`, `TryGhost/Ghost`, `strapi/strapi`

### Make designs and videos
- Diagrams for proposals: `excalidraw/excalidraw`, `mermaid-js/mermaid`, `jgraph/drawio`
- Icons and fonts (check licences): `lucide-icons/lucide`, `tabler/tabler-icons`, `rsms/inter`
- Screen recording for demos and courses: `obsproject/obs-studio`
- Quick edits: `mifi/lossless-cut`, `mltframework/shotcut`
- Remove backgrounds: `danielgatis/rembg`; enlarge images: `upscayl/upscayl`
- Subtitles: `ggml-org/whisper.cpp`, `SYSTRAN/faster-whisper`, `m-bain/whisperX`

### Create and sell ebooks and courses
- Build files: `jgm/pandoc`, `typst/typst`, `kovidgoyal/calibre`, `Sigil-Ebook/Sigil`
- Test on a reader: `readest/readest`
- Docs-style books online: `rust-lang/mdBook`, `quarto-dev/quarto-cli`, `squidfunk/mkdocs-material`
- Grammar: `languagetool-org/languagetool`
- Notes: `logseq/logseq`, `laurent22/joplin`
- Course slides: `marp-team/marp-cli`
- Course videos: `obsproject/obs-studio`

### Sell digital products
- Study how a creator store works: `antiwork/gumroad`
- Your own store later: `medusajs/medusa`, `saleor/saleor`
- Newsletters/memberships: `TryGhost/Ghost`
- Template ideas: n8n workflows, Notion-style templates, UI kits, SaaS starters, Chrome extensions (`GoogleChrome/chrome-extensions-samples`)

### Grow an audience
- Posts: `gitroomhq/postiz-app`, `inovector/mixpost`
- Email: `knadh/listmonk`, `pentacent/keila`
- Stats: `umami-software/umami`, `plausible/analytics`, `arp242/goatcounter`
- Test headlines/pages: `growthbook/growthbook`

### Run the business
- Invoices: `invoiceninja/invoiceninja`, `InvoiceShelf/InvoiceShelf`
- E-signatures: `docusealco/docuseal`, `documenso/documenso`
- Time tracking: `solidtime-io/solidtime`, `kimai/kimai`
- Projects: `makeplane/plane`, `kanboard/kanboard`
- Docs/handbooks: `BookStackApp/BookStack`, `outline/outline`
- Receipts and documents: `paperless-ngx/paperless-ngx`
- Budget: `actualbudget/actual`, `firefly-iii/firefly-iii`
- Passwords: use hosted Bitwarden first; `keepassxreboot/keepassxc` offline
- Backups: `restic/restic`, `rclone/rclone`, `syncthing/syncthing`

### Learn (free)
- Web: `freeCodeCamp/freeCodeCamp`, `microsoft/Web-Dev-For-Beginners`
- AI: `microsoft/generative-ai-for-beginners`, `anthropics/prompt-eng-interactive-tutorial`, `dair-ai/Prompt-Engineering-Guide`, `mlabonne/llm-course`
- Command line: `jlevy/the-art-of-command-line`
- Project ideas: `practical-tutorials/project-based-learning`, `codecrafters-io/build-your-own-x`, `Shubhamsaboo/awesome-llm-apps`
- Lists of lists: `sindresorhus/awesome`, `awesome-selfhosted/awesome-selfhosted`, `ripienaar/free-for-dev`

### Claude skills, agents and MCP
- Skills: `anthropics/skills`, `obra/superpowers`, `coreyhaines31/marketingskills`
- Subagents: `wshobson/agents`, `VoltAgent/awesome-claude-code-subagents`
- Discovery lists: `hesreallyhim/awesome-claude-code`, `ComposioHQ/awesome-claude-skills`, `punkpeye/awesome-mcp-servers`
- Build your own: `modelcontextprotocol/python-sdk`, `anthropics/claude-agent-sdk-python`
**Security rule:** a skill or MCP server can run commands or read files. Only install ones you have read and understand.

## With 8 GB RAM
Prefer hosted free tiers and lightweight tools (Astro, Hugo, SQLite, small local models via `ggml-org/llama.cpp`). Avoid running ERP/CRM suites (Odoo, ERPNext), big vector stacks and image-generation UIs on your laptop. Add one heavy service at a time.
