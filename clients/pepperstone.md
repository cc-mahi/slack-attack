---
slug: pepperstone
refs:
  vibepulse: [../VibePulse/.claude/clients/pepperstone.yaml, ../VibePulse/.claude/clients/pepperstone-crypto.yaml]
  billing: ../MahiProduct/data/billing/clients.json     # entry: pepperstone
  hosts: ../MahiProduct/data/client-hosts.json          # entries: pepperstone, pepperstone-cfd, pepperstone-crypto
  wiki: null                                             # ../MahiProduct/wiki/clients/pepperstone.md (not yet)
channels_override: null
key_people_overrides:
  - {name: "Stephen Hendrie", role: "exchange/product"}
  - {name: "Marianna", role: "trading ops", confidence: low}
  - {name: "Reece", role: "ops / counterparty admin", confidence: low}
last_catchup: 2026-04-24T11:00:00Z
---

## Recent issues

> [open] 2026-04-24 — YTD list of counterparties removed from `reference.lists.counterparty.custom`
> Reece asked for a full YTD removal list beyond what Audit History surfaces; Kate investigating. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1777024868051039)

> [open] 2026-04-23 — Cpty 2075077 not routed to Dynamic Arbitrageurs as expected
> Client expected `B-RETAIL/Dynamic Arbitrageurs` routing based on markouts + classification config, but wasn't. Discussion in thread; unresolved as of 04-23 15:29. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1776942671186329)

> [open] 2026-04-22 — Inventory XAG Tapaas A/B reporting — tag 1 prefix solution
> Hedger fills currently come down the Mahi_A OZ takers, breaking Tapaas A/B split. Will proposed splitting tag 1 per order source (keep `MahiFX` for A-book, `B-MahiFX` or agreed prefix for inventory hedger). No code change needed. Awaiting Marianna/Tapaas prefix confirmation. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1776849698434619)

> [open] 2026-04-21 — tXAUUSD post-normalisation-persistence review
> Weekend review: XAUT mids cluster better than PaxG (Wintermute drifts from B2C2/HRP). Isaac proposes dual-rate model — a 24/7 normalised rate (all XAUT+PAXG sources, single basis) included in tXAUUSD mid-formation during the week, with Primary tracking B2C2+HRP PAXG blend for XAU-close→XAU-open tracking. Beta prices ~10s above gold open at 7s into open, resolves quickly. Supersedes prior `[open] 2026-04-17` tXAUUSD entry. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1776743136995659)

> [open] 2026-04-14 — XAGUSD allocation blocked by minimum-lag qty mismatch
> dynamicOrderSpeeds config has XAGUSD minimum-lag normal-qty 0.5 vs normal-qty 5000, producing a 2500 minimum that blocks allocation. Thread active.

> [open] 2026-04-01 — Proposal: move crypto maintenance/reboots to weekdays
> Weekend volumes ≥ weekday; weekend reboots left traders off-state. Awaiting Liam + Pepper confirmation.

> [resolved] 2026-04-13 — Sebastian Andrews Compass access revoked (compromised device)
> Suspended same day by Rory King.

> [resolved] 2026-04-13 — Arb/XAUUSD crash ~11:02 UTC (PagerDuty Q1MAQYLK2ESYP8)

> [watching] 2026-04-10 — USDILS toxic flow (acct 51331195), NY first-hour pattern (cf. prior NZD/CHF)

> [resolved] 2026-03-24 — XAUUSD non-execution 11:00–11:02 UTC
> LP pricing flapping through sanity checks; Mahi pricing indicative during the period.

## Notable topics

- 2026-04-22 — XRPAUD live on Pepperstone Crypto Exchange. [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1776826778419749)
- 2026-04-23 — CFD NY IPs posted (trading-1 `192.81.111.207`, admin `192.81.111.240`); Nathan chasing LP handover ETA with Gordon/Martyna. Hardware updates done over weekend, handover imminent per Gordon. [permalink](https://mahifx.slack.com/archives/C06AR8MT8NT/p1776904666370719)
- 2026-04-21 — Argamon want Tokyo JPY crypto crosses too (Lee bumping existing request). [permalink](https://mahifx.slack.com/archives/C033K2P0RPT/p1776735210458109)
- Pepperstone CFD rollout — new desk being stood up. LDN servers in Mahi setup (IPs exchanged 2026-04-08/15). NY IPs now shared (see above). Hedgers for inventory-risk model; awaiting LP connection data + instrument specs from Pepper AU team.
- Pepperstone Crypto Exchange (pcrypto.com) — soft-launched 2026-03-Q1; rolling BNB/TRX/XRP-AUD on the exchange side. See Guru card T8xkG7nc.
