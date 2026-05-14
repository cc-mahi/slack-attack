---
slug: toa
refs:
  vibepulse: ../VibePulse/.claude/clients/toa.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toa
  wiki: null
channels_override: null
key_people_overrides: []
last_catchup: 2026-05-14T07:32:23Z
---

## Status

- **Stage:** live and expanding rapidly. Nado (Vertex 2.0) launched 2025-11-21 as primary crypto venue replacing Vertex. Spot markets (WETH, kBTC, USDC, BNB) + BTC/ETH perps at launch; dozens of new perps added Dec 2025–Apr 2026 (HYPE, MONAD, ZEC, XAUT, Lighter, DOGE, kBONK, kPEPE, UNI, XPL, ASTER, ONDO, and more). FX perps live 2026-03-26; Silver (XAG) 2026-03-17; Oil (CL/WTI) ~2026-03-24; ETF pricing (QQQ/SPY) 2026-03-31; Mag7 perps 2026-04-08. CVEX wound down September 2025 (rebranded as Pascal/Jetstream). NLP is the primary liquidity provider for Nado spot and perp markets. Argamon Tokyo live on minor coins 2026-04-14+ (Eugen setting up pricerInstiLight1/2).
- **Integration:** Mahi infra hosting Toa's pricing/distribution across APN1, CHI, EUW2, USE2; CHAOS_ORACLE quoting ETF prices, CFD feeds weekday-only. Replace workflow (cancel-and-place) deployed mainnet 2026-02-23 via Lee. Nado's `/ws/v2` (faster, async responses) piloted on testnet by Lee — intermittent connection-reset under load (affects both old+new endpoint; likely proxy/limit issue). NLP fee structure: 0/-3bps maker/taker; vault cap targeting 10M. Recurring AMQ disk and DB space issues on APN1; Binance instability operationally managed by ops team.
- **Relationship:** sister company (same CTO — James Furness); James and Lee effectively dedicated. Ops team (Inald, Arun, Maten, Daria, Isaac, Liam) handles 24/7 crypto on-call. Slack: `internal-toa-ops`, `toa-nado-shared` (cross-workspace, ink-foundation).

## Recent issues

> [resolved] 2026-05-13 — starfishFilePersisterExternalMarketData down on TOA LDN: signals gap in Pulse, restarted by Daria
> Daria restarted `starfishFilePersisterExternalMarketData` in LDN, restoring signals in Pulse. Last data aligned with the most recent prior restart; no suspicious config changes. Root cause unknown — Daria's best guess is restart-related. Lee acknowledged. No backfill source available for the gap. https://mahifx.slack.com/archives/C035H1VNCAD/p1778639825532889

> [resolved] 2026-05-11 — marketDataCboe1 down on TOA Argamon CHI: new process, resolved in ~33 min
> Inald flagged marketDataCboe1 down on TOA Argamon CHI (16:55 UTC). James replied it was a new process he was adding. Inald resolved the ordersCboe alert independently; James confirmed the process was up by 17:29 UTC. https://mahifx.slack.com/archives/C035H1VNCAD/p1778514939388589

> [resolved] 2026-05-08 — EURUSD-PERP 1% wide on Nado: deliberate RWA depth cut due to absent DMM liquidity
> Kento (Nado-side) flagged EURUSD book 1% wide at 04:33 UTC. Lee loosened the FX max risk limit to allow one-sided quoting. Later that day (13:26 UTC) Nado clarified the RWA depth was deliberately cut the prior week because NLP cannot hedge risk without DMM liquidity — not a misconfiguration. https://ink-foundation.slack.com/archives/C09RGU1T1GE/p1778214820766959

> [open] 2026-05-06 — Toa Argamon LDN rejects: oncall investigation requested
> Lee Butts (06:57 UTC) tagged the oncall subteam to investigate rejects on the Toa Argamon LDN instance; stated he was not at a computer. No reply or resolution in thread as of window close. https://mahifx.slack.com/archives/C035H1VNCAD/p1778050635016669

