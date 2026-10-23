---
slug: fintokei
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/fintokei.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: fintokei
  hosts: ../MahiProduct/data/client-hosts.json          # entry: fintokei
  wiki: ../MahiProduct/wiki/clients/fintokei.md
channels:
  internal-fintokei: C08R694QVNX
  mahi-fintokei: C08QWKFARDL
contacts:
  - {name: "Paulina Cajkova (Pau)", role: "Fintokei/Purple Technology ops; account requests, order queries"}
  - {name: "Jan Becan", role: "Fintokei/Purple Technology; MT4/MT5 server and bridge changes"}
  - {name: "Adam Foltyn", role: "Fintokei/Purple Technology; pricing and MT5 gateway issues"}
  - {name: "Lukas Sedlacek", role: "Fintokei/Purple Technology risk; suspicious-client reviews"}
  - {name: "Kristof Heger", role: "Fintokei/Purple Technology; order-fill queries"}
  - {name: "Roman Komurka", role: "Fintokei/Purple Technology; pricing/skew opinions", confidence: low}
last_catchup: 2026-10-23T07:18:25Z
status: active
---

## Now
LD-environment networking incident on 2026-10-16 (fleet-wide, hosting provider investigating) hit Fintokei connectivity; Liam reported signs of recovery at 10:46 UTC, no RCA or all-clear seen. Live on Compass 26.4 since the 2026-10-11 weekend restart. Mahi is fighting two pricing-skew problems: arbitrageurs exploiting skew flicker (GBPJPY, XBT) and XAU FI performance collapsing from 2026-10-12. Fintokei wants orders to survive LP feed gaps (TTL / last-price execution); Mahi is offering normalisation instead. New MT4 server clone (feeder and bridge copy) requested 2026-10-12.

## Streams

### xau-fi-skew-perf — XAU FI performance drop, skew rule changes
status: open · since: 2026-10-15 · last: 2026-10-15
State: Shyam flagged poor XAU FI this week; Kate found the price signal stopped performing from Monday 2026-10-12 (funded XAU skew ~$0.4/M vs $6.6/M the week before, both LS books negative). XAUUSD skew rule moved back to harmonics (as before 2026-10-06) and a new XAUUSD rule on the LSB model with a 5-pip ceiling (was 20). Backtests of price/harmonics/IFM/IFMS on main and LSB models are running.
Next: Kate to post backtest results in #internal-fintokei (this week's due 2026-10-15 afternoon, last week's evening).
Refs: https://mahifx.slack.com/archives/C08R694QVNX/p1792040613876479 https://mahifx.slack.com/archives/C08R694QVNX/p1792061221645329?thread_ts=1792040613.876479

### mt4-server-clone — Fintokei new MT4 server needs copy of feeder and bridge
status: open · since: 2026-10-12 · last: 2026-10-12
State: Jan Becan says Fintokei is deploying a new MT4 server as a copy of the existing one and wants exact copies of the feeder and bridge with all settings. Asked what Mahi needs from them. Rory King replied "we'll review and let you know".
Next: Mahi (Rory) to say what is needed from Fintokei.
Refs: https://mahifx.slack.com/archives/C08QWKFARDL/p1791806622473929 https://mahifx.slack.com/archives/C08QWKFARDL/p1791806684630299

### skew-arb-defence — arbitrageurs exploiting skew flicker (GBPJPY, XBT)
status: open · since: 2026-09-30 · last: 2026-10-02
State: XBT FI PnL drops on 2026-09-30 came from oversized skew (LSB $5 wide pushed to $17+); Shyam cut floor 500 to 10 and ceiling 2000 to 500 pips on IFMS and harmonic. Fintokei risk (Lukas) reported accounts 6103016 and 6104366 farming GBPJPYz flicker; William Denny confirmed an arber had influenced the neuron signal, switched GBPJPY neuron to harmonics (2026-10-01) and is reducing arber influence on signals. Arbers were auto-classified but stayed on the skewed internal price because executing them on the continuity pool adds slippage; Lukas first asked for both accounts to go to the pool, then he and Roman Komurka agreed (2026-10-02) to try the signal change plus monitoring first. The XBT arber got a fresh tag on each challenge stage (accounts 6094087, 6098579, 6099739; tags do not carry over), so Shyam whitelisted 6099739 as an arber for Funded LS Clients. Andrew Morgan says arb detection/defence should be per instrument; his follow-up fed this into /skew-health-check (adaptive switching over signals by recent skew PnL) and a research backlog item, with no live change or backtest launched.
Next: William to monitor skew PnL and verify arbing is reduced (continuity-pool execution is the fallback if not); William asked for per-trade skew amount to be persisted to yield profiles (no answer seen).
Refs: https://mahifx.slack.com/archives/C08R694QVNX/p1790733359556629 https://mahifx.slack.com/archives/C08QWKFARDL/p1790856065770089 https://mahifx.slack.com/archives/C08QWKFARDL/p1790941538452089?thread_ts=1790856065.770089 https://mahifx.slack.com/archives/C08R694QVNX/p1790952627862029?thread_ts=1790733359.556629

