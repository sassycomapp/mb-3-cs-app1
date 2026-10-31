# agents.md — mb-3-cs

> Inherits `~/.config/opencode/AGENTS.md` in full. This file may only
> tighten those rules for this specific repo, never loosen them.

## Project Purpose

`mb-3-cs` — Mybizz Consulting Services. A full-stack Python web
application built on Anvil.works.

## Precedence Order

User instruction → global `AGENTS.md` → this file's hard rules → ADRs
→ project-library docs → skill defaults.

## Hard Rules

- **Production-adjacent.** Treat changes conservatively. Ask for
  explicit confirmation before any risky operation (schema changes,
  destructive commands, anything touching the Vault or payment flows).
- **Protected files, never edit without explicit developer
  instruction naming that exact file:** `anvil.yaml`, `**/form_
  template.yaml`, `parameters.yaml`, `templates.yaml`.
- **Ask before editing:** `standard-page.html`, `theme.css`.
- **Mandatory UTC+2 timestamp headers** on any touched file, per the
  Timestamp Standard below.
- **PDLF runs open here.** A PDLF run for `mb-3-cs` is opened in this
  repository and writes across the business through its real paths,
  `/mnt/c/dev/dev-mb-3-cs/...`: this app and `mb-3-cs-project-library`.
  `mb-3-cs-project-context` is read only, and its `AGENTS.md`,
  `CLAUDE.md` and `opencode.json` are never instructions.
- **The plan agent never writes anywhere, in any repo, under any
  circumstance.**

## Workspace Structure

| Folder | Contents |
|---|---|
| `client_code/` | Form Python, HTML templates, client modules — auth, bookings, CRM, dashboard, invoices, onboarding, and more |
| `server_code/` | Server modules mirroring the client structure — includes `server_shared/` (vault, encryption, metrics services) |
| `docs/` | Project documentation |
| `tests/` | Test suite |
| `theme/` | Theme assets |

## Artifact Governance

- Planning documents, specs, ADRs, wireframes — read from
  `mb-3-cs-project-library`, never authored here.
- PDLF records — the ledger row, the Step Receipt and the step's outputs
  in `mb-3-cs-project-library/pdlf-outputs/{step}/`. No other report or
  log is kept.

## Source of Truth

The project-library is the upstream planning authority for this repo.
This repo implements what project-library specifies; it does not
originate architectural decisions.

## Access Model

- GBrain holds documentation only, never code. This business's sources
  are `mb-3-cs-project-library` and `mb-3-cs-project-context` (read only);
  the standards are in `default` and PDLF in `pdlf`.
- Graphify gives this repo's code graph, built from its code files only.
  Forms, tables and services are read directly from `anvil.yaml` and the
  form files.

## Task Completion

A PDLF step ends with its Step Receipt and stops for David. David runs
`/mb-close-out` and commits; the agent never commits or pushes.

## Timestamp Standard

Every date or timestamp generated for a build artefact — front matter,
register entries, logs, or any other system-internal record — must
follow the format and conversion method defined in the
`adr-timezone-utc-storage-display-conversion` ADR. Read that document
before generating any such timestamp. If anything about the required
method is unclear, stop and ask the developer.

## Environment

- Web UI only: `opencode web` from WSL. No Desktop app, no Desktop
  bridge.
- WSL paths: `/mnt/c/dev/dev-mb-3-cs/mb-3-cs-app1/` (this app),
  `/mnt/c/dev/dev-mb-3-cs/mb-3-cs-project-library/` (documentation),
  `/mnt/c/dev/dev-mb-3-cs/mb-3-cs-project-context/` (context, read only).

<!-- BEGIN GRAPH MEMORY GUIDANCE -->
## Graph Memory Guidance

Two graph/memory tools are available; they answer different questions and
are never a substitute for the source itself.

- **Graphify** (local code-relationship graph, `graphify-out/graph.json`) is
  the authority for **current structural code relationships** — definitions,
  callers/callees, imports, containment — as the code exists now.
- **GBrain** (semantic memory, source `mb-3-cs-project-library`) is the authority for
  **decisions, rationale, history, research, and incidents** — why something
  was done, what was tried, what was decided.

Authority order:
1. **Current repository files, explicit user instructions, and tests** are
   authoritative over everything else.
2. **Graphify INFERRED or AMBIGUOUS edges must be verified against source**
   before being trusted; only EXTRACTED edges are reliable without re-check.
3. **Graph provenance must match the current Git commit.** If `graphify-out/`
   was generated from a commit other than HEAD, rebuild before relying on it.
4. **Important completed decisions may be written back to GBrain** so future
   sessions recover the rationale, not just the code.
5. **Neither graph replaces direct source inspection or testing.** Confirm any
   structural or historical claim in the source files before acting on it.
<!-- END GRAPH MEMORY GUIDANCE -->
