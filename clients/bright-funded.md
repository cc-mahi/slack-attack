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
last_catchup: 2026-07-06T07:07:04Z
status: active
retired_at: null
retired_reason: null
---

## Status

- **Stage:** live
- **Integration:** prop firm running 2-Step (Bright + Classic) and 1-Step challenge programs on AWS eu-west-2; Mahi providing prop sims, skew + LR pricing, distribution via LDN.
- **Relationship:** healthy, bi-weekly call cadence with Cameron Hughes; client (Benjamin Galindo) actively engaging on prop sim outputs and a futures expansion ask.

## Recent issues

> [resolved] 2026-06-19 — XAUUSD Match Trade pricing gap (US Juneteenth holiday)
> Rory King flagged at 18:05 BST that XAUUSD pricing was not being received from Match Trade; Benjamin Galindo (BF) suggested US bank holiday as the cause; Rory confirmed it was Juneteenth and apologised. Self-resolved, no config change needed. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1781888749613119)

> [resolved] 2026-06-16 — BTC spread widened unexpectedly (distribution.markupProfiles misconfiguration)
> Jelle flagged BTC spread was very wide at 09:02 BST; William Denny and Cameron H both jumped on it. Cameron H identified that `distribution.markupProfiles` for the internal model had somehow been changed to match the continuity pool — no recent config trace found. Widening was at distribution level, not model level. Fix applied by 13:59 BST; Jelle confirmed "Yes, it's fixed now" shortly after. Separately, Jelle also asked to decrease BTC base spreads — Cameron H confirmed "yeah sure, have any values in mind?"; client responded with target values at 13:07 ("Is it done?"), Cameron H applied the change at 13:59, and client confirmed "Yes, perfect!" at 08:14 BST on 2026-06-17. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1781596943927769) [resolved](https://mahifx.slack.com/archives/C08473TFD7Z/p1781680448615449)

> [resolved] 2026-06-01 — free product pricing: how do Mahi charge for one-time-use accounts?
> Syb Dijkstra asked on 2026-05-27 how Mahi pricing works for a free version of BrightFunded (one-time use per user). Cameron H and Will Carter both said they'd raise internally; Mio followed up in the same thread on 2026-06-01 asking for an update. Cameron H resolved on 2026-06-09: free/demo one-time-use accounts will NOT be charged — Mahi charges on unique active accounts per month and the free ones will be excluded. Only requirement: a flag/tag on the account to allow automatic exclusion. Ball is in BF's court to confirm how to identify these accounts. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1780330801690039) [resolution](https://mahifx.slack.com/archives/C08473TFD7Z/p1781009677311779)

> [resolved] 2026-06-01 — AVAX/USD and ATOM/USD slippage (base spreads too wide)
> Benjamin reported significant slippage on AVAX/USD and ATOM/USD at 13:54 BST; Cameron H identified base spreads as too wide and asked Benjamin to check. By 17:44 BST Benjamin confirmed improved but requested a further 50% reduction; Cameron H applied the change and confirmed done at 18:35 BST. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1780318466562819)

> [resolved] 2026-04-13 — log disk near-full from marketDataProxyTx spam
> Cameron Copland alerted on `/app/fx/log/mahifx` at 88% (and tickstore at 96%) on bright-funded-euwest2-prod-compass-1; Arun Patel matched the log spam pattern to a recent earlier incident, prescribed a rolling restart of `marketDataProxyTx*`. Restart done same hour, logs confirmed recovered. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1776092711480289)

> [resolved] 2026-04-13 — Benjamin Galindo locked out of admin tooling
> Client couldn't access (screenshot of error). Kate Stagg requested cookie clear, then IP whitelist for 94.204.181.52 once that didn't work; Kate confirmed whitelist request raised. No follow-up message confirms completion but no further complaints in window. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1776066492352719)

> [resolved] 2026-04-30 — futures prop sims for BrightFunded Futures launch
> On 2026-04-26 Benjamin specced four futures plans (A1/A2/B1/B2 — 6% PT with 4% or 3% MLL, EOD-trailing vs intraday-real-time-trailing drawdown, plus 25% / 40% consistency rule variants) and asked Cameron Hughes to replicate the existing 1-Step sim methodology. Cameron H confirmed feasible on 2026-04-27. Commercial renegotiation (May 2026) delayed progress. On 2026-06-10 Cameron H delivered results — initial run used old plans (4-plan format), corrected on the day to the 2-plan structure (Express: intraday real-time trailing, 50% consistency; Standard: EOD trailing, 40% consistency). Final Express results: Express P1 7.7% pass rate; 113/398 funded payable ($182,104 / $458/acct). Standard: 9.1% P1 pass rate; 122/398 funded payable ($278,618 / $700/acct). Client replied "Great thanks!" — sims delivered. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1777191630837849) [results](https://mahifx.slack.com/archives/C08473TFD7Z/p1781099535990359)

> [resolved] 2026-04-14 — new program launched off prop sim pricing
> Bi-weekly on 2026-04-14: client launched their new program the prior day, used the 2026-04-01 prop script results (2-Step Bright/Classic + 1-Step pass-rate + payout figures) to choose pricing. Happy with sim outputs; framing the prop script as useful for pricing future challenges. By 2026-04-30 bi-weekly Cameron H reports the new program is performing well, pass rates close to sim expectations and lower than the OG program, with LR changes recently improving execution across the board. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1776162017645809)