> [resolved] 2026-03-31 — Nado ETF pricing live on APN1
> ETF pricing rolled out as planned on the 2026-03-31 target. QQQ/SPY opened for trading on 2026-04-02. https://mahifx.slack.com/archives/C09RGU1T1GE/p1774964941888099

> [resolved] 2026-04-08 — Mag7 perps onboarded, BE rejects fixed
> Mag7 perps (MSFTUST/NVDAUST/AAPLUST/AMZNUST/TSLAUST/METAUST/GOOGLUST-PERP) hit `2069: Trading is blocked for this market` rejects on first quote attempt; Nado side flipped them on within minutes. Follow-up TSLA depth issue was Chaos backup pricing during NASDAQ closed hours (working as designed); James pushed staleness-tolerance change so Chaos rate doesn't appear stuck out of hours. https://mahifx.slack.com/archives/C09RGU1T1GE/p1775678206463809

> [resolved] 2026-04-09 — traderNado2 crashed on null SPOTINDEX prices (MSFTUST/AMZNUST PERPs)
> APN-SEC `traderNado2` came down with `IllegalStateException: ... price from SPOTINDEX:MSFTUST<-[EQUS_MINI/MSFTUSD] has changed from not-null to null`, then same on traderNado1 for AMZNUST. Restarted, both back up. Followed by NADO_POOL_MM position-rec mismatches booked via JMX. https://mahifx.slack.com/archives/C035H1VNCAD/p1775739105479449

> [open] 2026-04-10 — Nado balance reconciliation: no way to decompose settled PnL from USDT spot
> Mahi building a balance-rec monitor comparing gateway `subaccount_info` USDT spot vs internal realised-PnL position; mismatch grows because gateway's USDT includes continuous perp PnL settlement. Nado confirmed it's not exposed via REST/WS — suggested deriving via `-net_entry_unrealized - v_quote_balance`. Mahi to try that approach. https://mahifx.slack.com/archives/C09RGU1T1GE/p1775797523845519

> [resolved] 2026-04-13 — traderNado1 order-breaches outage on APN-PRI; bulk-ack visibility issue surfaced
> Cameron paged James after restart didn't stick; James found WebSocket dead, `ordersNado1` restart recovered it. A low-urgency position-break PD alert went unseen during the incident because Cameron's bulk-ack-via-API didn't filter by urgency. Cameron added an urgency flag to the ack so low-urgency alerts can't be accidentally bulk-acked, and flagged building a "float low-urgency that needs prompt action" mechanism. James pushed back: most ambient low-urgency stuff is really EOD-SLA telemetry that shouldn't be on PD at all. https://mahifx.slack.com/archives/C035H1VNCAD/p1776083029602669

> [open] 2026-04-15 — stuckOrder alert resolves at exactly 60s (replace-order-rejected loop)
> Cameron raised stuck-order + timeout alerts on `toa-apnortheast1-prod-pri-1` (traderNado1 SPY layering); cancel returned at exactly the 60s deadline. Lee identified the trader getting stuck in a replace-order-rejected loop and is working on a fix. James also asked whether the alert deadline could be extended past 60s if it's a recoverable automated path. https://mahifx.slack.com/archives/C035H1VNCAD/p1776251765484639

> [resolved] 2026-04-15 — PnlDropAlerter false-positive on transient swings; fix committed 2026-04-23
> Cameron raised a PnL drop alert (Argamon LDN, but the alerter is shared Toa-stack infra). James's writeup attributed it to a real ~$8.8K swing inside 2 minutes that Graphite's 60s TRADEPOSITIONPNL smoothed away — alerter not wrong, but operationally noise. systemStateMonitor `--binaryLogOutputPath` was rolled back 2026-03-08 so tick-by-tick binlogs unavailable. Fix committed 2026-04-23 (`MahiMain` c2cdb3b3); James confirmed fix on same day — needs release + config set but commit is done. https://mahifx.slack.com/archives/C035H1VNCAD/p1776245271372289

