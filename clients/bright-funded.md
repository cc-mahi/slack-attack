---
slug: bright-funded
aliases: [brightfunded]
refs:
  vibepulse: ../VibePulse/.claude/clients/brightfunded.yaml
  billing: ../MahiProduct/data/billing/clients.json
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "Benjamin Galindo", role: "BrightFunded — primary client contact (product / new programs)", confidence: low}
  - {name: "Jelle Dijkstra", role: "BrightFunded — co-founder, led commercial renegotiation May 2026"}
  - {name: "Syb Dijkstra", role: "BrightFunded — co-founder, attended Mahi anniversary party May 2026"}
  - {name: "Mio Knights", role: "BrightFunded — CC'd on weekly call coordination", confidence: low}
last_catchup: 2026-05-02T07:25:41Z
status: active
retired_at: null
retired_reason: null
---

## Status

- **Stage:** live
- **Integration:** prop firm running 2-Step (Bright + Classic) and 1-Step challenge programs on AWS eu-west-2; Mahi providing prop sims, skew + LR pricing, distribution via LDN.
- **Relationship:** healthy, bi-weekly call cadence with Cameron Hughes; client (Benjamin Galindo) actively engaging on prop sim outputs and a futures expansion ask.

## Recent issues

> [resolved] 2026-04-13 — log disk near-full from marketDataProxyTx spam
> Cameron Copland alerted on `/app/fx/log/mahifx` at 88% (and tickstore at 96%) on bright-funded-euwest2-prod-compass-1; Arun Patel matched the log spam pattern to a recent earlier incident, prescribed a rolling restart of `marketDataProxyTx*`. Restart done same hour, logs confirmed recovered. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1776092711480289)

> [resolved] 2026-04-13 — Benjamin Galindo locked out of admin tooling
> Client couldn't access (screenshot of error). Kate Stagg requested cookie clear, then IP whitelist for 94.204.181.52 once that didn't work; Kate confirmed whitelist request raised. No follow-up message confirms completion but no further complaints in window. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1776066492352719)

> [open] 2026-04-30 — futures prop sims for BrightFunded Futures launch
> On 2026-04-26 Benjamin specced four futures plans (A1/A2/B1/B2 — 6% PT with 4% or 3% MLL, EOD-trailing vs intraday-real-time-trailing drawdown, plus 25% / 40% consistency rule variants) and asked Cameron Hughes to replicate the existing 1-Step sim methodology. Cameron H confirmed feasible on 2026-04-27 and committed to a timeline. As of the 2026-04-30 bi-weekly the action item is still "give an ETA on the futures prop sims" — September is the outer deadline. Commercial renegotiation (May 2026) occupied the relationship; no further futures-sim update visible in the window. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1777191630837849)

> [resolved] 2026-04-14 — new program launched off prop sim pricing
> Bi-weekly on 2026-04-14: client launched their new program the prior day, used the 2026-04-01 prop script results (2-Step Bright/Classic + 1-Step pass-rate + payout figures) to choose pricing. Happy with sim outputs; framing the prop script as useful for pricing future challenges. By 2026-04-30 bi-weekly Cameron H reports the new program is performing well, pass rates close to sim expectations and lower than the OG program, with LR changes recently improving execution across the board. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1776162017645809)

> [resolved] 2026-05-07 — commercial renegotiation: new fee model agreed
> Pilot contract ($30k/month + 10% skew PnL) expired; Mahi targeting ~$18k/month based on April active-user counts (~6k active trading counterparties). Extended commercial negotiation across 2026-05-01 to 2026-05-07: Jelle Dijkstra (co-founder) proposed tiered $2.50–$1.50/account with $30k cap; Mahi proposed $12k fixed + $1/active challenge; David Cooney rejected a $32.5k cap ("not fair to clients who pay multiples of that"). Final agreement on 2026-05-07: $12k fixed + $1/active trading user/month (1 active trading user = 1 unique individual trader), no cap. Addendum to be drafted by Mahi legal (NZ) and sent within days. Long-term intent is to move to Option B (consumption/funded-capital model) via addendum once DX and cTrader platform integrations can supply user+challenge+deposit IDs. April was billed at pilot rate per agreement extension. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746623989396429)