> [resolved] 2026-05-07 — commercial renegotiation: new fee model agreed
> Pilot contract ($30k/month + 10% skew PnL) expired; Mahi targeting ~$18k/month based on April active-user counts (~6k active trading counterparties). Extended commercial negotiation across 2026-05-01 to 2026-05-07: Jelle Dijkstra (co-founder) proposed tiered $2.50–$1.50/account with $30k cap; Mahi proposed $12k fixed + $1/active challenge; David Cooney rejected a $32.5k cap ("not fair to clients who pay multiples of that"). Final agreement on 2026-05-07: $12k fixed + $1/active trading user/month (1 active trading user = 1 unique individual trader), no cap. Addendum to be drafted by Mahi legal (NZ) and sent within days. Long-term intent is to move to Option B (consumption/funded-capital model) via addendum once DX and cTrader platform integrations can supply user+challenge+deposit IDs. April was billed at pilot rate per agreement extension. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746623989396429)

> [open] 2026-05-05 — new crypto pairs expansion (22 pairs; 4 still need deploy, 2 need instrument clarification)
> Benjamin Galindo requested 22 new crypto pairs; OKB/KCS originally blocked on code change. By 2026-05-18 Isaac Dann confirmed 15 of the 22 are now priced (Kraken/Binance streams, no MWMS/BMSL, 1000 $/M base spread both sides); TONUSD, THETA, OKB, KCS still need a system deploy. MKR is no longer a listed crypto (replaced by SKY at 1:24000 ratio — needs client confirmation on which instrument), and EOS has been relisted as Vaulta at most exchanges (1:1 swap — needs confirmation). Awaiting client response on MKR/EOS and a deploy window for the remaining 4. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1778006518033119)

> [open] 2026-05-08 — coordinated trading detection: weekly CSV delivery ongoing; format refresh overdue; false-positive issue flagged
> BrightFunded asked on 2026-05-08 for Mahi's trading correlation script to combine with their fingerprinting tool for multi-account detection. Cameron Hughes sent the first coordinated-trading CSV on 2026-05-12 (covering 2026-05-05..2026-05-12); second delivery sent 2026-05-21 covering 2026-05-13..2026-05-20 — Mio acknowledged with 🤙; third delivery sent 2026-05-29 covering 2026-05-22..2026-05-29. On 2026-05-29 Mio requested the output be based on sub-counterparty/account number rather than counterparty (while keeping a counterparty tag column); Cameron H explained the current logic uses sub-IDs where available but not all platforms supply them, and delivered the standard run in the meantime. On 2026-06-11 client sent updated spec: correlate pairs on account number (subcounterparty); filter out pairs with fewer than 2 matched trades (≥2 same-or-opposite-side matches over two weeks); add 4-week volume columns per account; remove tag columns (keep counterparty column for deduplication). Cameron H acknowledged "sure thing, I'll let you know once these changes are in place." On 2026-06-15 (~4 days later) client followed up: "Hey mate, any progress on this one yet?" — no response from Cameron H as of 2026-06-17; delivery overdue. On 2026-06-23 call Cameron H noted client is using the collusion detection heavily but there are false positives from the same user appearing on multiple accounts; BF will come up with a way for Mahi to filter those out. Format spec update (sub-account correlation, 4-week volumes) still not confirmed as delivered. Client is also implementing device/payment fingerprinting. [2026-05 permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1779380274437499) [2026-06-11 spec](https://mahifx.slack.com/archives/C08473TFD7Z/p1781192107540339) [2026-06-15 chase](https://mahifx.slack.com/archives/C08473TFD7Z/p1781533676034959) [2026-06-23 call notes](https://mahifx.slack.com/archives/C084G40JXEE/p1782209410357919)

> [open] 2026-06-03 — second pricing model for qualifying traders (tighter spreads)
> Jelle raised on a call (2026-06-03) that VWAP on larger-ticket qualifying traders is causing complaints; wants tighter spreads for qualifying flow only without touching funded. Amir proposed a separate qualifying pricing model (same config, tighter tiers and BMSL) — straightforward to set up but needs a new FIX connection (DX + cTrader = 2 additional connections; BF already uses 3 of their contracted FIX connections). As of 2026-06-04/05 Bonnie checking the contract (1 distribution channel, 3 FIX connections specified); Andrew says $500/month for one model, and server load needs a review before proceeding. Bonnie reached out to Syb, who was unaware of the specifics. Not yet contracted or scheduled. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1748947530909369)

> [resolved] 2026-05-08 — XBTUSD max price stale (100k cap vs 102k live price)
> Isaac flagged at 22:22 BST: BTC live price exceeded the Compass max price config (100k cap). Distribution restarted at scheduled BrightFunded downtime (23:30 CET / 21:30 UTC). Config fix applied to `reference.marketInstrumentDefinitions.priceFormatPipRelative`. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1746739332848859)

