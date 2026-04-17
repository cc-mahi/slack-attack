# slack-attack

Personal Slack catch-up workflow + rolling client reference.

Two purposes, one repo:

1. **Client dossiers** (`clients/<slug>.md`) — structured frontmatter + prose notes on each client: type (broker/prop), contract status, products, channels, key people, tech notes, recent issues, notable topics. This is my reference when someone says "what's the deal with $client".
2. **Daily catch-up** (`/catchup`) — pulls Slack activity since last catch-up for a client (or a cross-cutting channel, or everything), produces a digest, and proposes updates to the dossier so it stays current.

Cross-cutting channels (e.g. `#dev`, `#announcements`) live in `channels/<name>.md` with the same shape.

## Layout

```
clients/     per-client dossiers (_template.md is the schema)
channels/    per-channel dossiers for non-client channels
.claude/
  skills/
    catchup/       /catchup [target]
    seed-client/   /seed-client <slug>
  docs/
    slack-conventions.md   channel patterns + skip list
```

## Data sources (for seeding dossiers)

- `../VibePulse/.claude/clients/*.yaml` — regions, Slack channels, Athena DBs, AWS profiles
- `../MahiProduct/data/billing/clients.json` — authoritative active-client list, fees, hosting notes
- `../MahiProduct/data/client-hosts.json` — per-env Graphite hosts
- `../pagerbuddy/.claude/docs/slack-channels.md` — channel mapping + skip rules

The catch-up skill does not need these; they're inputs to `/seed-client` only.

## Setup

After cloning, wire up the commit-msg hook:

```
git config core.hooksPath .githooks
```

Enforces conventional commits (`feat|fix|docs|chore|refactor|test|ci|build|perf|style|revert`), 72-char subject, no trailing period.
