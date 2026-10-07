# Governance: powerful and trustworthy

**Maximum capability + minimum permissions + verification + audit log + human
approval for risky actions.**

## Autonomy levels (set per client and per workflow)

| Level | AI may… | Example |
|---|---|---|
| 0 Suggest | advise only | strategy ideas |
| 1 Prepare | create drafts; a human sends them | proposals, emails to new contacts |
| 2 Reversible | act when the action can be undone | save drafts, create CRM records |
| 3 Routine | run pre-approved repeating tasks | scheduled posts from an approved calendar |
| 4 Workflow | manage a whole workflow within limits | support inbox with escalation |
| 5 Process | run a business process within written policy | full content pipeline incl. publishing |

**Always requires your approval, at any level:** payments, deleting data,
contracts, legal/medical/financial advice, messages to new external
contacts, publishing for a client for the first time, credential changes, and
production deployments.

## Client data isolation

- Every client has its own folder, database schema/tenant id, vector collection and credentials.
- An agent working for Client A can never see Client B's data.
- Client data never goes into Git, and never into a free cloud model without the client's consent. Use local models for sensitive data.
- Every agent action is logged: who, what, when and why.

## Safe self-healing

Health check fails → restart → still failing → diagnose → **backup → test the fix in a sandbox → approval → deploy**.
The system never edits production on its own.
