---
slug: icmarkets
aliases: [icmarkets-crypto]
refs:
  vibepulse: ../VibePulse/.claude/clients/icmarkets.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: icmarkets-crypto
  hosts: ../MahiProduct/data/client-hosts.json          # entry: icmarkets
  wiki: ../MahiProduct/wiki/clients/icmarkets-crypto.md
channels:
  internal-ic-markets: C07TZ00FK1Q
  mahi-ic-markets: C07UBJNUWG1
contacts:
  - {name: "Pavlos Elpidorou", role: "IC Markets Head of Market Risk (Compass/Echo user); approves LR/spread/hedging changes"}
  - {name: "Karam Abo Qoura", role: "IC Markets risk/analytics; defensive-tag requests, LR/last-look asks, news-event latency complaints"}
  - {name: "Harry Politis", role: "IC Markets; asks for per-account execution/LR reviews", confidence: low}
  - {name: "Nouri Dalati", role: "IC technical/infra contact; FIX routing, China crypto connection, in-house account checks"}
  - {name: "Chi-Loong Ho", role: "IC technical; connection audits, price failover (maker pool)", confidence: low}
  - {name: "Andreas Charalampous", role: "IC; reports BTCUSD/MT5 server incidents, joined 2026-08-13", confidence: low}
  - {name: "Savvas Savva", role: "IC; reported BTCUSD rejections 2026-09-07", confidence: low}
  - {name: "Xenofon Neokleous", role: "IC; spread/slippage queries (XBTUSD), joined 2026-08-13", confidence: low}
  - {name: "Elbekjon Kh", role: "IC; slippage query 2026-08-31", confidence: low}
  - {name: "Angus", role: "IC senior decision-maker above Pavlos on commercial sign-off; surname not seen", confidence: low}
  - {name: "Kyriakos", role: "IC; requested toxic account list and Compass/Echo access; first name only", confidence: low}
  - {name: "Vasilis", role: "IC; sits between Pavlos and Angus on commercial sign-off; surname not seen", confidence: low}
  - {name: "Joanna Theophanous", role: "IC ops/client-side contact", confidence: low}
  - {name: "Dimitrios Lambrou", role: "IC; joined 2026-05-18, role unknown", confidence: low}
  - {name: "Konstantinos Haitas", role: "IC; Compass/Echo access via Kyriakos, role unknown", confidence: low}
  - {name: "Neophytos Poullou", role: "IC; joined 2026-06-11, role unknown", confidence: low}
  - {name: "Andreas Xenofontos", role: "IC; joined 2026-07-02, role unknown", confidence: low}
  - {name: "Kok Hou Chan", role: "IC; joined 2026-08-03, role unknown", confidence: low}
  - {name: "Marios Christofidis", role: "IC; joined 2026-09-14, role unknown", confidence: low}
  - {name: "Harries Hingco", role: "IC; joined 2026-09-01, role unknown", confidence: low}
  - {name: "Joshua Yiap", role: "IC; joined 2026-08-24, role unknown", confidence: low}
last_catchup: 2026-10-15T13:04:16Z
status: active
---

## Now
IC's crypto (XBTUSD-centred) B-book is Mahi's live product there, and the commercial relationship is in a renegotiation phase, so Mahi is deliberately front-footing value-add ("hero moments", price forensics) in client replies.
Open: IC's CPI-news latency complaint (Oct 14) and its last-look request, where the cause was an internal fallback rule that dropped LP1 as primary pricing source, plus PSM spread logic running in Beta ahead of a Price Forensics demo.
Isaac Dann is primary quant lead on the account since 2026-10-08.

## Streams

### cpi-news-latency — CPI news-event latency complaint and last-look change
status: open · since: 2026-10-15 · last: 2026-10-15
State: Karam says accounts (240069580 plus 250040598, 330025738, 330029906 per his 10:51 BST follow-up) traded ~1s after the Oct 14 12:30 UTC CPI print and suspects price latency. Mahi replied the published price reacted within 65ms (inside the default 100ms last look) and LR plus FI added ~316 $/M over the 4-minute window. Internally Isaac found the real cause: FallbackToSecondaryPricingNode dropped MAHI_CRYPTO_LP_1 (Wintermute) as primary for 60s because LP1's 1 BTC spread (~$700) exceeded 20x base (`fallbackSpreadTooWideRatioOfBase`=20), and the fallback markets were slower. Karam then asked for 150-200ms last look on high-impact news; Isaac actioned `newsAdditionalLastLookDelay` (+50ms for >50 weighted news, +100ms for >100), applying at the next scheduled restart. The team argued about messaging (Andrew: optics, avoid framing the best skew/LR moment as an ops failure; Will: every reply is an upsell during renegotiation).
Next: Isaac to raise `fallbackSpreadTooWideRatioOfBase` and decide whether to disclose the fallback cause to IC; Mahi to send the full reply on the 5 accounts.
Refs: https://mahifx.slack.com/archives/C07UBJNUWG1/p1792056629435349 https://mahifx.slack.com/archives/C07TZ00FK1Q/p1792059917658369 https://mahifx.slack.com/archives/C07UBJNUWG1/p1792068166287969

