---
slug: toponetrader
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/toponetrader.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: toponetrader
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toponetrader
  wiki: ../MahiProduct/wiki/clients/toponetrader.md
channels:
  internal-toponetrader: C08TG143F4L
  mahi-toponetraders: C08U853T684
contacts:
  - {name: "Matt Morris", role: "CEO, Top One Trader"}
  - {name: "Lars Aerts", role: "Operations / integration lead at TOT"}
  - {name: "Shane Kalichurn", role: "TOT operations; payouts reporting, harsh-execution group requests"}
  - {name: "Daniel", role: "TOT trading/risk contact; raises slippage and fill queries in mahi-toponetraders"}
  - {name: "Priojit", role: "TOT hire working closer with Compass (Jan 2026)", confidence: low}
  - {name: "Todd Hodges", role: "TOT internal contact; Compass product training Jan 2026", confidence: low}
  - {name: "Arjie", role: "MatchTrader operations contact at TOT", confidence: low}
last_catchup: 2026-10-26T08:04:59Z
status: active
---

## Now
Prop firm; Mahi is dealing desk and risk. Focus is payout ratio: skew and LR tightened, harsher execution on 2-Step/1-Step groups, spreads restored on Prop Firm Match.
Open client query: CADCHF 4 ms-apart fills with 1.3 pip difference (Mahi to explain). New: drop-copy volume exceeds expected volume (checking with Shane).

## Streams

### prop-network-showcase — Mahi to show TOT its prop-network work
status: open · since: 2026-10-21 · last: 2026-10-21
State: The 2026-10-21 check-in call was cancelled by Shane (kept in the calendar if needed); Cameron Copland was on leave. Will Carter said Mahi will pull together what it is working on for its prop network and show TOT over the next week.
Next: Will Carter / Mahi to send the prop-network material to Shane within about a week.
Refs: https://mahifx.slack.com/archives/C08U853T684/p1792585285879989 https://mahifx.slack.com/archives/C08U853T684/p1792585333046689

### drop-copy-volume — Drop-copy volume exceeds expected volume
status: open · since: 2026-10-15 · last: 2026-10-15
State: Cameron Hughes saw drop copies carrying much more volume than expected. Shane (TOT) thinks the extra accounts are "competition" accounts not sent to Mahi, and is double-checking.
Next: Shane to confirm whether the excess is competition accounts.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1792053381996649 https://mahifx.slack.com/archives/C08TG143F4L/p1792053398775309

### cadchf-slippage — CADCHF second fill 1.3 pips above quoted ask
status: open · since: 2026-10-14 · last: 2026-10-14
State: Daniel forwarded TOT's analysis: two 3-lot buys at the same price, the second filled 4 ms after the first at 1.3 pips worse than Mahi's published ask. TOT wants Mahi to explain the fill. Shyam Hari acknowledged and said Mahi will check.
Next: Mahi (Shyam Hari) to investigate and revert to Daniel.
Refs: https://mahifx.slack.com/archives/C08U853T684/p1791943609687779 https://mahifx.slack.com/archives/C08U853T684/p1791943843239269

### payout-ratio-levers — Payout ratio, skew and spread levers
status: open · since: 2026-09-30 · last: 2026-09-30
State: Call with Matt and Shane on 2026-09-30: 2-Step Pro payout ratio was 47% over 6 weeks. Mahi is raising skew on 1-Step and 2-Step. EURUSD, USDJPY and GBPUSD spreads go back to 0.0 on Prop Firm Match after a ranking slide. Max loss 9% to 8% is the agreed fallback if skew and spreads are not enough. TOT's Launchpad experimental groups need the harsher execution rules, so Shane will flag each new group.
Next: Mahi watching results of skew and spreads; Shane to notify Mahi of each new Launchpad group.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1789027773632959 https://mahifx.slack.com/archives/C08TG143F4L/p1790787041722219