### no-price-cancels — orders cancelled when LP feed drops; TTL and SL/TP stuck in MT5
status: open · since: 2026-09-07 · last: 2026-10-02
State: Triggered orders with no published price are rejected immediately (no TTL parameter exists); on 2026-09-07 the XAUUSD cancel happened because the Fintokei feed and all other LPs dropped together. Pau said TTL would be welcome (used in other engines) and Kate promised updates after internal discussion (none seen); Fintokei also asked on 2026-09-21 for execution on the last available price. Daria declined last-price execution (risk of stale fills when the feed is indicative) and offered to back the feed with other firm feeds. 2026-09-25 USOILp close was cancelled because Fintokei's LP feed stopped at 20:59:30. Adam also reports SL/TP orders rejected for stale price in Compass end up stuck in MT5 (gateway not passing rejection) and wants the tech team to investigate; he has no order IDs because they delete the orders, and will send logs next time. Kate (2026-10-02) will look into what she can without IDs.
Next: Fintokei (Adam) to send order IDs/logs on the next stuck SL/TP; Mahi (Kate) to investigate the MT5 gateway rejection handling and update Pau on TTL.
Refs: https://mahifx.slack.com/archives/C08QWKFARDL/p1788776409327359 https://mahifx.slack.com/archives/C08QWKFARDL/p1789980122311229 https://mahifx.slack.com/archives/C08QWKFARDL/p1790603545212809 https://mahifx.slack.com/archives/C08QWKFARDL/p1790930827758139?thread_ts=1790846280.783699

### cfd-normalisation — Kate proposes second-LP normalisation for CFD pricing
status: open · since: 2026-09-28 · last: 2026-10-01
State: CFD pricing is built from a single LP feed with no second source, so a feed drop blanks the book. Kate proposed normalisation (align a second LP onto the primary) and optional config to force the model indicative at the 20:59:30 weekly stop; offered a call or setup on the beta model first. Adam (2026-10-01) replied they will think about it but want the stuck SL/TP issue (no-price-cancels) addressed first; no decision on call / beta trial.
Next: Fintokei to decide on call / beta trial after SL/TP investigation.
Refs: https://mahifx.slack.com/archives/C08QWKFARDL/p1790605312090849 https://mahifx.slack.com/archives/C08QWKFARDL/p1790846139509429?thread_ts=1790605312.090849

### ld-network-incident — fleet-wide LD networking incident, 2026-10-16
status: watching · since: 2026-10-16 · last: 2026-10-16
State: Liam Cordelle announced a networking incident in the LD environment on 2026-10-16 (~09:31 UTC), advising clients with a failover to switch to it. Adam Foltyn asked which connections were affected and whether it was isolated to Fintokei; Liam said it is fleet-wide, all LD clients affected to some extent, with the hosting provider investigating. At ~10:46 UTC Liam reported signs of recovery. No all-clear, root cause or Fintokei-specific impact summary posted yet.
Next: Mahi (Liam) to post all-clear, RCA and Fintokei-specific details.
Refs: https://mahifx.slack.com/archives/C08QWKFARDL/p1792143076144139 https://mahifx.slack.com/archives/C08QWKFARDL/p1792147616452629

### compass-26-4-upgrade — Compass 26.3 to 26.4 and related deploys
status: watching · since: 2026-10-08 · last: 2026-10-13
State: 26.4 staged 2026-10-09, live at the weekend restart (client told 2026-10-09). Known pricing change: fintokei sets neither adjustmentSignalParametersForWidening nor ForTightening, so prices now widen/tighten one increment on PSM-W/PSM-T signals; Liam decided to let it go on. RC #7224 (includes a fix for an arb hedger on adaptive reference pricing that failed to start) was approved/self-approved 2026-10-09; infra main to LDN was self-approved before staging. Hugepages on trading-1 raised 2026-10-11 and a Hedger Config/Channel Explorer UI deploy landed 2026-10-13. No post-upgrade issues reported in Slack.
Next: ask Kate whether Zendesk 23102 (BMSL timezone overrides, needed release/26.3+) is now unblocked.
Refs: https://mahifx.slack.com/archives/C08R694QVNX/p1791483333881419 https://mahifx.slack.com/archives/C08QWKFARDL/p1791543779812879 https://mahifx.slack.com/archives/C08R694QVNX/p1791866232732339