> [resolved] 2026-04-29 — `/ws/v2` testnet rollout: intermittent connection-reset under load
> Nado asked Lee to pilot the new `/ws/v2` endpoint on testnet (faster, responses no longer strictly ordered across requests; per-request still atomic — would obviate IoC/PostOnly segregation per James). Lee hit `java.net.SocketException: Connection reset` running the test suite; Nado side confirmed it didn't reach their gateway. Lee reproduced once on the old `/ws` URL too — diagnosed as existing limit/proxy issue not specific to v2. As of 2026-04-30 thread close, Nado confirmed and investigation concluded. https://mahifx.slack.com/archives/C09RGU1T1GE/p1777450163783759

> [resolved] 2026-04-29 — Toa asking for NLP depth/size update post SLA reductions
> Toa-side asked James to update the shared NLP depth/size sheet given recent SLA reductions. James replied in-thread with a canvas doc (Toa Capital Slack canvas F0B0LF4TJ0J) containing the past-24h avg depth/size NLP is currently servicing. https://mahifx.slack.com/archives/C09RGU1T1GE/p1777452146937409

> [open] 2026-04-30 — CVEX EUW2 risk limit hit: BTC-30MAY25 quoting stopped
> `noRecentOpenOrderUpdates.CVEX-BTC-30MAY25` PD fired after no two-way orders since 13:53 UTC; Justin identified Toa at the risk limit with no way to close risk. James noted alerting will need to be backed off given the limit is a structural cap. Justin resolved the PD alert at 17:54. Alerting threshold calibration for CVEX contracts at max risk remains open. https://mahifx.slack.com/archives/C035H1VNCAD/p1746030941556329

> [resolved] 2026-05-04 — noRecentOpenOrders PD on APN1: XETUST-PERP, XBTUST-PERP, SOLUST-PERP
> Three Nado instruments fired `noRecentOpenOrders` PD alerts on TOA APN1 following a reboot. James confirmed processes looked live; Leo verified all procs up on both boxes; resolved within 6 minutes of the alert. https://mahifx.slack.com/archives/C035H1VNCAD/p1777904442214679

> [resolved] 2026-05-05 — traderVertexSei1 crash loop on APN1: VERTEX cancel timeouts
> traderVertexSei1 crashed 3+ times in quick succession (`Exceeded maximum number of order breaches (0): [VERTEX cancel timed out: ...]`). Inald handled: turned off books, bounced ordersVertex1, restarted traders; stable after fourth attempt. paidGivenProfileProcess also came down and was restored. https://mahifx.slack.com/archives/C035H1VNCAD/p1746454824352989

> [resolved] 2026-05-12 — Toa-CHI OOM: riskReporting1/riskPath down
> Both `riskReporting1` and `riskPath` on Toa-CHI came down with native OOM (`mmap failed to map 2113929216 bytes`). Resolved after memory bump and process restarts. Also same day: high VAR alert at TOA APN1 (12,654 USDT) — levelled off after monitoring. https://mahifx.slack.com/archives/C035H1VNCAD/p1747079989606149

> [resolved] 2026-05-15 — signalProcessAP1-1 OOM at TOA APN (recurring, fix in progress)
> signalProcessAP1-1 at TOA APN OOM at 8192MB. Reoccurred 2026-05-21 (heap space OOM). James was testing fixes; still in testing on 2026-05-21. https://mahifx.slack.com/archives/C035H1VNCAD/p1747299963170189

> [watching] 2026-05-22 — Crypto infrastructure expansion: new APN boxes, Binance moved to rocky 8
> Lee moved traderBinance1 to new rocky 8 `toa-apnortheast1-prod-crypto-2` box 2026-05-22 (alerts now route to existing Toa APN PD service). New `toa-apnortheast1-prod-crypto-01` box being built in parallel; alerts suppressed until declared live. Recurring limit-price-breach and self-trade alerts on crypto-2 flagged by Lee as spammy (can resolve). https://mahifx.slack.com/archives/C035H1VNCAD/p1747885755306959

