---
slug: alphacapital
aliases: [alpha-capital]
refs:
  vibepulse: ../VibePulse/.claude/clients/alphacapital.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: ../MahiProduct/wiki/clients/alpha-capital-group.md
channels:
  internal-alphacapitalgroup: C06UHTDQ8JF
  mahi-alphacapitalgroup: C070016ND6X
contacts:
  - {name: "Gerard McConnell", role: "Alpha Capital, routing / platform / prop-product contact", confidence: low}
  - {name: "Jade", role: "Alpha Capital (last name and role unknown; raised statement of account request 2026-05-22)", confidence: low}
last_catchup: 2026-10-22T07:21:31Z
status: active
---

## Now
Prop client mid-build: Alpha is moving to its own broker and Alpha Trader on a DX Trade backend, so routing and platform-scope asks are arriving via Gerard McConnell.
Open this week: confirm Mahi routing for the new MT5 demo groups before Gerard goes live, and the TempDXPrices FIX bad-credential spam.
Billing: July cleared, August arrears still overdue, September bill due 20 Oct; Nicole Vivian wants payments before extending product offering.

## Streams

### pulse-dropcopy-stale — Pulse yield-profile stale alerts from dropped MT5 drop-copy session
status: open · since: 2026-10-16 · last: 2026-10-16
State: After the Beeks outage, Alpha's MT5 bridge drop-copy session (MahiFXMT5Bridge -> LIVE1Trades) into analyticsFixServerMT1 timed out at 09:13 UTC on 2026-10-16 and had not reconnected; no Alpha trades reached Pulse after 09:12 UTC and the backgroundJobs stale-yield-profile alert keeps firing. Liam Cordelle said a fix for the alert spam ships in 26.4. Reconnection not confirmed in window.
Next: Bridge session to be logged back on; alert fix in 26.4.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1792153713986749

### mt5-demo-routing — Routing needed for new Alpha MT5 demo groups
status: open · since: 2026-10-13 · last: 2026-10-13
State: Gerard McConnell updated feeds for new ACGd demo MT5 groups (Direct, Qualified High Risk, Swing High Risk, Alpha One routed to Mahi Grads MT5 ML / Alpha1 Q1 MT5 ML; Swing Pro/Raw EA to Mahi Q2 MT5 ML) and asked Mahi to confirm routing exists before he puts them live. Cameron Hughes said he will put it in config on Mahi's end. No confirmation visible.
Next: Cameron Hughes to apply config and confirm to Gerard.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1791894322304399

### tempdx-fix-logons — Prices->TempDXPrices FIX session spamming bad-credential logons
status: open · since: 2026-10-06 · last: 2026-10-06
State: Session Prices->TempDXPrices is repeatedly rejected on clientDistributionGateway2 (Invalid username and/or password), generating many alerts on Mahi's side. Cameron Hughes flagged it to Gerard; Arun said not urgent. No fix confirmed.
Next: Alpha to fix or remove the session credentials.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1791277536831499 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1791278615268349

### invoices-arrears — ACG Markets and ACG Broker invoices overdue
status: open · since: 2026-09-08 · last: 2026-10-06
State: Alpha futures business hit by Ninja Trader cancelling on a day's notice; challenge sales fell sharply and Alpha goes live with its own broker 21 Sept. George (Alpha) promised arrears cleared by end of September; as of 2026-10-06 Nicole Vivian confirmed 83k and 6k received clearing July, August still overdue, September bill not due until 20 Oct. Outstanding on 2026-10-05 was ACG Markets 249,815 and ACG Broker 19,632 before those payments. Nicole wants to see payments before extending product offering.
Next: Alpha to pay August; September invoice due 2026-10-20.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1788856330954559 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1790720761202929 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1791318273980089

### dx-platform-scope — Alpha Trader / DX Trade platform scope; direct bridge routing off T4B
status: open · since: 2026-08-26 · last: 2026-09-28
State: Gerard says Alpha Trader (own platform) is being built, temporarily 3-6 months on a DX Trade backend; Mahi has no direct DX Trade connection yet. Long-term goal is MT5 native, cTrader, Alpha Trader, probably DX Trade. Gerard (2026-09-16) said routing and stop-out rules for new plans need access via the Mahi bridge, not T4B; flow is currently via T4B while Alpha builds its draw-down engine and Mahi's build-out estimate is long. Nathan Burch logged the DX Trade platform-scope question as open on the MahiProduct wiki.
Next: Mahi to answer what the Compass document covers (DX/cTrader direct, own-platform integration); Cameron Hughes started with DXtrade and cTrader bridge docs.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1787749386714689 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1790264746444999 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1790579145063059