### lsb-z-pricing — LSB pricing model (z-suffix symbols)
status: watching · since: 2026-06-30 · last: 2026-08-27
State: CLIENT_PRICE_LSB_LDN went live on z-suffix symbols at the 2026-07-12 Sunday open. 2026-08-26 Fintokei found zero spread on all z FX instead of only 15 pairs (33% reduction elsewhere); TOB benchmarking resolved identically for both subsets since go-live; Kate's thread explanation: benchmarking config was unchanged since the 2026-07-12 go-live, so both subsets sat at zero spread until the fix (the _t test set streamed from 2026-06-30 showed no issues); Lukas confirmed it works as expected 2026-08-27. The 2026-07-13 finding that z-suffix trades fill on the older wide model is not mentioned again. Commercial question (setup fee vs monthly cost, no contract provision) from 2026-06-16 has no Slack resolution.
Next: confirm the execution-routing bug is fixed; Daria to settle setup fee vs addendum.
Refs: https://mahifx.slack.com/archives/C08R694QVNX/p1782815433338759 https://mahifx.slack.com/archives/C08R694QVNX/p1783914394599609 https://mahifx.slack.com/archives/C08QWKFARDL/p1787754510970159 https://mahifx.slack.com/archives/C08QWKFARDL/p1787826867642199?thread_ts=1787755505.765169

### account-requests — new trading accounts, September batch
status: watching · since: 2026-09-24 · last: 2026-09-28
State: Pau requested new accounts 2026-09-24; Cameron Hughes added 27 accounts (cTrader/MT4/MT5) plus FIX connections, multi-channel config and execution rules on LDN the same day. Nathan Burch logged on 2026-09-28 that the 27 accounts were completed but not confirmed to the client; no confirmation to Pau seen in #mahi-fintokei.
Next: Mahi (Cameron Hughes) to confirm completion to Pau.
Refs: https://mahifx.slack.com/archives/C08QWKFARDL/p1790244899556639 https://mahifx.slack.com/archives/C08R694QVNX/p1790579137529469?thread_ts=1790269115.866159

### liquidity-violation — "Liquidity Violation" cancels from stale JPXJPY price
status: closed · since: 2026-07-08 · last: 2026-08-05 · closed: 2026-10-15
State: Cancels on accounts 6058190 (2026-07-08) and 6056302 (2026-08-05) on JPXJPY were due to stale-price protection, not liquidity shortfall; Shyam raised with dev. Rory acknowledged the 2026-08-05 recurrence but no findings were posted. Earliest signal in the window; no Slack activity since.
Next: Mahi (Rory) owes findings on the 2026-08-05 recurrence.
Refs: https://mahifx.slack.com/archives/C08QWKFARDL/p1783508183263049 https://mahifx.slack.com/archives/C08QWKFARDL/p1785919175208259 https://mahifx.slack.com/archives/C08QWKFARDL/p1785919331725949

### sl-exec-delay — SL execution delay on account 6029722
status: closed · since: 2026-07-15 · last: 2026-07-15 · closed: 2026-10-15
State: Pau reported a stop loss on 6029722 (2026-07-14 US news) took ~1.876s from trigger to placement and asked if gateway delay explains it. Rory acknowledged; no findings since. No activity since 2026-07-15; assumed resolved.
Refs: https://mahifx.slack.com/archives/C08QWKFARDL/p1784109810336399 https://mahifx.slack.com/archives/C08QWKFARDL/p1784109838387739

### bmsl-tz-deploy — BMSL timezone overrides (Zendesk 23102)
status: closed · since: 2026-06-16 · last: 2026-06-16 · closed: 2026-10-15
State: Kate raised Zendesk 23102 for per-TradingTimeZone pricing.benchmarkMinimumSpread; blocked on the Fintokei pricer being on release/26.3, which the 26.4 upgrade now supersedes. No Slack update since; follow-up moved to compass-26-4-upgrade.
Refs: https://mahifx.slack.com/archives/C08R694QVNX/p1781610590423249 https://mahifx.zendesk.com/agent/tickets/23102

### ndx-spx-limit-price — limit orders with 100,000x price on NDX/SPX
status: closed · since: 2026-09-08 · last: 2026-09-09 · closed: 2026-10-15
State: Shyam rejected NDX/SPX limit orders from CP 4300683 priced ~100,000x too large; Kristof Heger (2026-09-09) found it was a client's automated-system misconfiguration, already fixed.
Refs: https://mahifx.slack.com/archives/C08QWKFARDL/p1788906654679089 https://mahifx.slack.com/archives/C08QWKFARDL/p1788945082237219?thread_ts=1788906654.679089

## Arc
- 2025-07 — Beeks admin server NIC outages, NICs replaced; resolved mid-July
- 2025-09-02 — Crypto addendum fully executed
- 2025-11-24 — Weekly FI PnL snapshots start in #mahi-fintokei (~$310-313k/week)
- 2026-05-25 — MT4 bridge rejection incident; root cause MTB-391 reserveUUID leak (RCA 2026-05-26)
- 2026-07-12 — New LSB pricing model live on z-suffix symbols at Sunday open
- 2026-08-26 — Zero-spread misconfiguration on all z FX symbols found and fixed
- 2026-10-11 — Compass 26.4 live at weekend restart
- 2026-10-16 — Fleet-wide LD networking incident affects Fintokei connectivity; recovering by midday