> [open] 2026-05-18 — traderCvex CVEX order-breach crash loop: recurring pattern
> traderCvex crashing repeatedly on order breach exceptions (`Exceeded maximum number of order breaches (0): [CVEX replace order timed out ...]`) across EUW1 and EUW2. Multiple instances: 2026-05-18 (Daria), 2026-06-27 (Maten, twice), 2026-06-30 (Maten), 2026-07-04 (ongoing thread). Each resolved by bouncing ordersGW and restarting trader, but the root cause — CVEX replace order timeouts causing breach trips — is not fixed. James identified the breach limit is set to 0 (zero tolerance). https://mahifx.slack.com/archives/C035H1VNCAD/p1747601897439739

> [resolved] 2026-06-23 — ordersVertex1 fails to start: Vertex contract load timeout (APN-TOA)
> ordersVertex1 failing on APN1 with `Error loading contract data: Timed out after 60 seconds waiting for response for {"type":"contracts"}`. traderVertexSei1 also down as a result. Stable after several restart attempts; Arun confirmed orders and trades flowing. https://mahifx.slack.com/archives/C035H1VNCAD/p1750688652805529

> [resolved] 2026-06-24 — Crypto.com FIX migration: temporarily offline
> CDC would not allow two simultaneous FIX sessions; James turned off Crypto.com while migrating connections to the new `toa-apnortheast1-prod-crypto-2` server. CVEX also turned off during the transition. Both back live 2026-06-26. https://mahifx.slack.com/archives/C035H1VNCAD/p1750764060944289

> [resolved] 2026-07-01 — CVEX EUW2 MD feed died: cancel-ratio alert
> CVEX market data feed died (failing to peg bids/offers), causing 99% cancel-ratio PD alert. James restarted MD feed; alert auto-resolved by James in PD. https://mahifx.slack.com/archives/C035H1VNCAD/p1751363641150399

> [open] 2026-07-02 — High VaR with increased Argamon crypto flow: threshold needs tuning
> High VaR alert (~50k now at critical threshold) following increased crypto flow from Argamon. James bumped critical VaR limit to 50k temporarily. Acknowledged that thresholds need tuning to match the new Argamon volume. https://mahifx.slack.com/archives/C035H1VNCAD/p1751443836066739

> [open] 2026-07-04 — Crypto.com crossed data + cancel-ratio alert
> Crypto.com market data became crossed again on 2026-07-03 (James bounced marketDataCryptoDotCom). 2026-07-04 Daria bounced the MD gateway to fix crossing. Leo raised a 78% cancel-ratio alert (`CRYPTO_DOT_COM/PROP_TRADER_CRYPTO_DOT_COM_1`, 629 of 808 orders cancelled in 15 min). https://mahifx.slack.com/archives/C035H1VNCAD/p1751612943352569

> [resolved] 2025-12-29 — ExternalOrder DB full on APN1-PRI (324 GB); truncated to recover
> Sam Hewitt identified ExternalOrder tables had grown to 324 GB (total disk 327 GB) on toa-apnortheast1-prod-pri-1, filling messagePersister with alerts. Lee extended the MySQL disk and Sam truncated ExternalOrder and ExternalOrder_properties tables. Recurring disk pressure pattern from Nado trade volume growth. https://mahifx.slack.com/archives/C035H1VNCAD/p1767052175728059

> [resolved] 2026-01-02 — AMQ disk full on APN1-PRI: ~1 hr Nado outage
> ActiveMQ message store filled disk on toa-apnortheast1-prod-pri-1; messagePersister backpressure took the Nado maker down for ~1 hr. Liam resolved and confirmed recovery in toa-nado-shared. Recurring AMQ disk-full pattern (also hit Dec 2025 and Feb 2026): messagePersister accumulates unbounded until disk is full, then trips all downstream processes. Root cause (retention/size config) not definitively fixed across the window. https://mahifx.slack.com/archives/C035H1VNCAD/p1767376466119649

> [open] 2026-02-16 — Toa APN1 PagerDuty noise: 2064 incidents flagged for review
> Cameron shared a PD incident review for Toa APN1 covering the prior period: 2064 total incidents, top sources slowNameFactoryLookup (757) and orderBookStuck (465). Most are suppressible bot noise or alert threshold mismatches. Alert tuning work initiated but not closed — no follow-up commit or threshold change observed through window end. https://mahifx.slack.com/archives/C035H1VNCAD/p1771238401696939

