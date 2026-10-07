# Bah.Digital roadmap

**Rule:** we never start a phase until the one before it works and is backed up.
Times assume about 2 to 3 hours per day as a beginner. **You start earning in Month 1**:
the platform grows while you sell.

| # | Phase | Time | Done when… | Earn from it |
|---|---|---|---|---|
| 0 | **Foundation**: repo, folders, secrets, scripts | 1 to 2 days | `setup.sh` all green | (none yet) |
| 1 | **Local AI core**: Postgres, Qdrant, Ollama, Open WebUI, n8n | 3 to 7 days | `health.sh` all UP | AI business audits (sold manually) |
| 2 | **AI gateway + router**: LiteLLM, free-first chains, fallbacks, usage tracking | 3 to 5 days | agents call `bah-fast` etc. | (none yet) |
| 3 | **Knowledge brain**: document ingestion, embeddings, RAG, client-isolated memory | 1 to 2 weeks | ask questions about your documents, with sources | **AI chatbot / knowledge assistant** packages |
| 4 | **Agent workforce**: CEO orchestrator plus Research, Marketing, Creative, Coding, Data, Support, Ops (LangGraph) | 2 weeks | the CEO splits a request into tasks and assigns them | Research reports, content packages |
| 5 | **MCP tool layer**: GitHub, files, database, web search, permissions | 1 to 2 weeks | agents use tools within their permissions | (none yet) |
| 6 | **Browser + computer use**: Playwright / browser-use, approval gates | 1 to 2 weeks | an agent fills a form as a draft and you approve it | Lead generation, data entry, form automation |
| 7 | **Creative factory**: scripts, images, voice (Whisper/Piper), FFmpeg, Canva + CapCut handoff | 2 to 3 weeks | one idea becomes 10+ content pieces | **Social media retainers** |
| 8 | **Software factory**: OpenHands, templates, tests, CI/CD, deploy | 2 to 4 weeks | a site goes from brief to deployed preview | **Websites, dashboards, apps** |
| 9 | **Business operations**: CRM, proposals, invoicing, onboarding, email | 2 to 3 weeks | a lead becomes a proposal and then an invoice | Scales all services |
| 10 | **Bah.Digital website**: services, portfolio, AI sales assistant, newsletter, booking | 1 to 2 weeks | the site is live on your domain | Inbound leads + newsletter |
| 11 | **Client portal**: login, projects, approvals, reports, files | 2 to 4 weeks | a client can see and approve their project | Premium retainers |
| 12 | **SaaS**: multi-tenancy, plans, billing, usage limits, API | 1 to 3 months | a stranger signs up and pays | **Subscriptions** |
| 13 | **Intelligence engine**: tech radar, competitor and success-pattern research, trend detection | ongoing | monthly "what we should adopt" report | Paid research reports |
| 14 | **Autonomous ops**: monitoring (Uptime Kuma → Prometheus/Grafana), Langfuse, Promptfoo evals, self-healing, VPS production | ongoing | services restart themselves; alerts reach your phone | 24/7 reliability = higher prices |

## Calendar view

| When | Build | Sell |
|---|---|---|
| **Month 1** | Phases 0 to 3 | AI audits, simple chatbots, AI-written content |
| **Month 2** | Phases 4 to 6 | Automations (n8n), research reports, lead generation |
| **Month 3** | Phases 7 to 9 | Social retainers, websites, digital products |
| **Months 4 to 6** | Phases 10 to 11 + move to a VPS | Retainers through the portal, newsletter sponsors |
| **Months 6 to 12** | Phase 12 SaaS MVP, then multi-tenant | Subscriptions + agency + products |

## Master checklist

- [x] 00 Architecture
- [x] 01 Project structure, secrets template, scripts *(built for you)*
- [ ] 02 GitHub repo cloned on your PC + `setup.sh` green
- [ ] 03 PostgreSQL
- [ ] 04 Qdrant
- [ ] 05 Ollama + starter models
- [ ] 06 Open WebUI
- [ ] 07 n8n
- [ ] 08 Free cloud API keys
- [ ] 09 LiteLLM gateway + router
- [ ] 10 First backup
- [ ] 11 Model registry + evaluation (Promptfoo)
- [ ] 12 Document ingestion
- [ ] 13 RAG with sources
- [ ] 14 Per-client memory isolation
- [ ] 15 Agent framework (LangGraph)
- [ ] 16 AI CEO orchestrator
- [ ] 17 to 22 Research, Marketing, Creative, Coding, Data, Support agents
- [ ] 23 to 25 MCP gateway, GitHub tools, browser tools
- [ ] 26 Computer use with approval gates
- [ ] 27 Security hardening
- [ ] 28 Observability (Langfuse)
- [ ] 29 Evaluation suite
- [ ] 30 Self-healing
- [ ] 31 to 34 Creative, video, software and marketing factories
- [ ] 35 CRM (evaluate Twenty / EspoCRM)
- [ ] 36 Client portal
- [ ] 37 Bah.Digital website
- [ ] 38 Payments
- [ ] 39 to 42 SaaS auth, multi-tenancy, billing, deployment
- [ ] 43 to 45 Intelligence engine, innovation engine, tech radar
- [ ] 46 Production hardening on VPS

## What "free" means here

Every piece of software is free and open source, or a free tier. Your only
planned costs are Claude Pro, Canva Pro, CapCut Pro and your domain. **Later**,
when clients pay for it, a VPS for 24/7 hosting (about $5 to $20 a month) is the
first upgrade. Your laptop cannot serve customers around the clock.