### arb-classification — Arbitrageur detection lag and classifier changes
status: watching · since: 2026-05-05 · last: 2026-09-17
State: 2026-05 skew health check found arbitrageur detection lag costing ~35K/week on XAGUSD; continuity-pool fills on arb-classified flow do not apply last look, and Q1-Arbitrageurs profile uses forced internalisation. Arbs are whitelisted manually when auto-detection misses (riskPath reference market changed BLACKWELL to VELOCITY 2026-06-22; CP 5103699 whitelisted 2026-08-19). Liam Cordelle switched the classifier to run against Pulse 2026-09-16, reverted by Daria Horton after PagerDuty alerts, then re-enabled after a Netty fix. Full report in docs/skew-health/alphacapital/2026-05-05-skew-health.md.
Next: none open; watch for further detection lag.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778009823301759 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1789656162589149

### price-spikes — Spikes from bad Velocity ticks and skew over-amplification
status: watching · since: 2026-05-05 · last: 2026-09-15
State: Recurring spikes traced to bad Velocity ticks (BMSL blowouts 2026-05-04; GBPUSD 2026-05-27 via crossed ticks corrupting TOBPN and 100% benchmark skew; GBPNZD 2026-08-31). Responses: MAHI_BENCHMARK_LDN added to continuity pool for NDXUSD/DOWUSD 2026-09-15, 10 pip ceiling cap added to the global override 2026-09-01. Nathan Burch's proposal to cut max skew from 10,000 to 2 pips (2026-05-28) was never confirmed as actioned.
Next: confirm whether the max skew reduction was applied.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1777994333748779 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1779945147921969 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1789460982893339

### xag-fi-pnl — XAGUSD and FI PnL leakage; FI PnL methodology question
status: watching · since: 2026-04-23 · last: 2026-08-25
State: XAG FI PnL bled repeatedly (April, June, August), with signal moved neuron to synapse (2026-04-23), skew floor lowered to 1 pip (2026-07-07), and XAG switched to price + IFMS signals (2026-08-13); by 2026-08-25 FI turned around on all books. Shyam Hari also flagged (2026-06-25, EURGBP false FI drop from news last-look delay) that prices used for FI PnL calculations may need review; no action seen.
Next: none; FI PnL price-source review unowned.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1776939603625359 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782445628932189 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1787672825872419

### weekend-trading — Alpha prop asks about 24/7 weekend trading
status: watching · since: 2026-09-14 · last: 2026-09-14
State: Gerard asked about weekend trading on XAU, XAG, WTI, SPX, NDX with reduced leverage and smaller contracts. Andrew Morgan called it the first prop-side ask; plan is explanatory material without commercials. No activity since; reduced to watching.
Next: Cameron Hughes to send the bespoke draft after review.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1789378377294579 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1789396646430429

### fastmt-requests — FastMT (David Rapp) feature and access requests
status: watching · since: 2026-07-02 · last: 2026-08-26
State: Restricted Compass Bridge Operator role provisioned on alphacap-broker for FastMT 2026-07-02, with a standard Compass account to follow. On 2026-08-26 David asked for an MT5 plugin to auto-stop out at an equity threshold then set accounts read-only; not available, a few months out. He also sources from T4B and wants ongoing feature updates and regular flow catch-up calls.
Next: Mahi to schedule flow catch-up calls and share feature updates.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782978915962429 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1787760873528779

### oils-off — Oils instruments turned off
status: closed · since: 2026-06-24 · last: 2026-08-14 · closed: 2026-10-15
State: Cameron Hughes turned oils off due to arbed price spikes and very low volumes; CO1USD signal later switched to IFMS + price (2026-08-14), possibly ahead of re-enabling, not stated. No activity since 2026-08-14; assumed resolved.
Refs: https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782303349490299 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1786707493633689

### statement-of-account — Statement of account request from Jade
status: closed · since: 2026-05-22 · last: 2026-05-22 · closed: 2026-10-19
State: Jade asked who to contact for a statement of account. Shyam Hari took it internally; Bonnie Cassidy said she would follow up. No activity since 2026-05-22; assumed resolved.
Refs: https://mahifx.slack.com/archives/C070016ND6X/p1779427327328109 https://mahifx.slack.com/archives/C06UHTDQ8JF/p1779442392670229

## Arc
- 2026-06-07 — Compass upgraded to latest version over the weekend
- 2026-07-02 — Restricted Compass operator role created for FastMT
- 2026-08-02 — clientDistributionGateway3 removed (unused)
- 2026-09-08 — Invoice arrears escalated (ACG Markets, ACG Broker)
- 2026-09-21 — Alpha planned go-live with its own broker