### commercial-renegotiation — Renegotiation phase and decision-maker mapping
status: open · since: 2026-08-17 · last: 2026-10-15
State: Will Carter says IC is under renegotiation (Oct 15) and every communication should show value-add. In August Cooney spoke to Angus, who stays "at 30,000 feet" and said Pavlos is the person to walk through XAU details; Nicola's read was that Pavlos is influencer not decision-maker and still needs convincing. Crypto full licence (12 months from May) is live; XAU 24/7 and weekend pricing are the open commercial levers.
Next: Mahi to build a value-add narrative (hero moments, PSM demo) before the next commercial call; no date seen.
Refs: https://mahifx.slack.com/archives/C07TZ00FK1Q/p1786983558369939 https://mahifx.slack.com/archives/C07TZ00FK1Q/p1792057523803899

### hero-moments-value-add — Value-add evidence for IC (hero moments, Price Forensics)
status: open · since: 2026-10-08 · last: 2026-10-15
State: Andrew Morgan's value-add-moments scan found 10 positive moments (nine LR, one skew) and six learning windows (report 2026-10-08); Price Forensics was reworked 13-14 Oct to show contribution alongside price action, but client sharing is gated on attribution and IP-filtered evidence. On Oct 15 Andrew argued the views should celebrate Mahi's work and that IC channel interactions skew towards ops fix-ups; he is adding per-channel sentiment scoring and a daily hero-moments routine. The first findings are intended to go to IC with the weekly briefing.
Next: Andrew to sanity-check findings before client delivery; Isaac to propose Slack-plus-dashboard delivery.
Refs: https://mahifx.slack.com/archives/C07TZ00FK1Q/p1791453279474879 https://mahifx.slack.com/archives/C07TZ00FK1Q/p1792057523803899

### xbtusd-pricing-psm — XBTUSD pricing model, TOA lag, PSM in Beta
status: open · since: 2026-08-19 · last: 2026-10-09
State: After IC cut TOB spread to $1 (mid-Aug) a coordinated cohort picked off stale prices in the 25 Aug rally; analysis showed CLIENT_PRICE_NYC lagging LP1/Wintermute (CME-led) by ~250ms via the Tokyo-to-NYC TOA path (129ms feed latency). Mahi raised last look (signal-follow 100 to 300, broker 100 to 200, Pavlos agreed), added signal widening (live Aug 26), and from Aug 27 prices off WM/LP1 normalised to the TOA basis; Sep 1 spreads compressed and volumes rose. Skew tuning caused XBTUSD's first negative FI day on 2026-09-08 (-$13.1k) and was walked back. PSM went live on the Beta stream on 2026-10-09 (base $3.50, floor $1, widening up to +$4, target average ~$4 vs $5 in production).
Next: Isaac to watch Beta 24-48h, adjust base, then use for the Price Forensics demo; PSM-W and PSM-T rollout and a CME feed (Databento) remain unscheduled.
Refs: https://mahifx.slack.com/archives/C07TZ00FK1Q/p1787651304260879 https://mahifx.slack.com/archives/C07UBJNUWG1/p1787652712657649 https://mahifx.slack.com/archives/C07TZ00FK1Q/p1791548828363299

### xau-247-gold — Weekend/24-7 gold and FX/Metals product
status: open · since: 2026-07-13 · last: 2026-10-08
State: XAU pilot expired 2026-06-30; FX/Metals B volume went to zero around 2026-08-04 as IC stopped routing XAU to Mahi. IC (Pavlos) wanted a Pyth 24/7 Gold index with PAXG as divergence guard; in Aug Isaac mapped XAU-adjacent feeds in the IC env (XAUTUSD, PAXGUSD, XAUUSD-PERP) and Binance perp basis. On Oct 8 the team agreed to repackage PAXG as "XAU 24/7", show it in Beta only, and keep the pitch crypto-only; IC is also seeing EURUSD/USDJPY/GBPUSD fills that are being reported on but not yet sized.
Next: Andrew to optimise weekend gold in Beta; no IC commitment seen.
Refs: https://mahifx.slack.com/archives/C07TZ00FK1Q/p1783938383718259 https://mahifx.slack.com/archives/C07TZ00FK1Q/p1791453279474879

### account-reviews — Per-account execution/LR reviews and defensive tags
status: open · since: 2026-08-19 · last: 2026-10-02
State: IC regularly asks Mahi to review specific accounts or add tags to the defensive profile (Aug 19, 21, 27 batches actioned, 5299799 moved to defensive with ~$4k protected). Harry on 2026-10-02 asked for an LR/edge review of high-vol BTC sweeps on 8120817 and Rory replied he will check; on 2026-09-09 a similar request for cTrader account 6165669 was acknowledged by Shyam. A Sep 10 oddity: trades for MT4S27_270073080 appeared on drop copy (clips over $1m, filled better than VWAP) without Mahi executing them; Nouri said it is an in-house group with no live trading.
Next: Rory to report back on 8120817 (no reply seen); account 6165669 review reply not seen.
Refs: https://mahifx.slack.com/archives/C07UBJNUWG1/p1789037279787749 https://mahifx.slack.com/archives/C07UBJNUWG1/p1790929415758279