> [resolved] 2026-02-23 — CHI unrealised PnL reporting broken: wrong defaultClientPriceMarket in SSM
> Toa CHI showed broken unrealised PnL figures. Root cause: systemStateMonitor was configured with the wrong `defaultClientPriceMarket`. Fixed 2026-02-23 by Lee. https://mahifx.slack.com/archives/C035H1VNCAD/p1771885704601639

> [resolved] 2026-03-26 — traderNado1 crash loop on FX perp launch day; stabilised on code version 26.3
> FX perps (XXXUSD-PERP format) went live on Nado mainnet 2026-03-26. traderNado1 on PRI crashed repeatedly ("Exceeded maximum number of order breaches (0): [NADO new order confirmation timed out]") — Leo/ops bouncing it every 10–15 min. Lee and James investigated: PRI rolled forward to 26.3 (fix: da20e247); SEC rolled back to 25.4 with a backported FX perp fix (d17402d6). PRI stable on 26.3 after ~1 hr. Firewall change also needed for 26.3 (a7783ffb, deployed 2026-04-02). Stuck-order risk during WS response-channel failures flagged by James — ordersNado1/2 bounce on startup sends cancel-all. https://mahifx.slack.com/archives/C035H1VNCAD/p1774549995951549

> [resolved] 2026-04-23 — traderBinance1 crash loop on Argamon APN1: config issue, stabilised
> traderBinance1 kept crashing on toa-apnortheast1-prod-argamon-1. Leo tried bouncing ordersBinanceFutures1 without success; James not available (Noey bedtime). Stable after Leo applied config changes and bounced ordersBinanceFutures1 again later in the evening. https://mahifx.slack.com/archives/C035H1VNCAD/p1776966508050719

> [watching] 2026-04-30 — FIELD_VALIDATION_ERROR rejects on APN PRI: TOO_SMALL quantity and maximumShowQuantity
> Maten reported a wave of rejects from Nado on toa-apnortheast1-prod-pri-1: `FIELD_VALIDATION_ERROR: {quantity=TOO_SMALL, maximumShowQuantity=TOO_SMALL}`. No follow-up resolution seen in the window — likely a Nado-side min-size change on a perp instrument requiring config update on Mahi side. https://mahifx.slack.com/archives/C035H1VNCAD/p1777559946762319

> [resolved] 2026-05-01 — EURUSD-PERP SLA alert: one-sided open orders, no action taken
> Maten flagged EURUSD-PERP had only one-sided open orders on TOA APN1, triggering an SLA alert (PD Q2BXAKEQGDST1L). No restart or intervention noted — consistent with FX perp behaviour at market close / expected gap. https://mahifx.slack.com/archives/C035H1VNCAD/p1777662669701519

> [resolved] 2025-11-21 — Nado spot market launch: WETH/kBTC/USDC/BNB/BTC-ETH perps go live
> Nado spot markets (WETH, kBTC, USDC, BNB) and BTC/ETH perps launched on 2025-11-21. James spent the day tuning: spread widening, throttle limits (increased from 10k to 60k orders/min), spot pricer fix (odd single bid/offer creating a strange mid), BNB pricing issue resolved by restart. Nado side noted thin candle resolution due to low trade frequency and requested tighter NLP quotes. Stable by evening with ETH perp near risk limit. https://mahifx.slack.com/archives/C09RGU1T1GE/p1763755276568719

> [resolved] 2025-12-12 — Latency crisis: Nado market data 200ms worst-case, orders >30ms speedbump
> Dec 2025 review call: NLP performance at -0.5bps (below breakeven); last 7 days lost ~$7,500. Market data latency 200ms worst case (avg 1-2ms), order posting 43ms, cancel 20ms — all exceeding the 30ms speedbump. Cost: ~$12k to spread deterioration, ~$4.5k to late cancellations. NLP capital utilisation at 1% of $1.6M. Nado side agreed to infra upgrade (hot-warm → hot-hot) and add `remaining_qty` field to order_update for replace workflow. https://mahifx.slack.com/archives/C09RGU1T1GE/p1765547958843559

