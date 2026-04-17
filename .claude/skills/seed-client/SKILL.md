---
name: seed-client
description: Create a client dossier in clients/<slug>.md from VibePulse + MahiProduct data. Use when the user says "/seed-client <slug>" or asks to add a new client to the reference.
---

Build `clients/<slug>.md` by merging what exists in sibling repos. Do not pull Slack — `/catchup` does that.

## Inputs (check all four, not all will have entries)

1. `../VibePulse/.claude/clients/<slug>.yaml` — `regions`, `slack.internal`, `slack.client`, `athena_dbs`, `aws_profile`, `notes`.
2. `../MahiProduct/data/billing/clients.json` — find `slug` match. Pulls `name`, `athenaDb`, fee structure, `billingClarification`, hosting/contract clarifications.
3. `../MahiProduct/data/client-hosts.json` — `environments` with `graphiteHost`/`graphiteRegion`.
4. `../pagerbuddy/.claude/docs/slack-channels.md` — confirms `internal-*` / `mahi-*` channel names, especially for clients with non-standard suffixes.

The slug may not match across all four — try the obvious candidates (hyphen vs underscore, with/without vendor suffix) and report if a source has nothing.

## Merging VibePulse variants

VibePulse often splits one commercial client into multiple entries for infra reasons (e.g. `pepperstone` and `pepperstone-crypto`). If sibling entries share the same `slack.internal` and `slack.client` channels, they are one client from slack-attack's perspective — merge them into a single dossier:

- Use the parent slug (the shorter one, typically).
- Union `products`, `regions`, `athena_dbs` in frontmatter.
- Under Technical notes, keep a subsection per variant so the per-desk infra (hosts, DCs, workgroups, LP FIX connections, order-table quirks) stays addressable.
- Tell me which VibePulse entries you merged so I can sanity-check.

## Output

Copy `clients/_template.md` → `clients/<slug>.md` and fill frontmatter from the sources. Body sections:

- **Summary**: one paragraph derived from contract/fee notes + product clues. If nothing substantive is known, leave a single line placeholder (don't invent).
- **Technical notes**: copy anything non-obvious from VibePulse `notes` or MahiProduct billing clarifications. Infra quirks, ring-fenced accounts, Athena weirdness — these are the kinds of things worth capturing. When variants were merged, use a subsection per variant.
- **Recent issues / Notable topics**: leave empty — `/catchup` populates these.

For frontmatter:
- `products`: asset classes the client trades (fx, crypto, cfd, equities), not Mahi services.
- `contract_expires`: extract from billing notes if a term end date is mentioned (e.g. "3yr terms" + signing date → compute). Leave null if not derivable with confidence.

## Rules

- Never invent a field. If the source is silent, leave the frontmatter value empty/null.
- If `clients/<slug>.md` already exists, do not overwrite. Instead, show me what's changed between the sources and the existing dossier and let me merge.
- Leave `last_catchup: null` — seeding does not count as a catch-up.
- At the end, summarize what you filled in and what you left blank so I can judge whether to enrich manually.