### connectivity-incidents — Outages and MT5/BTCUSD incident queries
status: open · since: 2026-09-01 · last: 2026-09-23
State: A Beeks BGP outage on 2026-09-01 triggered JMS heartbeat alerts. On 2026-09-21 a TK-NY link failed (AWS scheduled maintenance, single-redundancy) from 13:25 UTC; ETH pricing broke, IC failed over to HK, and James resolved it by ~15:07 UTC; follow-ups are ETH normalisation, dual-redundancy with Beeks (~GBP 500/month) and AWS notice alerting. IC (Andreas) also reported client complaints about opening and closing trades on 2026-09-19 02:00-04:30 GMT+3; William Denny found no Mahi-side gap but suspected an MT5 Server 3 / OneZero hub outage and asked IC for server journals and hub logs. Savvas flagged BTCUSD rejections on 2026-09-07. The 26.4 release on 2026-10-09 succeeded after an overrunning patch process extended downtime to 21:51 UTC.
Next: IC (Andreas) to supply MT5 S3 journal and OneZero hub logs; Mahi decision on Beeks dual-redundancy not seen.
Refs: https://mahifx.slack.com/archives/C07UBJNUWG1/p1789999684236149 https://mahifx.slack.com/archives/C07UBJNUWG1/p1790085738501569 https://mahifx.slack.com/archives/C07UBJNUWG1/p1790179197920489

### cnh-connection-audit — IC connection cleanup and China crypto sessions
status: watching · since: 2026-09-14 · last: 2026-09-14
State: Chi-Loong audited maker/taker ports and asked to remove old FX/CNH-NYC and extra orders sessions while keeping core crypto and `icmarkets_crypto_cnh` (China) and HK as possible backup. Isaac replied he would review; no outcome seen in channel. Downgraded from open: no activity since 2026-09-14.
Next: Isaac to confirm the removal list with IC.
Refs: https://mahifx.slack.com/archives/C07UBJNUWG1/p1789387784721829

### lr-last-look-tuning — Liquidity reduction, WSS caps and last-look policy
status: watching · since: 2026-08-13 · last: 2026-08-25
State: Mid-August the WSS cap was raised to 125 and a notional ladder for LR proposed (Isaac, Aug 18-20); after IC's challenge on tiers Pavlos agreed to 300 $/M up to ~$50k tickets and 1000 above, with global burst cut to 50k and TOB spread set to 5 on Aug 21. Rare-event spread protection (cap $11.50/side) was pushed to Beta on Aug 25 and Pavlos approved on Aug 26. Xenofon's Aug 24 $50 spread blip was liquidity depletion capped by the $500/M channel limit. This stream's current driver is the news-event last look in cpi-news-latency.
Next: none pending beyond cpi-news-latency.
Refs: https://mahifx.slack.com/archives/C07UBJNUWG1/p1787222735783359 https://mahifx.slack.com/archives/C07UBJNUWG1/p1787652712657649

### si-hedging-clusters — Cluster LR groups and XBTUSD SI hedging
status: watching · since: 2026-08-20 · last: 2026-08-26
State: Pavlos grouped the BTCUSD cluster list into 3 clusters with shared liquidity pools and Signal Follow settings (2026-08-24), after Cooney's 6 new BO groups on Aug 21; cluster flow is sharp (about 10-20 $/M captured). Cooney set up SI hedging for XBTUSD: hold 5m for 2h, hard limit 20m, working out of excess via passive OKX orders (OKX moved HK to Tokyo). It remains on B Book because IC has not confirmed the switch ("throw the switch").
Next: IC (Pavlos) to approve switching SI on.
Refs: https://mahifx.slack.com/archives/C07UBJNUWG1/p1787327600173079 https://mahifx.slack.com/archives/C07UBJNUWG1/p1787573389998509 https://mahifx.slack.com/archives/C07UBJNUWG1/p1787731325918319

## Arc
- 2026-05-11 — Crypto full licence contract confirmed signed, 12-month term
- 2026-06-05 — Compass upgrade deployed cleanly in IC maintenance window
- 2026-06-30 — XAU pilot expired (extended once from 2026-05-29); no formal terms announced
- 2026-07-14 — IC begins routing China crypto flow through the new Mahi_CNH connection
- 2026-08-04 — FX/Metals B volume goes to ~zero as IC stops routing XAU
- 2026-08-16 — WSS distribution bug fixed for IC crypto
- 2026-08-27 — Pricing switched to Wintermute/LP1 normalised to TOA basis after rally pickoff
- 2026-09-21 — TK-NY link outage (AWS maintenance); resolved same day
- 2026-10-08 — Isaac Dann named primary quant lead for IC
- 2026-10-09 — Compass 26.3 to 26.4 release; PSM live on Beta XBTUSD
- 2026-10-15 — Renegotiation phase flagged; CPI latency complaint answered with value-add framing