> [open] 2026-05-26 — PFM ranking slipping; spreads tightened but still not reflecting
> Jelle flagged (screenshot) that BrightFunded is appearing lower and lower in the PFM ranking list. Cameron H confirmed spreads need tightening and got Jelle's go-ahead. Changes applied: US30 reduced to $1 spread, GBPUSD and USDJPY to 0 pip avg spread; pricers bounced in `internal-brightfunded` to pick up MWMS change. As of 18:47 BST on 2026-05-26 the changes had not yet been reflected in PFM. On 2026-06-02 a new screenshot posted to `mahi-brightfunded` shows BrightFunded "almost last" in spread standings; a Mahi reply noted "This is an issue on PFM side" (2× 👍). Spread tightening changes did not resolve the ranking drop — PFM-side issue identified, no fix visible yet. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1779793894044729) [2026-06-02 update](https://mahifx.slack.com/archives/C08473TFD7Z/p1780414792395589)

> [watching] 2026-05 — recurring pricer memory pressure and latency alerts
> Multiple pricer bounces through May: 2026-05-08 Arun bumped memory on pricer2/pricerBeta1 for MD latency; 2026-05-14 Maten bumped pricer1 from 2GB→3GB and bounced after CPL latency alerts (EURGBP 992ms on CLIENT_PRICE_LDN); 2026-05-16 Arun bounced pricerBeta1 again for allocation stalls (AeronEventLoop 1477ms); 2026-05-21 MdAnalytics OOM'd and self-restarted. Pattern of memory pressure on the BF eu-west-2 pricer fleet; no root-cause fix yet seen in window. (2026-05-26 pricer bounce was unrelated: spread/MWMS config change for PFM ranking — see entry above.) [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1747218630842229)

## Notable topics

- 2026-06-23 call: BrightFunded launched a Revolut partnership. Futures prop sim results well-received — client busy progressing on that. Call cadence moving from bi-weekly to monthly 30-min meetings. [call notes](https://mahifx.slack.com/archives/C084G40JXEE/p1782209410357919)
- 2026-05-12 bi-weekly call: account purchases and volumes dropped in April — client wants to know if industry-wide; new programs performing well and matching sim results; fingerprinting tool in flight to prevent multi-account holders (BF policy: no holding multiple accounts); Mio will reach out to Mahi to collaborate on abusive-trading detection; Match pricing for new instruments would significantly increase client costs — asked if Mahi LPs can price instead. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1778581203791929)
- Bi-weekly client call cadence with Cameron Hughes; 2026-04-28 slot was missed (Cameron H had a clashing appointment), rescheduled to 2026-04-29. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1777370681451249)
- Prop simulation pipeline is now load-bearing for BrightFunded program design — sim outputs (with skew + LR assumed) are driving pricing decisions on both the existing 2-Step/1-Step and the upcoming Futures product. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1775056213954179)
- Jelle and Syb Dijkstra (BrightFunded co-founders) attended the Mahi anniversary party in person (2026-05-08/09); Andrew noted it as a strong buying signal ahead of commercial close. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746791790148969)
- SB PnL analysis (Mio, 2026-05-06): LR PnL 6x higher and LL PnL removal 8x+ higher ($/$M) in the SB group vs non-SB. Client was monitoring the figures; Amir further tightened LR applied to SB and Ultra SB and stretched the refresh period the same day. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746549472142739)
- cTrader integration growing quickly — by 2026-05-01 already at 40% of DX volume; Andrew noted "pretty decent uptake." Flow routing: DX counterparty = user, cTrader counterparty = challenge. Both user+challenge IDs needed for the new consumption-based billing model (Option B). [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1746091872342019)
- Active user count data prep (2026-05-01): Amir queried Feb and April counterparty counts (distinct counterparties from yieldprofiles_latest) for commercial validation. April ~6k active; CLIENTS party was flagged as distorted (channel routing change in Feb/Mar made it redundant). Data used to underpin the $18k/month commercial target. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1746093438800979)
- Match Trade feed stuck (2026-05-01): G30EUR/F40EUR/E50EUR briefly indicative; Jelle confirmed instruments referred to GER30.cash/FRA40.cash/EU50.cash and they were closed for a public holiday. Resolved without intervention. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746109085301459)
- New cTrader account tags announced by Syb (2026-05-02): `fundedNormalSwapsRedLev` and `fundedSwapFreeRedLev` added for reduced-leverage funded accounts. Kate Stagg acknowledged. [permalink](https://mahifx.slack.com/archives/C08473TFD7Z/p1746194166004499)
- Crypto pricing went indicative briefly on 2026-05-22 (Match MD login failure ~8 min); Daria noted Pepper LDN could proxy as backup in the continuity pool. Self-recovered. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1747945987365829)
- Market reopen pricing monitoring (2026-05-05): Shyam Hari asked internal team to keep BrightFunded updated on indicative pricing at reopen and watch pagers; Daria confirmed coverage in place within 4 min. [permalink](https://mahifx.slack.com/archives/C084G40JXEE/p1778016012506979)
