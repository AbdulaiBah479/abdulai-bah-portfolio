# Bah.Digital

**An AI-powered digital transformation company, and the AI Operating System that runs it.**

Bah.Digital works two ways from one platform:

| Mode | Who uses it | How you earn |
|---|---|---|
| **Service / freelance** | You (and later a team) deliver work to clients | Projects, retainers, consulting |
| **SaaS** | Customers log in and use selected tools themselves | Monthly subscriptions, usage |

```
                         BAH.DIGITAL
              ┌───────────────┴────────────────┐
       SERVICE BUSINESS                  SAAS PLATFORM
              └───────────────┬────────────────┘
                     BAH AI OPERATING SYSTEM
       ┌──────────────────────┼──────────────────────┐
   AI WORKFORCE        AUTOMATION ENGINE         KNOWLEDGE
   agents, models      n8n, APIs, MCP        PostgreSQL, Qdrant
       └──────────────────────┼──────────────────────┘
                     EXECUTION + QA + APPROVAL
                              │
                        CLIENT RESULT
```

## Start here

1. **[docs/STEP-BY-STEP.md](docs/STEP-BY-STEP.md)**: exactly what to type, one step at a time
2. [docs/ROADMAP.md](docs/ROADMAP.md): all 14 phases, timeline and checklist
3. [docs/BUSINESS-PLAN.md](docs/BUSINESS-PLAN.md): services, pricing, income streams, payments
4. [docs/GOVERNANCE.md](docs/GOVERNANCE.md): autonomy levels, approvals, client data isolation
5. [docs/LICENSING.md](docs/LICENSING.md): what each tool lets you sell
6. [docs/TOOL-EVALUATION.md](docs/TOOL-EVALUATION.md): how new tools get approved

## V1 stack (all free and open source)

| Service | What it does | Address on your PC |
|---|---|---|
| PostgreSQL | Main database | `localhost:5432` |
| Qdrant | Vector memory for RAG | http://localhost:6333/dashboard |
| Ollama | Runs AI models on your own computer | `localhost:11434` |
| Open WebUI | ChatGPT-style interface for all models | http://localhost:3000 |
| n8n | Workflow automation | http://localhost:5678 |
| LiteLLM | AI gateway: one API, free-first routing, fallbacks | http://localhost:4000/ui |

## Everyday commands

```bash
./scripts/health.sh          # what is running?
docker compose up -d         # start everything
docker compose stop          # stop everything (data is kept)
docker compose logs -f n8n   # watch one service's logs
./scripts/backup.sh          # back up databases + config
```

## Folder map

```
agents/          AI workforce: role definitions (CEO, research, marketing...)
automation/      n8n workflow exports
clients/         one private folder per client (never committed to Git)
config/          service configuration (model router etc.)
data/            local runtime data (not committed)
docs/            plans, guides, policies
infrastructure/  database init, proxy, server setup
knowledge/       company knowledge for RAG
mcp/             tool servers that give agents "hands"
models/          model registry and evaluations
monitoring/      health, metrics, alerts
scripts/         setup, health, backup helpers
services/        Bah.Digital's own code (APIs, portal, SaaS)
tests/           automated tests and AI evaluations
workflows/       SOPs: how each service is delivered, step by step
```