> [open] 2026-06-03 — second pricing model for qualifying traders (tighter spreads)
> Jelle raised on a call (2026-06-03) that VWAP on larger-ticket qualifying traders is causing complaints; wants tighter spreads for qualifying flow only without touching funded. Amir proposed a separate qualifying pricing model (same config, tighter tiers and BMSL) — straightforward to set up but needs a new FIX connection (DX + cTrader = 2 additional connections; BF already uses 3 of their contracted FIX connections). As of 2026-06-04/05 Bonnie checking the contract (1 distribution channel, 3 FIX connections specified); Andrew says $500/month for one model, and server load needs a review before proceeding. Bonnie reached out to Syb, who was unaware of the specifics. Not yet contracted or scheduled. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1748947530909369)

> [resolved] 2026-05-08 — XBTUSD max price stale (100k cap vs 102k live price)
> Isaac flagged at 22:22 BST: BTC live price exceeded the Compass max price config (100k cap). Distribution restarted at scheduled BrightFunded downtime (23:30 CET / 21:30 UTC). Config fix applied to `reference.marketInstrumentDefinitions.priceFormatPipRelative`. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1746739332848859)

> [watching] 2026-05 — recurring pricer memory pressure and latency alerts
> Multiple pricer bounces through May: 2026-05-08 Arun bumped memory on pricer2/pricerBeta1 for MD latency; 2026-05-14 Maten bumped pricer1 from 2GB→3GB and bounced after CPL latency alerts (EURGBP 992ms on CLIENT_PRICE_LDN); 2026-05-16 Arun bounced pricerBeta1 again for allocation stalls (AeronEventLoop 1477ms); 2026-05-21 MdAnalytics OOM'd and self-restarted. Pattern of memory pressure on the BF eu-west-2 pricer fleet; no root-cause fix yet seen in window. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1747218630842229)

## Notable topics

- Bi-weekly client call cadence with Cameron Hughes; 2026-04-28 slot was missed (Cameron H had a clashing appointment), rescheduled to 2026-04-29. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1777370681451249)
- Prop simulation pipeline is now load-bearing for BrightFunded program design — sim outputs (with skew + LR assumed) are driving pricing decisions on both the existing 2-Step/1-Step and the upcoming Futures product. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1775056213954179)
- Jelle and Syb Dijkstra (BrightFunded co-founders) attended the Mahi anniversary party in person (2026-05-08/09); Andrew noted it as a strong buying signal ahead of commercial close. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746791790148969)
- SB PnL analysis (Mio, 2026-05-06): LR PnL 6x higher and LL PnL removal 8x+ higher ($/$M) in the SB group vs non-SB. Client was monitoring the figures; Amir further tightened LR applied to SB and Ultra SB and stretched the refresh period the same day. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746549472142739)
- cTrader integration growing quickly — by 2026-05-01 already at 40% of DX volume; Andrew noted "pretty decent uptake." Flow routing: DX counterparty = user, cTrader counterparty = challenge. Both user+challenge IDs needed for the new consumption-based billing model (Option B). [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1746091872342019)
- Active user count data prep (2026-05-01): Amir queried Feb and April counterparty counts (distinct counterparties from yieldprofiles_latest) for commercial validation. April ~6k active; CLIENTS party was flagged as distorted (channel routing change in Feb/Mar made it redundant). Data used to underpin the $18k/month commercial target. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1746093438800979)
- Match Trade feed stuck (2026-05-01): G30EUR/F40EUR/E50EUR briefly indicative; Jelle confirmed instruments referred to GER30.cash/FRA40.cash/EU50.cash and they were closed for a public holiday. Resolved without intervention. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746109085301459)
- New cTrader account tags announced by Syb (2026-05-02): `fundedNormalSwapsRedLev` and `fundedSwapFreeRedLev` added for reduced-leverage funded accounts. Kate Stagg acknowledged. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746194166004499)
- Crypto pricing went indicative briefly on 2026-05-22 (Match MD login failure ~8 min); Daria noted Pepper LDN could proxy as backup in the continuity pool. Self-recovered. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1747945987365829)
