---
name: seed-client
description: Create a minimal client dossier in clients/<slug>.md pointing at VibePulse + MahiProduct as source of truth. Use when the user says "/seed-client <slug>" or asks to add a client without pulling Slack yet.
---

Most of the time you don't need this — `/catchup <slug>` auto-bootstraps a missing dossier before digesting. Use `/seed-client` only when Cameron wants to pre-create the file without running a catch-up.

## Steps

1. Verify `clients/<slug>.md` doesn't already exist (abort if it does — suggest `/catchup <slug>` to refresh instead).
2. Confirm the slug resolves somewhere:
   - `../VibePulse/.claude/clients/<slug>.yaml`, or common variants (hyphen/underscore, with/without `-crypto`/`-cfd`).
   - `../MahiProduct/data/billing/clients.json` entry for the slug.
   - If neither has the slug, report unknown and stop.
3. Copy `clients/_template.md` → `clients/<slug>.md` and fill `refs:`:
   - `vibepulse`: one yaml path, or a list if sibling yamls share the same slack channels (e.g. `pepperstone` + `pepperstone-crypto`).
   - `billing`: `../MahiProduct/data/billing/clients.json` with an inline comment naming the entry slug.
   - `hosts`: `../MahiProduct/data/client-hosts.json` with the entry slug(s).
   - `wiki`: `../MahiProduct/wiki/clients/<slug>.md` if that file exists, else `null`.
4. Leave `channels_override: null`, `key_people_overrides: []`, `last_catchup: null`.
5. Leave `Recent issues` and `Notable topics` sections empty — `/catchup` populates those.
6. **Status section:** if `wiki:` resolves to an existing file (MahiProduct has it), delete the `## Status` section entirely — the wiki is canonical. If `wiki: null`, keep the section's bullet skeleton (`Stage:` / `Integration:` / `Relationship:`) with placeholder values for `/catchup` (or Cameron) to fill.
7. Report what you filled in and what you left `null` / empty.

## Rules

- Don't restate anything that lives in the upstream refs — the whole point of this schema is that the dossier is a pointer + Slack-derived state, nothing more.
- `last_catchup: null` after seeding — seeding isn't a catch-up.
- Don't write into `../VibePulse/` or `../MahiProduct/` under any circumstances.