### lr-harsh-execution — LR retune and harsher execution for 2-Step
status: watching · since: 2026-08-25 · last: 2026-08-26
State: Shane asked (2026-08-25) for harsher execution on the second phase of the 2-Step plan and harsher still when funded. Cameron Hughes sent LR options and applied LR changes on 2026-08-26 (channel refill/caps and a global cap). Shane is looking for a way to identify 2-Step accounts on TOT's side.
Next: Shane to provide a way to distinguish 2-Step accounts.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1787643570858959 https://mahifx.slack.com/archives/C08TG143F4L/p1787750805616039

### prop-perps — Prop perps request
status: watching · since: 2026-09-30 · last: 2026-10-05
State: Matt asked about prop perps (Vest Markets, MyFundedPerps). Cameron Hughes sees it as a growing area and a possible new offering and will look at Vest. Logged on the wiki Client requests section.
Next: Cameron Hughes to look at Vest.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1790787110596799 https://mahifx.slack.com/archives/C08TG143F4L/p1791183636574369

### arb-pricing-tuning — Arb flagged by daily checks, pricing tweaks
status: watching · since: 2026-08-18 · last: 2026-08-24
State: GBPUSD arb alert on 2026-08-18 led to proportion and price-improvement reductions; on 2026-08-21 daily checks flagged more arb, so MAHI_LP5 was removed from signalReturn markets, GBPJPY added to the GBPUSD/USDJPY override and signal moved to synapse. By 2026-08-24 no more significant arb; being monitored.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1787044539658809 https://mahifx.slack.com/archives/C08TG143F4L/p1787572737892749

### ctrader-billing-check — cTrader shut off by TOT; billing model review
status: watching · since: 2026-08-26 · last: 2026-09-10
State: TOT stopped using cTrader (Shane: it was costing them heavily); config kept in case they return. On 2026-09-09/10 internal billing was queried against the revised per-user model and Will Carter noted the fixed component was missing for low totals; Cameron Hughes was asked to review accounts.
Next: Cameron Hughes to review accounts; internal billing to reconcile.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1787752907131709 https://mahifx.slack.com/archives/C08TG143F4L/p1789022593579519

### btcusd-100x-multiplier — MatchTrader BTCUSD order 100x oversized
status: closed · since: 2026-07-25 · last: 2026-07-29 · closed: 2026-10-22
State: A 1.2 lot BTCUSD order reached Mahi as 120 BTC. Broker Support found a session multiplier misconfigured at 100x on BTCUSD and asked TOT to set it to 0.01 and check other symbols. No confirmation seen, but no activity since 2026-07-29; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08U853T684/p1784987610439809 https://mahifx.slack.com/archives/C08VCTZ7ZN2/p1785304369359649

### mt5-bridge-drop — Brief MT5 bridge disconnect 2026-10-06
status: closed · since: 2026-10-06 · last: 2026-10-06 · closed: 2026-10-15
State: MT5 bridge dropped for about 30 s at 03:10 UTC, with PagerDuty disconnect and cancelled-order alerts. No follow-up; no client report. Assumed resolved.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1791257735457909

### compass-upgrade-sep — Compass upgrade maintenance window 2026-09-19
status: closed · since: 2026-09-18 · last: 2026-09-18 · closed: 2026-10-15
State: Maten Rehimi requested a 10:00-11:00 UK window on 2026-09-19 (about 20 min downtime expected). No client objection or completion message seen; assumed completed.
Refs: https://mahifx.slack.com/archives/C08U853T684/p1789735398809429

## Arc
- 2026-01 — Crypto symbols (34) enabled on MatchTrader alongside MT5
- 2026-03 — Brokerage expansion discussion: TOT wants a retail brokerage on its Comoros licence with an outsourced dealing desk
- 2026-07-18 — Compass upgrade completed
- 2026-08 — TOT shut off cTrader
- 2026-09-30 — Payout-ratio call with Matt and Shane; skew increase and spread restoration agreed
