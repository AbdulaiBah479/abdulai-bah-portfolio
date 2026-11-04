---
name: client-onboarding
description: Onboard a newly won client or order: intake questionnaire, scope of work, contract-lite, milestones, kickoff message, client folder scaffold. Use when the user wins a job, receives a Fiverr order, or needs to scope a project and avoid scope creep.
---

# Client onboarding

Read `playbooks/12-client-delivery-and-reviews.md`.

## Steps
1. Scaffold: `bash scripts/new_client.sh "<client-name>"` creates `clients/<slug>/` (brief, scope, comms log, deliverables). `clients/` is git-ignored: never commit it.
2. **Intake**: send `templates/client-intake-questionnaire.md` (goal, audience, references, assets, access, deadline, approver, success metric).
3. **Scope of work** from `templates/scope-of-work.md`: deliverables, out-of-scope list, assumptions, revisions included, timeline, milestones, acceptance criteria, change-request process.
4. **Contract-lite** from `templates/contract-lite.md` for direct clients: payment terms, IP transfer on full payment, confidentiality, kill fee. On marketplaces the platform terms apply; still confirm scope in writing in-platform. Recommend a lawyer review for large or recurring deals.
5. **Payment structure**: marketplace escrow/milestones; direct = 30-50% deposit, balance on delivery (never deliver final source before payment).
6. **Kickoff message**: confirm understanding in 5 bullets, list what you need from them and by when, state next update date.
7. **Comms rhythm**: reply within 24h, a short progress update at each milestone, a written summary after calls.
8. After delivery: request revisions window, collect feedback, ask for a review, propose the next step (retainer/upsell). See `templates/testimonial-request.md`.
9. Update `tracker/leads.csv` (won) and `tracker/income.csv` when paid.
