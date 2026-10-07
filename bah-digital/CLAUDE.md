# Bah.Digital: instructions for Claude Code

You are running on the owner's own computer (Windows 11 + WSL2 Ubuntu +
Docker Desktop, 8 GB RAM). The owner is new to this and wants you to **do the
work yourself**. They will approve permissions.

## How to work
- Follow `docs/STEP-BY-STEP.md` and `docs/ROADMAP.md`. Do one step at a time,
  verify it (`./scripts/health.sh`), then report in plain, beginner-friendly language.
- After a step is verified, tick it in `docs/ROADMAP.md`, commit and push.
- Ask before: anything costing money, creating accounts, deleting data or
  volumes, exposing a port beyond 127.0.0.1, or changing Windows settings.
- Never print, commit or share secrets from `.env`. Never commit `clients/` data.
- Pin image versions; follow `docs/TOOL-EVALUATION.md` before adding any tool.
- Mind the RAM: run only the services the current step needs.
- Free and open-source first. Paid only: Claude Pro, Canva Pro, CapCut Pro, domain.
- Follow `docs/GOVERNANCE.md` (autonomy levels, client isolation) and
  `docs/LICENSING.md` (never resell hosted n8n).
