# mb-3-cs — explainer

## What it is

mb-3-cs is Mybizz Consulting Services: a multi-vertical consulting platform built
on Anvil.works (Material 3 theme, M3 dependency, MUI overlay). It manages the
practice's clients, contacts, bookings, services, invoices, email campaigns, blog
posts, landing pages, segments, tasks and time entries.

## What it can do

Run the consulting practice end to end: capture and segment contacts, take
bookings against service offerings, invoice for rendered services, market through
email campaigns and landing pages, publish a blog, and track tasks and time. One
codebase releases outward: App 1 is developed here, its tagged releases become
the master template (App 2), and the blank client template (App 3) is cloned for
each new client instance (App 4, on the client's own Anvil account).

## Suitability

Built for Mybizz's own consulting practice and its clients. Good for practices
that want one platform covering CRM, bookings, billing and marketing. Not a
generic multi-tenant SaaS: the architecture is dependency-based, so each client
instance is a clone of the blank template rather than a tenant of one database.

## Why it works this way

- **Anvil.works with Material 3 + MUI overlay** — one full-stack Python platform
  with a strict, token-driven design system; no hardcoded colors anywhere.
- **Dependency-based, not multi-tenant** — a client gets its own app clone, which
  keeps client data isolated by construction instead of by row-level rules.
- **Template cascade (App 1 → App 2 → App 3 → App 4)** — improvements made once in
  the development workspace flow to every client through releases, never by
  editing client apps directly.
- **Brevo for email** — one integration for campaign delivery, replacing Zoho.
- **A single contacts table** — leads, clients and other relationships are one
  record type with status, not separate tables.

## What has to happen

David directs and approves; the Plan agent reads and plans and never writes; the
Build agent writes only inside the app it is building. Releases flow App 1 to
App 2 through the PDLF pipeline; client instances come from App 3 clones. The
project context (`mb-3-cs-project-context`) and the project library stay current,
because every session inherits them.
