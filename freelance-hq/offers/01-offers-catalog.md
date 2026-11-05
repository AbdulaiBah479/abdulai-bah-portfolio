# Offers catalog (16 ready-to-test offers)

Each offer lists: **buyer**, **promise**, **tiers with starting-point prices** (test; local markets vary), **delivery steps**, **free tools**, **Claude's role**, **risks**. Prices assume global marketplaces in USD; adjust after checking real competitors. Always net out fees using `python3 scripts/price_calc.py`.

---
## 1. One-workflow automation (n8n / Make / Activepieces)
- **Buyer:** small agencies, clinics, shops, coaches drowning in repetitive admin.
- **Promise:** "I automate one repetitive task (lead follow-up, invoice reminders, report emails, form -> CRM) in 3 days."
- **Tiers (test):** Basic ($40-80 one simple 2-app flow) | Standard ($120-250 multi-step with error alerts and docs) | Premium ($300-600 3 workflows + dashboard + training video).
- **Delivery:** map the manual process on paper -> build in n8n -> test with fake data -> hand over with a 1-page doc + short screen recording -> 14 days support.
- **Free tools:** n8n self-host (or client's account), Google Sheets/Airtable, Gmail, webhooks.
- **Claude's role:** process mapper, workflow design, code snippets (JS/Python function nodes), documentation, test cases.
- **Product potential:** sanitize and sell workflow packs (see skill `n8n-workflow-productizer`). Check n8n's licence: you can deliver automations to clients; do not resell n8n as a hosted service.
- **Risks:** client credentials (never store them; use the client's own accounts with limited scopes), data privacy, vague scope.

## 2. Landing page in 48 hours
- **Buyer:** freelancers, restaurants, events, local services, product launches.
- **Promise:** a fast, mobile-ready one-page site with contact/booking form.
- **Tiers:** Basic ($40-90 template-based) | Standard ($120-250 custom, copy included, SEO basics) | Premium ($300-500 + analytics + 2 revisions + 30-day support).
- **Delivery:** intake form -> wireframe -> build (Astro/Hugo/plain HTML/Next.js; host on Netlify/Vercel/Cloudflare Pages/GitHub Pages) -> client review -> domain connection help.
- **Claude's role:** copywriting, section structure, accessibility and speed checks, code.
- **Product potential:** sell landing page templates by niche (dentist, gym, photographer).
- **Risks:** image/font licences, client content rights, domain/hosting confusion (clear instructions).

## 3. AI FAQ chatbot for a website (RAG)
- **Buyer:** businesses answering the same questions daily.
- **Promise:** "A chatbot trained on YOUR documents that answers customers and captures leads."
- **Tiers:** Basic ($80-150 FAQ bot, up to 20 pages) | Standard ($200-450 + lead capture + handoff email) | Premium ($500-1,000 + analytics + multi-language + 30 days tuning).
- **Delivery:** collect docs -> clean (markitdown/docling) -> chunk + embed -> prompt guardrails ("only answer from sources; say I don't know") -> embed widget -> test 30 questions -> train the client.
- **Free tools:** open-source stacks (Flowise is archived, so prefer Langflow, Dify, or Open WebUI; verify licences), vector DB (Qdrant/Chroma), Claude API (usage cost) or local models for private data.
- **Claude's role:** architecture, prompt, test set, evaluation, docs. See skill `chatbot-project-delivery`.
- **Product potential:** "Chatbot starter kit" and ebook "Build your first business chatbot".
- **Risks:** hallucinations (use sources + tests), privacy (no sensitive personal data without agreement), ongoing API costs (client pays).

## 4. Ebook formatting + publishing setup
- **Buyer:** first-time authors, coaches with manuscripts, small publishers.
- **Promise:** "Your manuscript becomes a clean EPUB/Kindle-ready file plus a print-ready PDF."
- **Tiers:** Basic ($30-60 EPUB) | Standard ($80-150 EPUB + PDF + metadata sheet) | Premium ($200-350 + cover brief + upload walkthrough).
- **Delivery:** receive .docx -> clean styles -> convert with Pandoc/Calibre/Sigil -> validate (EPUBCheck, Kindle Previewer) -> deliver files + checklist.
- **Claude's role:** structure fixes, front/back matter, consistency checks, metadata writing.
- **Product potential:** formatted ebook templates; ebook "Self-publish on KDP step by step" (from your own experience).
- **Risks:** you must not edit content without permission; do not publish for them using your account.

## 5. Transcription + subtitles + show notes
- **Buyer:** podcasters, YouTubers, trainers, researchers.
- **Promise:** accurate text and subtitle files within 48 hours.
- **Tiers:** priced per audio minute or per episode bundle (test).
- **Delivery:** Whisper/faster-whisper -> human proofread -> SRT/VTT + summary + chapters.
- **Risks:** accents and names (proofread), confidentiality (offer local processing), copyrighted material.

## 6. Brand kit + social templates (Canva)
- **Buyer:** new small businesses and coaches.
- **Promise:** a consistent look: logo usage, colours, fonts, 12-20 editable templates.
- **Tiers:** Basic ($30-70 palette + 6 templates) | Standard ($100-200 + 15 templates + guide) | Premium ($250-450 + 30 templates + monthly refresh).
- **Delivery:** brand questionnaire -> moodboard -> templates in Canva Brand Kit -> quick training.
- **Product potential:** sell template packs by niche (real estate, fitness, coaches) on Etsy/Gumroad/Creative Market (check Canva template-selling terms).
- **Risks:** trademark clashes, font/element licences.

## 7. Short-video editing pack (CapCut)
- **Buyer:** creators, restaurants, real estate agents, local brands.
- **Promise:** 8 captioned vertical videos from raw footage.
- **Tiers:** by count and length; add a thumbnail pack.
- **Delivery:** brief -> edit -> captions -> review -> export for each platform.
- **Risks:** music licences (use platform libraries/royalty-free), raw footage rights, heavy files on 8 GB RAM (render in chunks).

## 8. AI workflow audit (paid report)
- **Buyer:** small teams curious about AI but unsure where to start.
- **Promise:** "A 2-day audit ranking your 5 best automations by ROI, with a 30-day plan."
- **Tiers:** Basic ($50-100 questionnaire + report) | Standard ($150-300 + 45-minute call) | Premium ($350-700 + implementation plan + quote).
- **Delivery:** questionnaire -> process mapping -> time/cost estimate -> report with quick wins -> optional implementation offer.
- **Why it works:** low-risk to buy, builds trust, leads to bigger projects. Great for direct outreach.
- **Product potential:** audit checklist + spreadsheet calculator as a product.

## 9. Lead-capture bot (Telegram / Messenger / website)
- **Buyer:** service businesses that lose leads outside office hours.
- **Promise:** a bot that qualifies visitors and books calls.
- **Notes:** WhatsApp Business API has approval, costs and policy rules; start with web chat, Telegram or Messenger and verify WhatsApp requirements before promising it.
- **Delivery:** conversation flow design -> build -> connect to calendar/CRM -> test -> train.

## 10. Local business digital starter pack
- **Buyer:** offline businesses with no/weak online presence.
- **Promise:** Google Business Profile polish, simple one-page site, booking link, review-request automation, 3 starter social posts.
- **Tiers:** Basic | Standard | Premium plus monthly care.
- **Delivery:** `/audit` as the free first step -> pilot at reduced price -> case study.
- **Why it works:** many local owners pay for "done for you" and rarely shop around on Fiverr, so direct outreach is key.

## 11. Claude Project / custom assistant setup + team training
- **Buyer:** small teams who want AI helping with proposals, support replies, reports.
- **Promise:** a custom AI assistant with their documents and rules, plus a 60-minute training session.
- **Delivery:** discovery -> knowledge base -> instructions + examples -> test -> train -> handoff doc.
- **Risks:** data privacy and what the client's plan allows; don't promise unlimited accuracy.

## 12. Prompt library for one profession
- **Buyer:** realtors, teachers, recruiters, accountants, clinic admins (choose ONE).
- **Promise:** 50 tested prompts + workflows for their daily tasks, in a searchable Notion/Sheet.
- **Sell as:** service (customised) and product (generic). Includes safety notes for that profession (e.g. no private client data).
- **Risks:** accuracy in regulated fields (legal/medical/finance): add disclaimers and review steps.

## 13. Document/data extraction to spreadsheet
- **Buyer:** small firms with piles of PDFs/invoices/forms.
- **Promise:** structured spreadsheet from messy documents with accuracy checks.
- **Tools:** OCRmyPDF, markitdown, docling, Python scripts, Sheets.
- **Risks:** sensitive data, error rates (spot-check 10%, report accuracy honestly).

## 14. App MVP prototype (fixed scope)
- **Buyer:** founders with an idea and small budgets.
- **Promise:** a clickable or working prototype of the core feature in 2-3 weeks.
- **Delivery:** user stories -> screens -> build (Next.js/Expo/Supabase or PocketBase alternative; note PocketBase repo is archived, verify) -> demo -> source handover.
- **Risks:** scope creep (strict milestones), ownership of code, maintenance expectations.

## 15. Monthly care plan (retainer)
- **Buyer:** past clients.
- **Promise:** fixed monthly hours for updates, fixes, reports, small improvements.
- **Price idea:** a monthly fee equal to ~hours x rate x 0.9; minimum 3 months.
- **Why:** predictable income; reduces the need to hunt.

## 16. Translation / localization (only if you are fluent)
- **Buyer:** businesses expanding to your language markets.
- **Promise:** natural, context-aware translations with glossary and consistency checks.
- **Use AI as a first draft only; a fluent human must review.** Disclose AI-assisted workflow if the client or platform requires it.

---
## For every offer, prepare
1. One-sentence promise. 2. Three tiers. 3. Intake form. 4. Delivery checklist. 5. One case study. 6. Two FAQ answers about price and revisions. 7. A "no" list (what you do not do).
Claude builds these with `/gig`, `client-onboarding` and `/case-study`.
