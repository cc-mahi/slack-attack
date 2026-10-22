---
slug: axiory
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/axiory.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: axiory
  hosts: ../MahiProduct/data/client-hosts.json          # entry: axiory
  wiki: ../MahiProduct/wiki/clients/axiory.md
channels:
  internal-axiory: C06KQT6EU3W
  mahi-axiory: C06KHNQQYMR
contacts:
  - {name: "Adam Foltyn", role: "client trading ops, LP/pricing escalations", confidence: low}
  - {name: "Roman", role: "Axiory main commercial/relationship contact (no surname confirmed)", confidence: low}
  - {name: "Magda", role: "Axiory, possibly attending Cyprus event alongside Roman", confidence: low}
  - {name: "Jan", role: "Axiory TY office, data/ops requests (surname unknown)", confidence: low}
last_catchup: 2026-10-22T07:21:31Z
status: active
---

## Now
Live Compass client (LDN + TKY, PXM books). Compass 26.3 to 26.4 upgrade went to the weekend restart of 10-10/11; completion not confirmed in Slack.
Kate Stagg is actively tuning skew config from the weekly skew-health runs. CFD billing credit ($25k) was agreed internally in Aug; issuance not confirmed.
Client channel has been quiet since July apart from the upgrade notice.

## Streams

### compass-26-4-upgrade — Compass 26.3 to 26.4 upgrade (LDN + TKY)
status: open · since: 2026-10-08 · last: 2026-10-09
State: Change CHG-2610-6A7S staged Fri 10-09, live at the weekend restart; approved at RC #7224. Axiory sets neither PSM adjustment-widening nor tightening parameters, so from restart prices widen/tighten by one increment on PSM-W/PSM-T signals in LDN and TKY; Liam decided to let that go on. Client was told 10-09 and is being monitored over the open. Infra main moved to LDN + TKY ahead of staging (CHG-2610-WP2T, self-approved).
Next: confirm the restart landed cleanly and watch pricing after the open (nothing posted yet).
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1791483332472299 https://mahifx.slack.com/archives/C06KHNQQYMR/p1791543782667709

### skew-arb-tuning — Skew tuning and GBPAUD/arb handling
status: open · since: 2026-05-22 · last: 2026-08-28
State: Weekly skew-health runs (Kate, 08-28) found capture healthy (about $100k/wk TKY, $21k/wk LDN, mostly XAUUSD) and made config-only changes: flow-price-thresh published for five crosses on TKY (measurement only), a very small harmonics skew on GBPAUD TKY (LDN stays off after the Jan and May arbs; FI-drop alert is the tripwire), USDJPY/GBPJPY/XAGUSD signal swaps, dedicated graph threads for XAUUSD/USDJPY. AXIORY_MT5_LDN is now excluded via book scope (it double counted PXM trades). NDXUSD/G30EUR re-wire since 22 Jul is a net win (about $880/wk).
Next: Kate reads USDJPY/GBPJPY LDN and flow-price-thresh potential at the 4 and 11 Sep runs; no later result seen in Slack.
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1779469727749819 https://mahifx.slack.com/archives/C06KQT6EU3W/p1787914227833699

### infra-change-notices — Infra and network change windows affecting Axiory
status: watching · since: 2026-10-08 · last: 2026-10-14
State: Upcoming or recent imposed windows: PrimeXM LD4 cross-connect port upgrade 10-10 (brief BGP drops), Beeks cross-site link move 10-17 05:00-09:00Z (replication blips), AWS taking down LD_SEC 10-22 21:00-23:00Z (London Beeks clients). Informational; Kate is listed as the Axiory owner.
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1791494708657249 https://mahifx.slack.com/archives/C06KQT6EU3W/p1791998802022569

### billing-cfd-tier — CFD tier billed on combined volume
status: watching · since: 2026-07-22 · last: 2026-08-03
State: Roman queried the June invoice (29.5B). Cause: CFD tier was billed off combined FX+metals+CFD volume from Feb onward at $10k, when true CFD-only volume (5 instruments, parties PXM_BROKERS/GU) is 3-4.6b and belongs on the $5k tier. Nicole Vivian confirmed 08-03 that earlier months were only ever $5k, so a $25k credit covers Feb-Jun. `/billing-prep` was corrected to filter parties and instruments.
Next: Nicole/Kate to apply the $25k credit and tell Roman; no confirmation seen in Slack.
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1784710795537379 https://mahifx.slack.com/archives/C06KQT6EU3W/p1785715856791519

### commercial-compass-psm — Compass routing, PSM interest, low-spreads campaign
status: watching · since: 2026-05-22 · last: 2026-05-22
State: From the 05-22 client call: Axiory's low-spreads campaign had no volume effect and will not repeat. Roman is interested in a PSM setup and still sees Compass routing as pipeline, blocked by the double-bubble cost (PXM plus Compass fees via XCore). Roman may attend the Cyprus event, possibly with Magda.
Next: Kate to check whether the PXM fee-reduction agreement resolves the double bubble, then follow up with Roman (no follow-up seen).
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1779449151258899

### gbpaud-spread-dispute — GBPAUD spread blowout root-cause dispute
status: closed · since: 2026-07-13 · last: 2026-07-16 · closed: 2026-10-15
State: No activity since 2026-07-16; assumed resolved. Kate traced the 07-13 spike to Axiory's own PXM aggregation failing over to a bad Finalto quote; Jan disputed the 26D dropout theory with raw ticks and sent a reminder 07-16 that went unanswered in the channel.
Refs: https://mahifx.slack.com/archives/C06KHNQQYMR/p1784017690112589 https://mahifx.slack.com/archives/C06KHNQQYMR/p1784177182713689

### fix-session-alerts — Expected FIX session alerts silenced
status: closed · since: 2026-09-04 · last: 2026-09-04 · closed: 2026-10-15
State: AXIORY_BROKER_CLIENTS-ORDER and AXIORY_A_BOOK-ORDER PagerDuty alerts were expected (placeholder credentials, A_BOOK channel idle 90 days; all flow via MT5 bridge, cTrader and PXM books). Sam Hewitt turned the alerts off.
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1788489379120969

## Arc
- 2026-04-27 — LD4 pricing broke at open (LDN dist channel internalisation market overridden to CLIENT_PRICE_TKY via WAN replication, 04-20); restored, `_z` symbols back on MAHI pricing by 05-02
- 2026-05-22 — GBPAUD arb (acct 2040811) on LDN; skew turned off on GBPAUD everywhere, arb detection deployed to riskPath 05-26
- 2026-06-26 — Jan's XAUUSD demo-server price query; Mahi found no drop copies (demo execution is Axiory-side), supplied pricing CSV
- 2026-07-15 — XAUUSD slippage complaint (acct 2045069) traced to PXM side; client confirmed resolved
- 2026-07-22 — CFD billing over-charge found; corrected volumes and $25k credit agreed by 08-03
- 2026-08-28 — Kate's skew-health changes on TKY and LDN
- 2026-10-09 — Compass 26.4 approved for the weekend restart
