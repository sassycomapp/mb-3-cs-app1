# mb-3-cs — config

State of the mb-3-cs project and its App 1 repository, as verified 2026-11-25.

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
| `mb-3-cs-project-library` | Documentation, ADRs, wireframes, design artefacts; the planning authority. Git repository on GitHub (`sassycomapp/mb-3-cs-project-library`); GBrain source registered, federated; on the commit tools with the hook installed |
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
| Design doc (run app1) | `mb-3-cs-project-library\docs-local\design\app1\design-doc.md` — the reviewed plan; sections 16–24, the Step 15 review body and the GSTACK REVIEW REPORT last |
| `pilot-doc.txt` | `theme/assets/docs/app1/pilot-doc.txt` — keeps the folder alive in Anvil; never delete |
| Project context | `mb-3-cs-project-context` (sibling folder) — GBrain source `mb-3-cs-project-context`, federated |

## PDLF

| Item | Value |
|---|---|
| Entry | 03 `new-app-with-context`, taken 2026-10-30 |
| Run | `app1`, route Application |
| Last step | 22 complete 2026-11-18 (143 screen requirements in the project library's `ui\`; requirement index, checks and cross-check in `pdlf-outputs\c22\`; receipt written 2026-11-25 on resume; DC-16/DC-05 143/143; BFT Full) |
| Next step | 23 (Phase C, design review) |
| Gates | `domain-locked` passed 2026-11-12; `concept-locked` passed 2026-11-18; next gate `screens-approved` at Step 26 (end of Phase C) |
| Ledger | Database `pdlf`, port 5433, through the PowerShell bridge of PDLF's `spec-postgres-ledger` |

## Open items

- The 71-table schema was applied 2026-11-17: `anvil.yaml` `db_schema` equals `authoritative-schema.md` (zero differences; ST-06/ST-07 pass; the live tables match). The migration log's 2026-11-17 row supersedes prompts P1–P14/P13a as the application method.
- AC-6 (Anvil's written confirmation of the account structure) and AC-14 (SES production access) are outstanding; both before the first paying client.
