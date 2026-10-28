---
slug: switch
aliases: [switch-markets]
refs:
  vibepulse: null          # no ../VibePulse/.claude/clients/switch.yaml; prospect, pre-contract
  billing: null            # not in ../MahiProduct/data/billing/clients.json
  hosts: null
  wiki: null
channels:
  internal-switch: C0C7QB281J6
  mahi-switch: C0C7N7CGC7Q
contacts:
  - {name: Sammy, role: "Switch/consultant (xrigroup) - lead contact; says Switch is a consulting client of his and a future Mahi client"}
  - {name: Dom Gilbert, role: "Think Huge (Switch parent) - COO/shareholder; drives hosting cost questions"}
  - {name: Paul Pintiliescu, role: "Think Huge - infrastructure/CTO-side; asks hardware questions"}
  - {name: Brandon, role: "Think Huge - infrastructure lead (US west coast)"}
last_catchup: 2026-10-28T07:17:57Z
status: active
---

## Now
Prospect, contract unsigned. On 2026-10-26 Sammy relayed that Switch has cold feet: they distrust the skew/FI numbers after an AI-assisted backtest of their own. Will is rerunning XAUUSD SVA on Switch's own file and will read out with Sammy once it lands. No NDA with Switch covers the sims shared so far.

## Streams

### sva-credibility — Switch doubts FI numbers; fresh XAUUSD SVA rerun
status: open · since: 2026-10-26 · last: 2026-10-27
State: Sammy said Switch don't believe the skew numbers and backtested it themselves with AI, getting about $2/M and a 52% hit rate on gold, which Sammy says cannot be true. Old echo links may have expired. Will launched 13 monthly XAUUSD SVA runs (Jun 2025 to Jun 2026, UTC-corrected timestamps) on Switch's own file; at 08:00 UTC on 2026-10-27 eight of 13 were done with none failed, four more due that morning and Jun 26 about 35% with ETA 2026-10-28 ~07:00 UTC. Andrew also has preliminary Switch results. Cameron Hughes saved the raw SVA and SI sim data to Google Drive and wants to see what Sammy showed Switch commercially, since his charts may not match the sim results. Will thinks Mahi should run comms with Switch directly from here.
Next: Will to read out the 12-month results (Jun 26 follows) and prep an internal summary once Luke is sorted; Will to read out to Sammy; Will to retrieve what Sammy showed commercially.
Refs: https://mahifx.slack.com/archives/C0C7QB281J6/p1793039397274569 https://mahifx.slack.com/archives/C0C7QB281J6/p1793091926112869

### mnda-ip-coverage — No NDA with Switch covering sims and mechanism
status: open · since: 2026-10-26 · last: 2026-10-26
State: Andrew checked the Introducer Agreement Master: it binds the introducer, not the prospect, and "confidential information" is undefined, so nothing stops Switch rebuilding its own skew. Mahi has no NDA with Switch (nor with FinPrime) and there is no central store of MNDAs. Switch is already widely connected to brokers, AI fluent and has built its own skew.
Next: Protected IP to be named as a class in future agreements; NDA before further sims or mechanism discussion (Andrew).
Refs: https://mahifx.slack.com/archives/C0C7QB281J6/p1793042795810709 https://mahifx.slack.com/archives/C0C7QB281J6/p1793043520163329

### contract-proposal — Proposal and contract pending
status: open · since: 2026-10-08 · last: 2026-10-22
State: Proposal is with Sammy; contract unsigned. Sammy was off this week (family bereavement) but on 2026-10-15 said Switch will 100% be a Mahi customer (relayed by Will). Switch is evaluating Mahi as risk/bridge provider. Sammy asked Kate for an autoclassifier screenshot to present to Switch on Tuesday (Compass vs OneZero); Kate was wary given recent issues, Will agreed to use an anonymised demo screen and Andrew is preparing an IB-safe login. On 2026-10-21 Will said Sammy has re-engaged and he is reviewing the latest commercials. On 2026-10-22 Sammy asked Will for the FI success rate on gold from Switch's data; Will said he would look.
Next: Will to review latest commercials and respond to Sammy; Will to pull FI success rate on gold for Sammy.
Refs: https://mahifx.slack.com/archives/C0C7QB281J6/p1791454134051789 https://mahifx.slack.com/archives/C0C7QB281J6/p1791465957208229 https://mahifx.slack.com/archives/C0C7QB281J6/p1792584843864439 https://mahifx.slack.com/archives/C0C7QB281J6/p1792663788281489

### hosting-non-beeks — Switch self-hosting Compass outside Beeks
status: open · since: 2026-10-08 · last: 2026-10-09
State: Switch/Think Huge want to host Compass on Think Huge infra rather than Beeks. Liam offered it as possible but costed: one-off $2,000 per hosting provider plus $500 per server per month, x-connect to Beeks still needed for central market data and signals, UDP multicast, jumbo frames and private connectivity required. Standard Beeks setup for scope (1 admin, 2 trading) is about GBP 4,242 pm, billed separately. Think Huge asked whether Intel is mandatory (Liam: not mandatory, but low-latency tuning is Intel-specific and would need rework on AMD) and which DC Mahi uses with Beeks (LD4/LD5, NY4, TY3; would co-locate near the client's bridge provider).
Next: Think Huge to respond on hosting option and DC; Mahi awaiting their choice.
Refs: https://mahifx.slack.com/archives/C0C7N7CGC7Q/p1791459538072239 https://mahifx.slack.com/archives/C0C7N7CGC7Q/p1791535547310089

## Arc
- 2026-10-08 — Switch channels created; Mahi/Think Huge hosting call opened
- 2026-10-26 — Switch got cold feet over skew/FI numbers; fresh XAUUSD SVA rerun started
