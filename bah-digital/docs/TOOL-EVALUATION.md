# Tool evaluation pipeline

We never "install everything". Each new tool passes these checks first.

| Check | Pass if |
|---|---|
| License | allows how we plan to use it (see LICENSING.md) |
| Security | no open critical issues; trusted maintainers; pinned version |
| Maintenance | a release or commits in the last 3 months |
| Community | real users and issues being answered |
| Documentation | we can set it up from the docs alone |
| Fit | it solves a need on the roadmap; no existing tool already covers it |
| Resources | runs within the RAM budget (8 GB laptop now, VPS later) |
| Sandbox test | works in an isolated test container with test data |

**Result:** APPROVE / WATCH (check again in 3 months) / REJECT. Record it in `models/` or `docs/tools/<name>.md`.