> [resolved] 2026-02-23 — Replace workflow (cancel-and-place) deployed to mainnet
> Lee deployed replace workflow on Nado mainnet 2026-02-23 after the `remaining_qty` field question was escalated. Latency improved substantially by 2026-03-05/06 — p95 much better post Nado BE changes; TCP retransmissions still unresolved, max latency occasionally 500ms+. Nado confirmed further improvements coming. https://mahifx.slack.com/archives/C09RGU1T1GE/p1771853944369159

> [resolved] 2026-03-17 to 2026-03-31 — FX perps + Silver + ETF pricing rollout on Nado
> Silver (XAG) went live 2026-03-17 after network/system issues. FX perps (XXXUSD-PERP format) live on Nado mainnet 2026-03-26 in post-only mode; FX price feed report shared with notes on JPY divergence vs Hyperliquid. ETF pricing (QQQ/SPY) live 2026-03-31; opened for trading 2026-04-02. Oil/CL listed ~2026-03-24. Chaos oracle price weighting change (Tiingo:1/Finnhub:1/Nobi:2) applied 2026-03-25. https://mahifx.slack.com/archives/C09RGU1T1GE/p1774964941888099

## Notable topics

- Nado weekly maintenance window moved to 22:30 UTC Mon/Thu (was previously aligned to LDN hours); Toa reboot schedule updated to match — PRI reboots Monday 22:30 UTC, SEC reboots Thursday 22:30 UTC. Calendar reminder updated for NZ support coverage instead of LDN. https://mahifx.slack.com/archives/C035H1VNCAD/p1778185084196589
- Cameron asked whether low-urgency PD alerts requiring prompt action will get missed in the noise; James says most should drop off PD entirely as EOD telemetry. Open design question for pagerbuddy / alert routing. PD noise review (Feb 2026) showed 2064 incidents on APN1 — threshold tuning still pending.
- `--binaryLogOutputPath` for systemStateMonitor remains commented out (rolled back 2026-03-08); without it pnlDropAlerter forensics rely on slower log digs. PnlDropAlerter fix committed 2026-04-23 (c2cdb3b3) — needs release + config set before binlogs are useful again.
- Nado NLP vault cap targeted at 10M; NLP fee structure 0/-3bps maker/taker (in place since Dec 2025). Hot-hot infra transition still deferred.
- CVEX wound down September 2025 (rebranded as Pascal/Jetstream). All prior CVEX crash/risk-limit entries are now moot. traderCvex no longer running.
- AMQ disk-full and ExternalOrder DB growth are recurring patterns on APN1-PRI (hit Dec 2025, Jan 2026, Feb 2026). No permanent fix for AMQ retention/size deployed in the window — each incident resolved by truncation or restart.
- Nado listing cadence very rapid (weekly-to-fortnightly new perps Dec 2025–Apr 2026). Bot `Listing Request` pings James in `toa-nado-shared` for each one. Handled ad hoc; no systematic listing-support process on Mahi side.
- Nado spot empty-book alerts on WETH/USDC recurring when NLP hits risk limits; no other MMs to offset spot risk. Nado has been bringing more MMs in but still NLP-dependent for spot.
- traderNado1 crash pattern on order-breach (zero tolerance) recurs under load: FX perp launch (2026-03-26), general crypto activity. Stabilised each time via code version rollforward or ordersNado1 bounce. The breach limit of 0 remains a fragility.
- FIELD_VALIDATION_ERROR (`TOO_SMALL`) rejects seen 2026-04-30 — likely a Nado min-size change needing config update; unresolved in window.
- Key Nado contacts in `toa-nado-shared` (not in wiki/people): Ives Luo (ops/listing), Melanie (ops/listing), jeury (eng), Ian (ops), tony (ops), Chang (infra/latency), Jake (exec/business).
