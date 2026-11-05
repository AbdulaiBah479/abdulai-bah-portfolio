---
name: chatbot-project-delivery
description: Plan and deliver a client AI chatbot (FAQ/RAG or lead-capture) using a free/open-source stack: requirements, knowledge-base prep, architecture, guardrails, test set, deployment, handover and pricing. Use for /chatbot or any chatbot gig or project.
---

# Chatbot project delivery

Read `offers/01-offers-catalog.md` (#3, #9) and `../bah-digital` docs for the local AI stack and licensing.

## Phases
1. **Discovery (1 hr).** Goal (answer questions? capture leads? book appointments?), top 20 questions, channels (web, Telegram, Messenger; verify WhatsApp requirements), languages, handoff to humans, success metrics, privacy limits.
2. **Knowledge base.** Collect only documents the client owns/permits. Convert PDFs/Word/web to clean text (markitdown, docling, OCRmyPDF). Remove personal data. Chunk by topic with titles.
3. **Architecture choice.** Simple: prompt + FAQ in context (small KB). Medium: RAG with an embedding model + vector store (Qdrant/Chroma). Platforms to evaluate: Langflow, Dify, Open WebUI (check licences; Flowise repo is archived). Model: Claude API (client pays usage) or local model for private data if hardware allows.
4. **Guardrails.** System prompt: answer only from sources, cite the source, say "I don't know" and offer human contact, refuse out-of-scope, never give medical/legal/financial advice, collect leads only with consent.
5. **Test set.** 30+ real questions incl. trick questions, typos, other languages. Score accuracy, safety, tone. Fix prompt/KB until >= agreed threshold; show the client the results honestly.
6. **Deploy.** Embed widget or connect channel; add logging with consent; rate limits; fallback message. Document costs (API usage estimates).
7. **Handover.** 1-page admin guide, how to update the KB, how to review conversations, limitations, support terms, 14-30 days of tuning.
8. **Productize.** Remove client data and publish a starter kit and case study (with permission).

## Deliverables checklist
Requirements doc | KB folder | Config/prompt files | Test report | Deployment notes | Admin guide | Support terms | Invoice.

## Honesty rules
Never claim 100% accuracy. Label it an assistant, not a human. Disclose data processing in plain language. Keep API keys in env vars, never in code or chat.
