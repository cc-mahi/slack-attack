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
last_catchup: 2026-10-16T07:06:26Z
status: active
---

## Now
Prospect, contract not yet signed (as of 2026-10-08); integration discussions just started. Switch (parent Think Huge) would host its own Compass instance on non-Beeks infrastructure, so hosting terms are the live topic.

## Streams

### hosting-non-beeks — Switch self-hosting Compass outside Beeks
status: open · since: 2026-10-08 · last: 2026-10-09
State: Switch/Think Huge want to host Compass on Think Huge infra rather than Beeks. Liam offered it as possible but costed: one-off $2,000 per hosting provider plus $500 per server per month, x-connect to Beeks still needed for central market data and signals, UDP multicast, jumbo frames and private connectivity required. Standard Beeks setup for scope (1 admin, 2 trading) is about GBP 4,242 pm, billed separately. Think Huge asked whether Intel is mandatory (Liam: not mandatory, but low-latency tuning is Intel-specific and would need rework on AMD) and which DC Mahi uses with Beeks (LD4/LD5, NY4, TY3; would co-locate near the client's bridge provider).
Next: Think Huge to respond on hosting option and DC; Mahi awaiting their choice.
Refs: https://mahifx.slack.com/archives/C0C7N7CGC7Q/p1791459538072239 https://mahifx.slack.com/archives/C0C7N7CGC7Q/p1791535547310089

### contract-proposal — Proposal and contract pending
status: open · since: 2026-10-08 · last: 2026-10-15
State: Proposal is with Sammy; contract unsigned. Sammy was off this week (family bereavement) but on 2026-10-15 said Switch will 100% be a Mahi customer (relayed by Will). Switch is evaluating Mahi as risk/bridge provider. Sammy asked Kate for an autoclassifier screenshot to present to Switch on Tuesday (Compass vs OneZero); Kate was wary given recent issues, Will agreed to use an anonymised demo screen and Andrew is preparing an IB-safe login.
Next: Mahi to supply anonymised demo screen/login before Switch's presentation.
Refs: https://mahifx.slack.com/archives/C0C7QB281J6/p1791454134051789 https://mahifx.slack.com/archives/C0C7QB281J6/p1791465957208229 https://mahifx.slack.com/archives/C0C7QB281J6/p1792078628175019

## Arc
- 2026-10-08 — Switch channels created; Mahi/Think Huge hosting call opened
