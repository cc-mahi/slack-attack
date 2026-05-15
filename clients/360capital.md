---
slug: 360capital
refs:
  vibepulse: ../VibePulse/.claude/clients/360capital.yaml   # AWS eu-west-2 trading host, athena db 360capital_ldn, s3 360capital-parquet-store
  billing: null                                              # no entry in ../MahiProduct/data/billing/clients.json
  hosts: null                                                # no entry in ../MahiProduct/data/client-hosts.json or infra-hosts.json
  wiki: null                                                 # no ../MahiProduct/wiki/clients/360capital.md
channels_override: null                                      # no internal-360capital / mahi-360capital — analytics-only relationship
key_people_overrides: []
last_catchup: 2026-05-15T07:07:44Z
---

## Status

- **Stage:** live (analytics-only) — Bonnie corrected a sales-sheet edit on 2025-10-22 confirming 360 Capital "did go live", contrary to a sheet entry that had marked them as "dropped off just before going live". https://mahifx.slack.com/archives/C8YMBES8N/p1761133493462989
- **Integration:** analytics / parquet-store ingestion only. AWS eu-west-2 trading host (per VibePulse `360capital.yaml`), `360capital_ldn` athena db, `s3://360capital-parquet-store/`, "360Capital Trades" stream named in MQ-bridge reconnect data dec-2024. No dedicated Slack channel pair (`internal-360capital` / `mahi-360capital` do not exist).
- **Relationship:** quiet. Sales-side state owned by Bonnie Cassidy / Nicola Perikhanyan; no client-facing comms surfaced in 90d. Recent activity is internal data-import work only.

## Recent issues

> [open] 2026-04-22 — 360capital data re-import
> Hussain Bani standup: "Imported 360capital" alongside 5ers and pepperstone CFD bootstrap work. Suggests parquet-store / analytics data refresh; no thread, no follow-up signal in the slack-attack window. Earliest signal in this window — older context not searched. https://mahifx.slack.com/archives/C025QLNQ3AR/p1776888433004469

> [watching] 2025-10-22 — sales-sheet status conflict
> Bonnie flagged that someone overwrote 360 Capital's sales-sheet entry to say they "dropped off just before going live"; she reverted it because they did in fact go live. Nicola confirmed she hadn't touched 360 — origin of the bad edit unidentified. Worth keeping eyes on if status is queried again. https://mahifx.slack.com/archives/C8YMBES8N/p1761133493462989

## Notable topics

- Analytics-only client with no internal/client Slack channel pair — catchup signal will always be cross-channel (`#sales`, `#dev-status`, `#internal-trading-analytics`, `#dev-mq-bridge`). No `slack:` block in VibePulse `360capital.yaml`.
