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
last_catchup: 2026-10-30T07:23:17Z
status: active
---

## Now
Prospect, contract unsigned. Switch had cold feet on 2026-10-26 over skew/FI numbers; on 2026-10-28 Will concluded their ~$2/M gold figure is almost certainly an MT5 server-time clock error and the corrected XAUUSD skew is $9.89/M. Nothing goes to Switch until Mahi confirms whether an MNDA exists directly with Switch; Bonnie sent an MNDA to Sammy on 2026-10-29 for review.

## Streams

### mnda-ip-coverage — No NDA with Switch covering sims and mechanism
status: open · since: 2026-10-26 · last: 2026-10-29
State: Andrew found the Introducer Agreement binds the introducer, not the prospect, and "confidential information" is undefined, so nothing stops Switch rebuilding its own skew. Bonnie confirmed on 2026-10-28 there is no MNDA in place and offered to send one (customer is Mahi's, not the IB's), and is getting legal opinion too. On 2026-10-29 she sent Sammy an MNDA for Switch to review, with details guessed from Switch's website as Sammy did not reply. Will thinks an NDA is needed directly with Switch even via the IB, and is waiting on Andrew's counter work before going back to Switch. Mahi has no NDA with FinPrime either.
Next: Switch/Sammy to review and return the MNDA (party details unconfirmed); Andrew's counter work; Protected IP to be named as a class in future agreements.
Refs: https://mahifx.slack.com/archives/C0C7QB281J6/p1793042795810709 https://mahifx.slack.com/archives/C0C7QB281J6/p1793203037567439 https://mahifx.slack.com/archives/C0C7QB281J6/p1793284717969209

### sva-credibility — Switch doubts FI numbers; UTC-corrected XAUUSD SVA rerun
status: open · since: 2026-10-26 · last: 2026-10-28
State: Switch's own backtest gave about $2/M and a 52% hit rate on gold. Will's review (2026-10-28) says their trade file is in MT5 server time (UTC+3 summer, +2 winter), so reading it as UTC compares fills with prices 2-3h away. All 13 monthly XAUUSD SVA runs on UTC-corrected input are done: gold skew $9.89/M, positive in all 13 months (lowest $7.61/M); the July runs said ~$4.1/M and were likely under-sold; whole-book case $5.3m-6.1m over 13 months against $15k/month fixed; non-gold $1.25m is from the July runs and likely understated. A control run (same engine, 3 months, timestamps read as UTC) was due ~20:00 UTC to confirm it lands near $2/M. Proposed response once MNDA is settled: send the UTC-converted file so Switch can rerun, offer a fill-by-fill session, keep proof-before-payment in the integration month. Cameron Hughes saved raw SVA/SI data to Drive and wants to see what Sammy showed commercially.
Next: Will to read control-run result; Mahi to own the $4.1 to $9.9/M change; response to Switch held until MNDA question resolved; Will to retrieve what Sammy showed commercially.
Refs: https://mahifx.slack.com/archives/C0C7QB281J6/p1793039397274569 https://mahifx.slack.com/archives/C0C7QB281J6/p1793193969380179 https://mahifx.slack.com/archives/C0C7QB281J6/p1793201070227169

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
- 2026-10-28 — Rerun shows gold skew $9.89/M; Switch's $2/M traced to MT5 server-time offset; MNDA gap being closed
- 2026-10-29 — MNDA sent to Switch for review
