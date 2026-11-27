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
last_catchup: 2026-11-27T08:16:42Z
status: active
---

## Now
Live Compass client (LDN + TKY, PXM books). Compass 26.3 to 26.4 upgrade went to the weekend restart of 10-10/11; completion not confirmed in Slack.
Kate Stagg is actively tuning skew config from the weekly skew-health runs. CFD billing credit ($25k) was agreed internally in Aug; issuance not confirmed.
Client channel was quiet until 11-26, when Axiory asked for XAUJPY to be added with skew; Kate accepted.

## Streams

### xaujpy-setup — XAUJPY instrument add with skew
status: open · since: 2026-11-26 · last: 2026-11-26
State: Pauline Cajkova (Purple Technology, on Axiory's side) said they are adding XAUJPY to their offering and asked Mahi to set it up and apply skew to the pricing. Kate Stagg agreed to set it up. No timeline or config details posted yet.
Next: Kate to configure XAUJPY and skew; confirm back to client.
Refs: https://mahifx.slack.com/archives/C06KHNQQYMR/p1795691597779439 https://mahifx.slack.com/archives/C06KHNQQYMR/p1795691626303149

### compass-26-4-upgrade — Compass 26.3 to 26.4 upgrade (LDN + TKY)
status: watching · since: 2026-10-08 · last: 2026-10-09
State: Downgraded to watching (no Slack activity for 38d; restart outcome never posted). Change CHG-2610-6A7S staged Fri 10-09, live at the weekend restart; approved at RC #7224. Axiory sets neither PSM adjustment-widening nor tightening parameters, so from restart prices widen/tighten by one increment on PSM-W/PSM-T signals in LDN and TKY; Liam decided to let that go on. Client was told 10-09 and is being monitored over the open. Infra main moved to LDN + TKY ahead of staging (CHG-2610-WP2T, self-approved).
Next: confirm the restart landed cleanly (nothing posted yet); close if still silent at 60d.
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1791483332472299 https://mahifx.slack.com/archives/C06KHNQQYMR/p1791543782667709

### infra-change-notices — Infra and network change windows affecting Axiory
status: watching · since: 2026-10-08 · last: 2026-10-14
State: Upcoming or recent imposed windows: PrimeXM LD4 cross-connect port upgrade 10-10 (brief BGP drops), Beeks cross-site link move 10-17 05:00-09:00Z (replication blips), AWS taking down LD_SEC 10-22 21:00-23:00Z (London Beeks clients). Informational; Kate is listed as the Axiory owner.
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1791494708657249 https://mahifx.slack.com/archives/C06KQT6EU3W/p1791998802022569

### skew-arb-tuning — Skew tuning and GBPAUD/arb handling
status: closed · since: 2026-05-22 · last: 2026-08-28 · closed: 2026-11-16
State: No activity since 2026-08-28; assumed resolved. Weekly skew-health runs (Kate, 08-28) found capture healthy (about $100k/wk TKY, $21k/wk LDN, mostly XAUUSD) and made config-only changes: flow-price-thresh published for five crosses on TKY (measurement only), a very small harmonics skew on GBPAUD TKY (LDN stays off after the Jan and May arbs; FI-drop alert is the tripwire), USDJPY/GBPJPY/XAGUSD signal swaps, dedicated graph threads for XAUUSD/USDJPY. AXIORY_MT5_LDN is now excluded via book scope (it double counted PXM trades). NDXUSD/G30EUR re-wire since 22 Jul is a net win (about $880/wk).
Refs: https://mahifx.slack.com/archives/C06KQT6EU3W/p1779469727749819 https://mahifx.slack.com/archives/C06KQT6EU3W/p1787914227833699

## Arc
- 2026-04-27 — LD4 pricing broke at open (LDN dist channel internalisation market overridden to CLIENT_PRICE_TKY via WAN replication, 04-20); restored, `_z` symbols back on MAHI pricing by 05-02
- 2026-05-22 — GBPAUD arb (acct 2040811) on LDN; skew turned off on GBPAUD everywhere, arb detection deployed to riskPath 05-26
- 2026-06-26 — Jan's XAUUSD demo-server price query; Mahi found no drop copies (demo execution is Axiory-side), supplied pricing CSV
- 2026-07-15 — XAUUSD slippage complaint (acct 2045069) traced to PXM side; client confirmed resolved
- 2026-07-22 — CFD billing over-charge found; corrected volumes and $25k credit agreed by 08-03
- 2026-08-28 — Kate's skew-health changes on TKY and LDN
- 2026-10-09 — Compass 26.4 approved for the weekend restart
