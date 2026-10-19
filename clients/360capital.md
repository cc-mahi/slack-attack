---
slug: 360capital
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/360capital.yaml   # hosts, athena db, s3 bucket
  billing: null                                              # no entry in ../MahiProduct/data/billing/clients.json
  hosts: null                                                # no entry in ../MahiProduct/data/client-hosts.json
  wiki: null                                                 # no ../MahiProduct/wiki/clients/360capital.md
channels: {}                      # analytics-only; no internal-/mahi-360capital channels exist, signal is cross-channel only
contacts: []
last_catchup: 2026-10-19T07:10:17Z
status: active
---

## Now
Live, analytics-only client with no dedicated Slack channels; Slack signal is incidental and cross-channel (#internal-trading-analytics, #internal-ai-reports, #sales). Quiet: no client-facing comms and no incidents in the 2026-08-17..2026-10-15 window.

## Streams

### network-checks — Appears in network-wide cross-client checks
status: watching · since: 2026-10-14 · last: 2026-10-14
State: In Will Carter's cross-network check of the CMC SPX/NDX freeze around US CPI (2026-10-14), 360 Capital had no SPX/NDX fills in the window, so it was unaffected. Only Rostro dealt at the stale price.
Refs: https://mahifx.slack.com/archives/C03388U1YG4/p1791987866639159

### s3-tiering — Parquet store on OneZone-IA tiering
status: watching · since: 2026-09-09 · last: 2026-09-09
State: Sam Hewitt's August AWS cost review lists 360capital as one of the accounts already using OneZone-IA for the parquet store; the proposed fleet-wide Glacier Instant Retrieval move extends that practice. Open question there is retrieval frequency on historical parquet partitions, owned by the backtest read-path owner.
Refs: https://mahifx.slack.com/archives/C0B5MLCEQQJ/p1788950326136349

## Arc
- 2024-12 — "360Capital Trades" stream appears in MQ-bridge reconnect data.
- 2025-10-22 — Bonnie Cassidy corrected a sales-sheet entry: 360 Capital did go live (analytics-only), not dropped off before go-live. https://mahifx.slack.com/archives/C8YMBES8N/p1761133493462989
