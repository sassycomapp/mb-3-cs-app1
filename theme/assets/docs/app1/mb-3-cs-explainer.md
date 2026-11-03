# mb-3-cs — explainer

## What it is

mb-3-cs is Mybizz Consulting Services: a complete, standalone online business
platform for consulting businesses and service businesses, delivered as a
subscription SaaS product. Every client receives their own fully operational,
isolated application instance. It is built on Anvil.works (Material 3 theme, M3
dependency, MUI overlay).

## What it can do

Give a client business one platform for its whole online operation: a public
website with booking, ordering and lead capture; bookings, services, packages
and time tracking; invoicing and payments; CRM with a sales pipeline; a team
email inbox and email marketing; blog, landing pages and reviews; built-in
accounts; AI assistance and voice. One codebase releases outward: App 1 is
developed here, its tagged releases become the master template (App 2), and the
blank client template (App 3) is cloned for each new client instance (App 4, on
the client's own Anvil account).

## Suitability

Built for consulting businesses and service businesses as Mybizz's subscribing
clients. Good for businesses that want one platform covering CRM, bookings,
billing and marketing at one price with unlimited staff. Not a generic
multi-tenant SaaS: the architecture is dependency-based, so each client
instance is a clone of the blank template rather than a tenant of one database.

## Why it works this way

- **Anvil.works with Material 3 + MUI overlay** — one full-stack Python platform
  with a strict, token-driven design system; no hardcoded colors anywhere.
- **Dependency-based, not multi-tenant** — a client gets its own app clone, which
  keeps client data isolated by construction instead of by row-level rules.
- **Template cascade (App 1 → App 2 → App 3 → App 4)** — improvements made once in
  the development workspace flow to every client through releases, never by
  editing client apps directly.
- **Amazon SES for every email** — one SES tenant per client carries every email
  received and sent, and the CRM is built in (ADR `brevo-email-and-crm`; Brevo
  and Zoho are errors).
- **A single contacts table** — leads, clients and other relationships are one
  record type with status, not separate tables.

## What has to happen

David directs and approves; the Plan agent reads and plans and never writes; the
Build agent writes only inside the app it is building. Releases flow App 1 to
App 2 through the PDLF pipeline; client instances come from App 3 clones. The
project context (`mb-3-cs-project-context`) and the project library stay current,
because every session inherits them.
