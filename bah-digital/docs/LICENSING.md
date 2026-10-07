# Licensing: what you may sell

Not legal advice. Re-check a tool's license before building a product on it.

| Tool | License | Internal / client work | Resell as part of your SaaS |
|---|---|---|---|
| PostgreSQL | PostgreSQL (permissive) | ✅ | ✅ |
| Qdrant | Apache-2.0 | ✅ | ✅ |
| Ollama | MIT | ✅ | ✅ (each model has its own license, so check it) |
| LiteLLM | MIT (core; enterprise features separate) | ✅ | ✅ |
| Open WebUI | BSD-3 with a branding clause | ✅ | ⚠️ keep its branding unless you have an enterprise license, or build your own UI |
| n8n | Sustainable Use License | ✅ your business + building workflows for clients | ❌ do not host n8n as a paid product for others without an n8n commercial agreement |
| Models (Qwen, Llama, Gemma…) | each different | usually ✅ | check usage limits |
| Free cloud API tiers | provider terms | ✅ for development | ⚠️ free tiers often forbid or limit production use, so move to paid tiers when SaaS customers depend on them |

**Design rule:** the SaaS product customers pay for runs on Bah.Digital's
**own code** (in `services/`) plus permissively licensed parts. n8n stays
Bah.Digital's internal engine.
