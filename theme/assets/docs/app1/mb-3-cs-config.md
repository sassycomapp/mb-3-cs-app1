# mb-3-cs — config

State of the mb-3-cs project and its App 1 repository, as verified 2026-10-30.

## Identity

| Field | Value |
|---|---|
| Project | Mybizz Consulting Services |
| Slug | `mb-3-cs` |
| Repository | `mb-3-cs-app1` — Anvil app code repository; App 1, the development workspace |
| Branch | `master` (Anvil syncs that branch) |
| PDLF mode | `full` |
| Status | Active; registered in PDLF on 2026-10-30 |

## Repositories

One project folder, `C:\dev\dev-mb-3-cs\`, holds the business's repositories. Local
paths, GitHub repositories, GBrain sources and OpenCode/Cupcake state for every
repository on the machine: `C:\mybizz\mybizz-os-docs\os-reference-docs\repo-organization.md`.

| Repository | Role |
|---|---|
| `mb-3-cs-project-library` | Documentation, ADRs, wireframes, design artefacts; the planning authority. Folder exists; not yet a Git repository |
| `mb-3-cs-app1` | App 1, the development workspace — this repository |
| `mb-3-cs-app2` | App 2, `master_template`; receives App 1's tagged releases |
| `mb-3-cs-app3` | App 3, `blank_client_template`; cloned for each new client |
| `mb-3-cs-app5` | App 5, Mybizz management |

App 4 (client instances) lives on each client's own Anvil account; it has no folder here.

## Agent setup

| Item | State |
|---|---|
| `opencode.json` | Present at repository root |
| `.opencode/` | Present: `agents/`, `plugins/`, `package.json`, own `opencode.json` |
| `AGENTS.md` | Present at repository root; its body is kept current from `theme/assets/docs/app1/mb-3-cs-reference.md` by `agents-from-reference.sh` |
| Commands folder | None |
| Cupcake | Fallback home; no project `.cupcake` skeleton |

## Installed tools

| Tool | State |
|---|---|
| Graphify | `graphify-out/` present in the repository |
| GBrain | No source for this repository; application code is read directly from the app folder |

## Key documents

| Document | Where |
|---|---|
| Project config, reference, explainer, README | `theme/assets/docs/app1/` (this suite) |
| `pilot-doc.txt` | `theme/assets/docs/app1/pilot-doc.txt` — keeps the folder alive in Anvil; never delete |
| Project context | `mb-3-cs-project-context` (sibling folder) — GBrain source `mb-3-cs-project-context`, federated |

## PDLF

| Item | Value |
|---|---|
| Entry | 03 `new-app-with-context`, taken 2026-10-30 |
| Run | `app1`, route Application |
| Next step | 11 (Phase B) |
| Pause | After Step 16 gate `domain-locked`: Phases C to F are not built |
| Ledger | Database `pdlf`, port 5433, through the PowerShell bridge of PDLF's `spec-postgres-ledger` |

## Open items

- `mb-3-cs-project-library` is not yet a Git repository; PDLF Step 11 creates it.
- `product-requirements-document.md` in the project context is frontmatter-only (empty body).
