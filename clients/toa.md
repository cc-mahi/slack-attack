---
slug: toa
refs:
  vibepulse: ../VibePulse/.claude/clients/toa.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toa
  wiki: null
channels_override: null
key_people_overrides: []
last_catchup: 2026-08-07T07:45:00Z
---

## Status

- **Stage:** Nado wound down — James confirmed 2026-06-17 17:59 BST: "Nado flat - traders/order processes stopped". NLP switched to Close Only 2026-06-15; USDC position fully closed 2026-06-17. Prior to wind-down: Nado had been live and expanding rapidly since 2025-11-21 launch with dozens of perp/spot/FX/ETF/Mag7 markets added through Apr 2026. CVEX wound down September 2025 (rebranded as Pascal/Jetstream). Vertex formally closed 2026-07-16 (James helped them during shutdown sequence then turned off traderVertex1; `toa-apnortheast1-prod-crypto-1` AWS box shut down). Argamon Tokyo live on minor coins 2026-04-14+, relaunched 2026-06-26.
- **Integration:** Mahi infra hosting Toa's pricing/distribution across APN1, CHI, EUW2, USE2; CHAOS_ORACLE quoting ETF prices, CFD feeds weekday-only. Replace workflow (cancel-and-place) deployed mainnet 2026-02-23 via Lee. Nado's `/ws/v2` (faster, async responses) piloted on testnet by Lee — intermittent connection-reset under load (affects both old+new endpoint; likely proxy/limit issue). NLP fee structure: 0/-3bps maker/taker; vault cap targeting 10M. Recurring AMQ disk and DB space issues on APN1; Binance instability operationally managed by ops team. CVEX recurring crash loop (replace order timeouts, breach limit 0): partial fix committed by James 2026-07-11 (e60cf03); CVEX-side 500 unknown responses still causing crashes — CVEX fixing their end ~week of 2026-07-21.
- **Relationship:** sister company (same CTO — James Furness); James and Lee effectively dedicated. Ops team (Inald, Arun, Maten, Daria, Isaac, Liam) handles 24/7 crypto on-call. Slack: `internal-toa-ops`, `toa-nado-shared` (cross-workspace, ink-foundation).

## Recent issues

> [resolved] 2026-08-06 — hedgerCBOE1 taken offline then restarted with firewall limits raised (per Zendesk), addressing the recurring breach pattern
> Lee Butts took hedgerCBOE1's book offline at 03:33 BST ("ignore the 'should be on' alerts"), then at 06:41 BST fired it back up with firewall limits increased "for now until they're fixed as per zd" — a Zendesk-tracked fix rather than a bare restart. Third recurrence of the hedgerCBOE1 firewall-breach pattern in four days (see 2026-08-05 and 2026-08-03 entries below), this time addressed with a limit change. https://mahifx.slack.com/archives/C035H1VNCAD/p1785983600535619 https://mahifx.slack.com/archives/C035H1VNCAD/p1785994918152899

> [resolved] 2026-08-06 — hedgerHrpCME1 tripped again at TOA-ARG CHI: restarted
> Sam Hewitt (00:37 BST) flagged hedgerHrpCME1 tripping at Toa Argamon CHI (PagerDuty Q3BAT8OWDYXAC0) and restarted it in the same message. Continuation of the recurring hedgerHrpCME1 pattern (see 2026-07-23, 2026-07-22, 2026-07-21 entries below). https://mahifx.slack.com/archives/C035H1VNCAD/p1785973058427919

> [resolved] 2026-08-05 — Second hedgerCBOE1 firewall breach in three days at toa-argamon-ch-trading-1
> Sam Hewitt (05:14 BST) flagged hedgerCBOE1 tripping its firewall at `toa-argamon-ch-trading-1` (PagerDuty Q1RWU3QB0SZF17) and restarted it in the same message. No thread discussion. Second recurrence of the CBOE hedger firewall-breach pattern within three days (see 2026-08-03 entry below). https://mahifx.slack.com/archives/C035H1VNCAD/p1785903258220179

> [resolved] 2026-08-03 — Firewall breach on hedgerCBOE1 on toa-argamon-ch: limit raised, restarted
> Cameron Copland (12:40 BST) flagged a PagerDuty firewall-breach alert on hedgerCBOE1 at toa-argamon-ch (Q2ZBUKVK0KICRP). James Furness raised the `hedging.orderServiceConfiguration` limit and restarted the hedger within 6 minutes; Cameron confirmed he'd been checking it was safe to bring back before James's fix landed. https://mahifx.slack.com/archives/C035H1VNCAD/p1785757251842839

> [resolved] 2026-07-31 — hazelcastNode down on toa-apnortheast1-prod-pri-1: OOM, self-recovered, low criticality
> Inald (15:43 BST) flagged hazelcastNode down on `toa-apnortheast1-prod-pri-1` — `java.lang.OutOfMemoryError: Java heap space`. Confirmed back up minutes later (15:45 BST). James noted the node now only serves the Mahi/IC feed, so low criticality either way. https://mahifx.slack.com/archives/C035H1VNCAD/p1785509004772039

> [resolved] 2026-07-30 — Three HRP_CLIENTS_NET PnL-drop PagerDuty alerts at TOA-ARG LDN, confirmed same event, recovered
> Inald flagged a -5,333 PnL drop on HRP_CLIENTS_NET (15:01 BST, PD Q077AOWF6YDYXL), then two more PD alerts minutes later (Q22KQA1AVNQ1NQ, Q2GV1K2TZO3522). James confirmed all three were the same event seen across different horizon checks and that PnL had recovered almost completely. Continues the recurring HRP_CLIENTS_NET drop pattern (see 2026-07-28, 2026-07-27, 2026-07-22, 2026-06-25, 2026-05-26 entries) — this is the first instance with an explicit recovery confirmation. https://mahifx.slack.com/archives/C035H1VNCAD/p1785420088687629

> [open] 2026-07-28 — Two more HRP_CLIENTS_NET PnL drops on TOA-ARG LDN, no follow-up
> Inald flagged two further PnL-drop PagerDuty alerts at Toa Argamon LDN on HRP_CLIENTS_NET: -4.5k at 11:18 BST (Q0HT9L4SQ0KKGT) and -6.45k at 11:25 BST (Q0OCBP55HJ8JEL). Only a +1 reaction on the second — no thread discussion or resolution. Continues the recurring HRP_CLIENTS_NET drop pattern (see 2026-07-27, 2026-07-22, 2026-06-25, 2026-05-26 entries). https://mahifx.slack.com/archives/C035H1VNCAD/p1785233888832469 https://mahifx.slack.com/archives/C035H1VNCAD/p1785234357012699

> [open] 2026-07-27 — PnL drop at TOA-ARG LDN HRP_CLIENTS_NET ~-7k, no follow-up
> Sam Hewitt (23:23 BST) flagged a PnL drop at Toa Argamon LDN on HRP_CLIENTS_NET of ~-7k, with a screenshot. No thread replies or resolution noted — another instance of the recurring HRP_CLIENTS_NET drop pattern (see 2026-07-22, 2026-06-25, 2026-05-26 entries). https://mahifx.slack.com/archives/C035H1VNCAD/p1785190997465499

> [open] 2026-07-27 — External order rejects on TOA Argamon LDN: rate-limit related, no follow-up
> Inald (09:19 BST) flagged external order rejects at Toa Argamon LDN via PagerDuty (Q2DH0JLUWV2U3K), attributing it to hitting rate limits. Only a +1 reaction — no thread discussion or resolution noted in window. https://mahifx.slack.com/archives/C035H1VNCAD/p1785140358840599

> [open] 2026-07-24 — Third COMEX_CHI/HRP_HEDGING_CME_CHI reject-ratio recurrence: GC2 gold futures exposure limit, no follow-up
> Arun (16:36 BST) flagged a further reject-ratio alert on COMEX_CHI/HRP_HEDGING_CME_CHI: 38% (59/154 orders) rejected in 15 minutes. First reject was GCQ6 (COMEX gold futures) with reason code 104 "GC2 Futures Exposure Limit Violation: SHORT Order Quantity: 1 exceeds AvailableShortExposureQty: 0" — a different limit type than the 2026-07-23 MGC micro-gold position-limit reject, but same recurring pattern on this hedger. No thread replies or resolution noted. https://mahifx.slack.com/archives/C035H1VNCAD/p1784907369531299

> [open] 2026-07-23 — External reject alert recurs on COMEX_CHI TOA-ARG CHI: PD fired again in the evening, no detail added
> A second PagerDuty alert (Q35436RM6IKFR9) fired for external rejects on COMEX_CHI at Toa Args CHI, 17:55 BST — no message detail or thread beyond the PD notification. Likely a recurrence of the same morning's HRP_HEDGING_CME_CHI position-limit reject-ratio issue (see entry below); not confirmed. https://mahifx.slack.com/archives/C035H1VNCAD/p1784825710136429

> [resolved] 2026-07-23 — hedgerHrpCME1 PnL breach on TOA-ARG CHI: restarted, back online
> Arun (14:37 BST) reported hedgerHrpCME1 down on a 24h PnL profit-limit breach (850,263 raw, PnL change -493,422). Restarted and confirmed online in the same message. Continuation of the recurring hedgerHrpCME1 PnL-limit pattern (see 2026-07-21, 2026-05-18 entries). https://mahifx.slack.com/archives/C035H1VNCAD/p1784813820185659

> [open] 2026-07-23 — COMEX_CHI/HRP_HEDGING_CME_CHI reject ratio: CME position limit hit on Account 52700F0001
> Arun (09:55 BST) flagged a 25% reject ratio (46/181 orders) on COMEX_CHI/HRP_HEDGING_CME_CHI at TOA-ARG CHI — CME rejecting with "Pre Trade Position Limit Violation" on Account 52700F0001, LONG limit 500 contracts for product MGC (micro gold). Lee suggested raising it with Argamon directly; Arun agreed, then separately flagged (10:39 BST) a possible misconfiguration on Mahi's side, linking an external Argamon-channel message, but thought it unlikely. No resolution confirmed in window. https://mahifx.slack.com/archives/C035H1VNCAD/p1784796910360759 https://mahifx.slack.com/archives/C035H1VNCAD/p1784799548311919

> [resolved] 2026-07-22/23 — hedgerCBOE1 moved from Toa-argamon LDN to Chicago
> New ordersCboe1/hedgerCBOE1 processes stood up in Chicago (17:24 BST 2026-07-22); Lee Butts confirmed them live and the London hedgerCBOE1 book turned off (04:23 BST 2026-07-23). Closes out the LDN CBOE hedger left off since the 2026-06-10/11 overnight oscillation (see 2026-05-26 entry below). https://mahifx.slack.com/archives/C035H1VNCAD/p1784737477542119 https://mahifx.slack.com/archives/C035H1VNCAD/p1784777020413939

> [open] 2026-07-22 — PnLDropAlert on TOA-ARG LDN: HRP_CLIENTS_NET breached repeatedly through the day, no root-cause found
> Arun flagged a first HRP_CLIENTS_NET breach at 08:04 BST (-6,179 in 20 min, PnL change +2,239), then five more through the day (14:23, 14:38 ×3, 15:06, 17:32 BST) ranging -4,231 to -12,103 across the 8min/20min/1hr thresholds. Inald's 18:02 BST PD alert (Q0JW6TOZVZTDVG) was confirmed a duplicate of the same pattern and cleared. Only +1 reactions and James's "Lumpy today!" comment in thread — no root-cause investigation opened. Recurrence of the HRP_CLIENTS_NET drop pattern (see 2026-06-25, 2026-05-26 entries). https://mahifx.slack.com/archives/C035H1VNCAD/p1784703854590099 https://mahifx.slack.com/archives/C035H1VNCAD/p1784726609243179

> [resolved] 2026-07-22 — hedgerHrpCME1 down from unrealised position breach on TOA-ARG LDN: restarted
> Lee (00:54 BST) reported hedgerHrpCME1 down from an unrealised position breach; restarted (PD Q3O4AG2XRUJZDU). https://mahifx.slack.com/archives/C035H1VNCAD/p1784678064330609

> [open] 2026-07-21 — PnL drop at TOA-ARG LDN: -4,862, eyes only, no follow-up
> Inald (19:31 BST) flagged a PnL drop at TOA-ARG LDN of -4,862 via PagerDuty (Q3WD6WVC5H84HE). Only an eyes reaction — no investigation or resolution noted in window. Second HRP_CLIENTS_NET-style PnL drop within a day, alongside the 2026-07-22 08:04 entry above. https://mahifx.slack.com/archives/C035H1VNCAD/p1784658667099309

> [resolved] 2026-07-21 — hedgerHrpCME1 PnL limit bumped on TOA-ARG CHI to bring it back up
> Isaac (06:52 BST) bumped the 1-day PnL limit on hedgerHrpCME1 in CHI to get it back up. Continuation of the recurring hedgerHrpCME1 volume/PnL-limit pattern (see 2026-05-18 entry). https://mahifx.slack.com/archives/C035H1VNCAD/p1784613134154519

> [resolved] 2026-07-17 — pricerInsti2 down on Toa-argamon LDN: USDCAD PSM-W signal missing definition
> Leonardo (15:40 CEST) flagged pricerInsti2 repeatedly failing to construct on `toa-argamon-ln-trading-1` — `IllegalArgumentException: For instrument: USDCAD no definition exists for: PSM-W at index 0`. James identified a newly-introduced default on `pricing.adjustmentSignalParametersForWidening`; overrode with an empty array to fix. Process back up within 10 minutes. https://mahifx.slack.com/archives/C035H1VNCAD/p1784295651254059

> [open] 2026-07-15 — Sec-1 alerting noise needs infra fix; separate false PnL-drop alert flagged
> Shyam flagged frequent false PnL drop alerts (23:09 BST 2026-07-14), then asked (02:18 BST 2026-07-15) whether alerting tied to the intentionally-stopped `toa-apnortheast1-prod-sec-1` (PD Q1P54YYVHR2XRC, see 2026-07-04 stop entry) could be fixed or removed. Lee suggested JMX suppression as a stopgap — the proper fix needs an infra release during the IC maintenance window. https://mahifx.slack.com/archives/C035H1VNCAD/p1784078287263179 https://mahifx.slack.com/archives/C035H1VNCAD/p1784066981569519

> [resolved] 2026-07-13 — TOA-ARGAMON LDN PnL drop: hedger lagged fill on XAG down-move, missing broker rule fixed
> Shyam (01:32 BST) flagged a PnL drop on LDN — hedger struggled to get a fill on XAG on a downward price move, letting the trader profit before hedging caught up (PD Q2X4BKV1EM27NV). Lee confirmed shortly after: a XAG broker rule was missing; Elan has sorted it. https://mahifx.slack.com/archives/C035H1VNCAD/p1783902727651359

> [resolved] 2026-07-12 — Argamon CHI/LDN processes down after weekend restart: unresolved PropSignal.ZSDRaw config type
> Shyam (07:46 BST) flagged hedgerHrpCME1, hedgerHrpFxEBS1, propTrader1HrpChi1 (CHI) and hedgerHRP1, hedgerCBOE1 (LDN) down since the weekend restart. Root cause: `pricing.adjustmentSignalRegistry` referenced a signal type (`PropSignal.ZSDRaw`, the `ZSDR-12H`/`-T1`/`-T2` entries) the deployed build doesn't know — every process failed to construct with "Could not resolve type id 'PropSignal.ZSDRaw'". James redeployed by 10:03 BST — resolved. https://mahifx.slack.com/archives/C035H1VNCAD/p1783838785176749

> [resolved] 2026-07-04 — toa-apnortheast1-prod-sec-1 stopped: no longer required for Nado
> James (11:25 BST) stopped `toa-apnortheast1-prod-sec-1` as no longer required for Nado (wound down 2026-06-17). `toa-apnortheast1-prod-pri-1` continues, feeding IC Markets, rebooted in alignment with an IC Markets reboot. https://mahifx.slack.com/archives/C035H1VNCAD/p1783160733134849

> [resolved] 2026-06-29 — Booking rejects PD (Q3H4ARZS4AW58Y): test trades, no action
> James (11:09 BST) confirmed booking rejects triggering PD alert Q3H4ARZS4AW58Y are test trades — no action required. https://mahifx.slack.com/archives/C035H1VNCAD/p1782727722330439

> [resolved] 2026-06-29 — PXM_LD4_A distribution connection monitoring disabled on Toa Argamon APN1
> Maten (09:20 BST) disabled PD monitoring for the PXM_LD4_A distribution connection on Toa Argamon APN1 to reduce noise — the connection has been disconnected since the config was first added. https://mahifx.slack.com/archives/C035H1VNCAD/p1782721198480769

> [open] 2026-06-25 — PnLDropAlert on TOA-ARG LDN: HRP_CLIENTS_NET two consecutive drops, no response yet
> Arun (08:10 BST) flagged two PnL breach alerts on TOA-ARG LDN: -8,961 in 20 minutes (06:48–07:08 UTC) and -9,018 in 8 minutes (06:59–07:07 UTC), both on HRP_CLIENTS_NET. Only an `eyes` reaction as of window close — no investigation or intervention noted. Recurrence of the XAUUSD-driven HRP_CLIENTS_NET drop pattern (see 2026-05-26 and 2026-06-10/11 entries). https://mahifx.slack.com/archives/C035H1VNCAD/p1782371422081669

> [resolved] 2026-06-21 — CLS-OFIMB removed from registry: 13 processes down on Toa Args CHI/LDN, redeployed
> Isaac (09:02 BST) removed CLS-OFIMB from the signal registry because 13 processes were not coming back up on Toa Args CHI and LDN. propTrader1HrpLdn1 and signalProcess1 still down after the removal — Isaac noted it looked signal-versioning related; also flagged a possible duplicate feature in ML/XGBoost training in a separate message. James confirmed a redeploy was needed (11:20 BST) and completed it by 12:11 BST — CHI and LDN admin/trading confirmed OK; only propTrader1HrpLdn1 remains down (expected, per existing open entry). https://mahifx.slack.com/archives/C035H1VNCAD/p1782028930298559

> [resolved] 2026-06-15/17 — Nado fully wound down: traders/order processes stopped
> James announced 2026-06-15 12:49 BST that Nado was "wrapping up, positions now being unwound and we will switch off this weekend". NLP switched to Close Only 09:12 BST same day. 2026-06-17 17:59 BST James confirmed in `internal-toa-ops`: "Nado flat - traders/order processes stopped". During close-out, a Nado-side incident occurred on USDC spot (see entry below). USDC position fully closed 2026-06-17. https://mahifx.slack.com/archives/C035H1VNCAD/p1781715548.624489

> [resolved] 2026-06-17 — USDC close-out exploited during Nado wind-down: position now closed
> Nado (unidentified ops contact) flagged in `toa-nado-shared` 16:35 BST that NLP Pool 1 had sent a large volume of USDC sell orders at ~$0.90 (10% discount) — ~$400K notional. James explained: MM was set to join the ToB offer to close long USDC position, someone cleared the bids and walked the ToB offer down to exploit this, then began hitting Mahi's passive offer. James confirmed this was not Mahi-initiated manipulation — Mahi was 100% passive. USDC position fully closed by 16:41 BST; Mahi will not post again in this contract. Incident images shared by James. https://mahifx.slack.com/archives/C09RGU1T1GE/p1781710547126509

> [resolved] 2026-06-15 — Position mismatch PD Q1GOE30M5EZ0L3: 15,024 USD, JMX-resolved
> Inald flagged PD alert Q1GOE30M5EZ0L3 at 09:35 BST (15,024 USD mismatch). Resolved by Inald via JMX adjustments on exchangeAccounting by 09:40 BST — self-contained, no further follow-up. https://mahifx.slack.com/archives/C035H1VNCAD/p1781512502031929

> [resolved] 2026-06-14 — TOA CHI disk at 99%: partition expanded by Lee
> Shyam flagged (08:08 BST) disk space at 99% on TOA CHI. Lee gave the partition more disk by 08:16 BST — resolved. https://mahifx.slack.com/archives/C035H1VNCAD/p1781420916036159

> [resolved] 2026-06-11/14/21 — signalProcess NPE on tenant profile rename: resolved by redeploy, recurring pattern
> James flagged (14:36 BST 2026-06-11) that the CHI signal process had been down again for ~2 hours (PD Q0CHFO1JC1E7FN). Root cause: `NullPointerException: No classification store for HRP - available: [HRP-MM, NATWEST-M, HRP-PROP]` — renaming a tenant profile takes out models. Liam confirmed NPE-safe version not applied everywhere. James fixed CHI and asked Cameron to flag further alerts. 2026-06-14 22:29 BST: signalProcess1 crash-looping on toa-argamon-ln with the same NPE (PD Q18NGRWKYCWN6Q). Lee added a tenant profile for HRP-MM via Compass (https://toa-argamon-ln-admin-1.w8et.prod.toalabs.xyz:8400/configuration/edit/multiTenant.compassTenantProfiles/042dphabx9dzm) and confirmed running again at 22:37 BST. 2026-06-21 09:02 BST: Isaac removed CLS-OFIMB from registry (13 processes not coming back up on Toa Args CHI/LDN); signalProcess1 among those down — flagged as signal-versioning related. James redeployed ~12:11 BST; confirmed CHI and LDN sorted. Only propTrader1HrpLdn1 still down (expected — see 2026-06-02 entry). NPE-safe version still not universally applied — same issue will recur on further tenant profile renames. https://mahifx.slack.com/archives/C035H1VNCAD/p1782028930298559

> [resolved] 2026-06-10/11 — HRP_CLIENTS_NET 50k drop + hedger oscillation overnight: CBOE hedger turned off
> Nathan flagged HRP_CLIENTS_NET dropped ~50k at 23:33 BST 2026-06-10 — hedgers tripped PnL firewall and were turned off. Lee restarted hedger (~23:42 BST, PD Q170LHEGM93L3S; also Q0NUIYV443BS3H). Further oscillation: Daria noted -$2000/M in 10s (~01:40 BST); Lee found CME+CBOE hedgers trading back and forth far beyond client vol. Root cause: Elan (Nado-side) had been changing spread config. Lee turned off the CBOE hedger, kept CME on (~01:43–01:54 BST). Lee performed manual PnL adjustment back down at ~04:43 BST. Nathan acknowledged missing the hedger-down PD alert (saw prior PnL drop notification and mistook the new one for a reversion). https://mahifx.slack.com/archives/C035H1VNCAD/p1781131334130099

> [resolved] 2026-06-09 — hedgerHrpCME1 PnL breach on toa-argamon-ch-trading-1: hedge fluctuation, restarted
> Cameron paged PnL breach on hedgerHrpCME1 (PD Q2I20ZTM5HNOCK) at 15:51 UTC. Cameron also noted both hedgerHrpCME1 and propTrader1HrpChi1 were down on toa-argamon-ch-trading-1. James confirmed propTrader1HrpChi1 is still not configured (consistent with 2026-06-02 open entry), and that the PnL drop was hedge-side fluctuation only — matched by client-side gain. James restarted. Resolved. https://mahifx.slack.com/archives/C035H1VNCAD/p1781016700103829

> [resolved] 2026-06-09 — marketDataNado2 OOM on TOA APN: self-recovered
> Cameron posted OOM for marketDataNado2 (PD Q2XJ5CCYPGPD56) at 08:52 UTC; noted it looks to have self-recovered. No follow-up or intervention needed. +1 reaction only. https://mahifx.slack.com/archives/C035H1VNCAD/p1780991529998909

> [resolved] 2026-06-08 — CBOE new venue XAU wrong increment: self-fixed
> James flagged CBOE XAU wrong increment on the new venue via PD (Q04VWHPIFICMKE) at 11:36 UTC; posted "Should be fixed" 7 minutes later — self-resolved, no ops intervention needed. Related to the hedgerCBOE1 being brought up on Toa-argamon LDN (see 2026-05-26 entry). https://mahifx.slack.com/archives/C035H1VNCAD/p1780918597116949

> [open] 2026-06-08 — INST-34 off-market order flood on TOA-ARGAMON-LDN: orderRejectThrottle firing
> Nathan (Centroid) flagged counterparty INST-34 continuously triggering orderRejectThrottle throughout the day at TOA-ARGAMON-LDN — sending limit orders off-market, worst case 27k orders in 5 min. Lee said he'd raise with Argamon; the Argamon-side reply indicated they are discussing withholding with the client and also a Centroid solution to stop this. https://mahifx.slack.com/archives/C035H1VNCAD/p1780889725278749

> [open] 2026-06-07 — Argamon CHI+LDN processes down: gateway build mismatch + LR rule removal
> Nathan flagged processes down on argamon-chi and argamon-ldn affecting MARKETMAKING_HRP_INSTI-Channel. Maten found two root causes: (1) default counterparty LR rule had been removed during the week — restored by Maten, clientDist processes recovered; (2) a recent gateway-component deploy introduced `NoClassDefFoundError: ConnectionStatusSource` — gateway on CHI was on `20260605.090257.d35c7a44` while other components were on `20260529.164545.a4526744`. Maten rolled back the CHI gateway to the older build to recover; noted only the latest build was kept on CHI making rollback harder. propTrader1HrpChi1 also not yet configured (see entry above). Maten raised that CHI should retain more than the single latest build to allow faster rollback. https://mahifx.slack.com/archives/C035H1VNCAD/p1780814743280519

> [resolved] 2026-06-03 — marketDataCryptoDotCom1 on Toa-argamon APN1 being decommissioned
> Maten bounced marketDataCryptoDotCom1 on Toa-argamon APN1 after XETUSD crossed book; noted the crossed-book alert had been firing every hour and asked if it could be disabled via `marketdata.crossedBookAlertThresholdBps` given Crypto.com isn't in use. James confirmed it was turned off due to issues and suggested killing the gateway. Maten agreed to comment out marketDataCryptoDotCom1/ordersCryptoDotCom1 and do an infra deploy. https://mahifx.slack.com/archives/C035H1VNCAD/p1780488380763669

> [open] 2026-06-02 — propTrader1HrpChi1/propTrader1HrpLdn1 being added to Toa-argamon CHI/LDN: crash-looping on order breaches
> James posted "Adding propTraderHrp1 to toa-argamon CHI" (2026-06-02), then on 2026-06-05 switched naming to `propTrader1HrpChi1`/`propTrader1HrpLdn1`. On 2026-06-07 Nathan flagged processes down on argamon-chi and argamon-ldn due to MARKETMAKING_HRP_INSTI-Channel — Maten confirmed propTrader1HrpChi1 not yet configured, propTrader1HrpLdn1 also a factor. James said he'd set up propTrader in a few hours. On 2026-06-10 Cameron paged propTrader1HrpChi1 down on toa-argamon-ch-trading-1 (maximum order breaches, PD Q1RIF57OL9YM72) — brought it up; killed itself again and was left down. James fixed ordersCOMEX1 party filter and noted it's prop trading (not hedging) so fine to leave down for now. James also noted he will review increasing the breach limits (PD Q0D0YW82XRX02J, 13:21 BST). https://mahifx.slack.com/archives/C035H1VNCAD/p1781078300294379 Still unconfigured as of 2026-07-19 — Isaac flagged propTrader1HrpLdn1 down again at Toa Args LDN; James confirmed "expected, hasn't been configured yet". https://mahifx.slack.com/archives/C035H1VNCAD/p1784454116161199

> [watching] 2026-05-29 — TradePositionLimitMonitor being set up on Toa-argamon CHI: spurious alerts to ops
> James apologised to Leo (Borsi) for alerts on Arg CHI caused by TradePositionLimitMonitor being brought up. A clientDistributionGateway1 restart was also requested on 2026-05-27 (via #eod-restarts) to add a new channel to toa-argamon-ch-trading-1. https://mahifx.slack.com/archives/C035H1VNCAD/p1780070176002959

> [open] 2026-05-26 — PnLDropAlert on Toa-argamon LDN: HRP_CLIENTS_NET down ~8.2k in 20 min, XAUUSD main contributor
> Maten flagged a PnLDropAlert at 11:39 UTC: `HRP_CLIENTS_NET` fell -8,185 in 20 minutes (threshold -5,000/20min). Maten attributed it to XAUUSD in the follow-up. No intervention or resolution noted in thread. Related book to the hedgerHrpCME1 volume-breach pattern (see 2026-05-18 entry). https://mahifx.slack.com/archives/C035H1VNCAD/p1779795816962169

> [resolved] 2026-05-26 — hedgerCBOE1 being added to Toa-argamon LDN: turned off after overnight oscillation, moved to Chicago
> James announced adding hedgerCBOE1 to the Toa-argamon LDN instance; asked ops to ignore alerts during setup. 2026-05-29: still being set up, likely down on weekend checks. 2026-06-10/11: overnight CBOE+CME hedger oscillation incident (see entry above) — Lee found the two hedgers trading back and forth beyond client vol, attributed to Nado-side spread config changes by Elan. Lee turned the CBOE hedger off and kept CME on pending investigation. Closed out 2026-07-22/23: new ordersCboe1/hedgerCBOE1 processes stood up in Chicago instead; Lee confirmed them live and the London hedgerCBOE1 book turned off (see 2026-07-22 entry below). https://mahifx.slack.com/archives/C035H1VNCAD/p1779805776124319

> [resolved] 2026-05-22 — Stork Oracle API token requested and provided (toa-nado-shared)
> Nado asked if Mahi could get a Stork Oracle API token. Lee/James provided it promptly; Nado specified to use `stork-fast`. An oracle.yaml config file was shared in-thread. Likely preparatory for the Chaos→Stork oracle migration scheduled Thursday 22:30 UTC. https://mahifx.slack.com/archives/C09RGU1T1GE/p1779414775390839

> [watching] 2026-05-22 — Nado extended maintenance + Chaos→Stork oracle migration announced for Thu
> Weekly Nado maintenance at 22:30 UTC ran extended; Lee noted via their API Telegram channel that this Thursday's maintenance window (22:30 UTC) will include a 2-hour oracle migration: all crypto perp markets moving from Chaos to Stork. Shyam restarted Nado processes; all up by 01:47 UTC except marketDataGeneral2 (low concern per prior pattern — propTrader2 on SEC is off). Shyam set a reminder to perform restarts at 12:30 UTC Thursday. https://mahifx.slack.com/archives/C035H1VNCAD/p1779402945681989

> [resolved] 2026-05-21 — Nado fill-message gap causing position-rec mismatches on APN1 PRI/SEC
> Mahi noticed internal positions drifting from exchange from ~18:00 UTC; MONUST-PERP largest mismatch ~$52.8k, also SOLUSD-PERP, XBTUST-PERP, XETUST-PERP, ZECUST-PERP. Maten applied JMX adjustments multiple times (both PRI and SEC); Lee turned off trader and bounced GW — mismatches reoccurred. Lee confirmed no changes on Mahi side; checked with Nado and confirmed it was a Nado-side issue. Resolved ~20:29 UTC after Nado fixed their end. https://mahifx.slack.com/archives/C035H1VNCAD/p1779387149498799

> [resolved] 2026-05-11 — marketDataCboe1 down on TOA Argamon CHI: new process, resolved in ~33 min
> Inald flagged marketDataCboe1 down on TOA Argamon CHI (16:55 UTC). James replied it was a new process he was adding. Inald resolved the ordersCboe alert independently; James confirmed the process was up by 17:29 UTC. https://mahifx.slack.com/archives/C035H1VNCAD/p1778514939388589

> [open] 2026-05-08 — RWA posting cut to close-only on Nado: NLP hedging constraint, crypto majors/spot unaffected
> Kento (Nado-side) flagged EURUSD book 1% wide at 04:33 UTC 2026-05-08. Lee loosened the FX max risk limit to allow one-sided quoting. Nado clarified RWA depth was deliberately cut the prior week because NLP cannot hedge risk without DMM liquidity. 2026-05-30: James posted in the same thread that RWAs have now been cut entirely to close-only posting ("as agreed yesterday"), with crypto majors/spot continuing as normal. "Yesterday" = ~2026-05-29 (offline discussion). https://mahifx.slack.com/archives/C09RGU1T1GE/p1780139427944659

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

> [resolved] 2026-05-04 — noRecentOpenOrders PD on APN1: XETUST-PERP, XBTUST-PERP, SOLUST-PERP
> Three Nado instruments fired `noRecentOpenOrders` PD alerts on TOA APN1 following a reboot. James confirmed processes looked live; Leo verified all procs up on both boxes; resolved within 6 minutes of the alert. https://mahifx.slack.com/archives/C035H1VNCAD/p1777904442214679

> [resolved] 2026-03-26 — traderNado1 crash loop on FX perp launch day; stabilised on code version 26.3
> FX perps (XXXUSD-PERP format) went live on Nado mainnet 2026-03-26. traderNado1 on PRI crashed repeatedly ("Exceeded maximum number of order breaches (0): [NADO new order confirmation timed out]") — Leo/ops bouncing it every 10–15 min. Lee and James investigated: PRI rolled forward to 26.3 (fix: da20e247); SEC rolled back to 25.4 with a backported FX perp fix (d17402d6). PRI stable on 26.3 after ~1 hr. Firewall change also needed for 26.3 (a7783ffb, deployed 2026-04-02). Stuck-order risk during WS response-channel failures flagged by James — ordersNado1/2 bounce on startup sends cancel-all. https://mahifx.slack.com/archives/C035H1VNCAD/p1774549995951549

> [resolved] 2026-04-23 — traderBinance1 crash loop on Argamon APN1: config issue, stabilised
> traderBinance1 kept crashing on toa-apnortheast1-prod-argamon-1. Leo tried bouncing ordersBinanceFutures1 without success; James not available (Noey bedtime). Stable after Leo applied config changes and bounced ordersBinanceFutures1 again later in the evening. https://mahifx.slack.com/archives/C035H1VNCAD/p1776966508050719

> [watching] 2026-04-30 — FIELD_VALIDATION_ERROR rejects on APN PRI: TOO_SMALL quantity and maximumShowQuantity
> Maten reported a wave of rejects from Nado on toa-apnortheast1-prod-pri-1: `FIELD_VALIDATION_ERROR: {quantity=TOO_SMALL, maximumShowQuantity=TOO_SMALL}`. No follow-up resolution seen in the window — likely a Nado-side min-size change on a perp instrument requiring config update on Mahi side. https://mahifx.slack.com/archives/C035H1VNCAD/p1777559946762319

> [resolved] 2026-05-01 — EURUSD-PERP SLA alert: one-sided open orders, no action taken
> Maten flagged EURUSD-PERP had only one-sided open orders on TOA APN1, triggering an SLA alert (PD Q2BXAKEQGDST1L). No restart or intervention noted — consistent with FX perp behaviour at market close / expected gap. https://mahifx.slack.com/archives/C035H1VNCAD/p1777662669701519

> [resolved] 2026-02-23 — Replace workflow (cancel-and-place) deployed to mainnet
> Lee deployed replace workflow on Nado mainnet 2026-02-23 after the `remaining_qty` field question was escalated. Latency improved substantially by 2026-03-05/06 — p95 much better post Nado BE changes; TCP retransmissions still unresolved, max latency occasionally 500ms+. Nado confirmed further improvements coming. https://mahifx.slack.com/archives/C09RGU1T1GE/p1771853944369159

> [resolved] 2026-03-17 to 2026-03-31 — FX perps + Silver + ETF pricing rollout on Nado
> Silver (XAG) went live 2026-03-17 after network/system issues. FX perps (XXXUSD-PERP format) live on Nado mainnet 2026-03-26 in post-only mode; FX price feed report shared with notes on JPY divergence vs Hyperliquid. ETF pricing (QQQ/SPY) live 2026-03-31; opened for trading 2026-04-02. Oil/CL listed ~2026-03-24. Chaos oracle price weighting change (Tiingo:1/Finnhub:1/Nobi:2) applied 2026-03-25. https://mahifx.slack.com/archives/C09RGU1T1GE/p1774964941888099

> [resolved] 2026-05-13 — starfishFilePersisterExternalMarketData down in LDN: signals missing from Pulse
> Daria noticed last data in Pulse was from the same day as a prior restart; no suspicious config changes. Restarted starfishFilePersisterExternalMarketData in LDN and signals came back. No source to backfill the gap. https://mahifx.slack.com/archives/C035H1VNCAD/p1778639825.532889

> [open] 2026-05-14 — pricerRetailPremium1/2 not starting on Toa-Argamon CHI: no instruments configured
> James added new Toa-Argamon CHI model pricerRetailPremium1/2. As of 2026-05-17 the processes were not starting due to no instruments configured; Lee said they're new and still being set up. https://mahifx.slack.com/archives/C035H1VNCAD/p1778780018.368259

> [open] 2026-05-15 — HRP-DIRECT GMG logon rejections on Toa-Argamon LDN: wrong credentials
> Arun flagged `HRP-DIRECT_GMGPrices` and `HRP-DIRECT_GMGOrders` rejected logons on `toa-argamon-ln-trading-1: clientDistributionGateway1` — invalid username/password. James confirmed GMG put credentials the wrong way round; waiting for them to fix. https://mahifx.slack.com/archives/C035H1VNCAD/p1778834376.137359

> [resolved] 2026-05-17 — FX hedging delay alert on Nado: alert disabled (market too illiquid)
> Shyam flagged Nado FX hedging delay PD alerts. James confirmed FX market too illiquid to hedge; disabled that alert and backed it off to 12h. https://mahifx.slack.com/archives/C035H1VNCAD/p1779056029.757649

> [open] 2026-05-18 — hedgerHrpCME1 volume breach + firewall shutdown hang on TOA-ARG-CHI
> Volume breach alert on `hedgerHrpCME1` (TOA-ARG-CHI): 1.01E8 in 1 hour against 1E8 limit. PnL breach alerts followed (-6,557 in 8 min, -14,472 in 1 hr on HRP_CLIENTS_NET). James restarted hedgerHrpCME1. Arun noted repeat volume and PnL breach alerts on 2026-05-19. James confirmed the volume limit was raised; also surfaced a shutdown-hang bug: firewall tripped at 13:58:11 but process didn't come down until 14:09:15 (~10 min out of market, lost money). https://mahifx.slack.com/archives/C035H1VNCAD/p1779118383.172819

> [resolved] 2026-05-19 — marketDataGeneral2 on TOA APN1 SEC stuck in failed-subscription state
> Weekly PRI reboot at 22:30 UTC cleared the issue on PRI; SEC remained stuck post-reboot. Shyam flagged it; James confirmed SEC's propTrader2 is off so not a major concern. https://mahifx.slack.com/archives/C035H1VNCAD/p1779145326.334939

> [resolved] 2026-05-19 — paidGivenProfileProcess down on toa-argamon-ch-trading-1
> Shyam flagged PD alert for paidGivenProfileProcess down. Lee confirmed it crashed (not expected). Shyam restarted it successfully; process came back up. https://mahifx.slack.com/archives/C035H1VNCAD/p1779228759.119069

## Notable topics

- **2026-06-21 — CLS-OFIMB signal removed; ML/XGBoost duplicate feature flagged**: Isaac removed CLS-OFIMB from the Toa Args signal registry to recover 13 downed processes. In a separate message Isaac noted a possible duplicate feature on the ML/XGBoost training — no thread or follow-up; context sparse. https://mahifx.slack.com/archives/C035H1VNCAD/p1782028966717029
- **2026-07-21 — marketDataTT2 stopped on TOA CHI (v25.2 options MD bug)**: Lee stopped the process pending a fix — no ETA, currently blocking options MD on CHI. https://mahifx.slack.com/archives/C035H1VNCAD/p1753075908322289
- **2026-07-16 — Vertex fully closed; toa-crypto-1 AWS box shut down**: Vertex exchange formally closed. James turned off traderVertex1 and terminated the `toa-apnortheast1-prod-crypto-1` AWS instance. Vertex had been briefly reactivated 2026-07-09 to assist with their shutdown sequence (they begged for MM help). https://mahifx.slack.com/archives/C035H1VNCAD/p1752175088390839
- **2026-07-10/18 — CVEX recurring crash (500 unknown on replace): CVEX fixing their end ~week of 2026-07-21**: Mahi's code fix (e60cf03) handles the duplicate-cancel path but cannot handle CVEX returning HTTP 500 unknown on a replace (can't know if old or new order is live). CVEX acknowledged and said they're releasing a fix the following week. https://mahifx.slack.com/archives/C035H1VNCAD/p1752166120327089
- **2026-07-10 — Wintermute→Toa BTC position move**: Isaac Dann raised ~9 BTC at Wintermute with opposite positions at Toa; Lee said manual trades fine, up to 1 BTC at a time. Ad hoc position management between venues. https://mahifx.slack.com/archives/C035H1VNCAD/p1752103790390549
- **2026-07-03 — High VaR / Argamon dashboard confusion**: Justin panicked at ~500k VaR reading on the Argamon dashboard; James confirmed it was gross (client + hedging exposure), net hedged. Surfaced that the dashboard doesn't show net position clearly. James uses Grafana; multi-book dashboard improvement flagged by Justin. https://mahifx.slack.com/archives/C035H1VNCAD/p1751552745129849
- **2026-06-26 — Argamon Tokyo relaunched on minor coins**: After being in setup/maintenance mode, Lee confirmed Toa Argamon Tokyo live again. https://mahifx.slack.com/archives/C035H1VNCAD/p1750927682432399
- **2026-06-16 — GBPUSD arb on Argamon LDN: Elan suggests MWMS+BMSL timezone stack**: Daria relayed (23:35 BST) that Elan (Nado-side) messaged about GBPUSD arb on Toa-Argamon LDN — suggesting adding timezone MWMS in addition to BMSL rather than reducing the sampling on BMSL, to get spreads to widen faster. Post-Nado-wind-down engagement on Argamon LDN spread config. https://mahifx.slack.com/archives/C035H1VNCAD/p1781649328090949
- **2026-06-15 — Nado wind-down confirmed**: James posted in `internal-toa-ops` that Nado is "wrapping up", positions are being unwound, and the switch-off is planned for this weekend. In `toa-nado-shared` earlier the same morning, James confirmed NLP has been switched to Close Only "as agreed". This supersedes all prior "live and expanding" status. https://mahifx.slack.com/archives/C035H1VNCAD/p1781524142261449
- **2026-06-09 — Nado FX markets empty confirmed as intentional RWA cut**: Nado asked James in `toa-nado-shared` why FX markets were basically empty. James confirmed RWAs have been cut to close-only as agreed with Zach — consistent with the 2026-05-08 open entry. No new development work or reversal indicated. https://mahifx.slack.com/archives/C09RGU1T1GE/p1781015707695679
- **2026-06-05 — Nado xstock spot launch request refused pending renegotiation**: Nado asked James in `toa-nado-shared` to have NLP support xstock spot launch targeting Monday 2026-06-09, saying activity would be low (mainly depth for liquidation). James refused: new development work is on hold pending renegotiation, Mahi is not in a position to support xStocks without development work, and Friday-to-Monday notice is insufficient. https://mahifx.slack.com/archives/C09RGU1T1GE/p1780661003888839
- Nado weekly maintenance window moved to 22:30 UTC Mon/Thu (was previously aligned to LDN hours); Toa reboot schedule updated to match — PRI reboots Monday 22:30 UTC, SEC reboots Thursday 22:30 UTC. Calendar reminder updated for NZ support coverage instead of LDN. https://mahifx.slack.com/archives/C035H1VNCAD/p1778185084196589
- Cameron asked whether low-urgency PD alerts requiring prompt action will get missed in the noise; James says most should drop off PD entirely as EOD telemetry. Open design question for pagerbuddy / alert routing. PD noise review (Feb 2026) showed 2064 incidents on APN1 — threshold tuning still pending.
- `--binaryLogOutputPath` for systemStateMonitor remains commented out (rolled back 2026-03-08); without it pnlDropAlerter forensics rely on slower log digs. PnlDropAlerter fix committed 2026-04-23 (c2cdb3b3) — needs release + config set before binlogs are useful again.
- CVEX recurring crash loop (replace order timeouts): CVEX breach limit is 0 (zero tolerance). Mahi partial fix e60cf03 deployed 2026-07-11; CVEX-side 500 unknown responses still causing crashes — CVEX fixing their end ~week of 2026-07-21. Lee also hit a self-match cancel loop 2026-07-15.
- High VaR alerting calibration: VaR critical threshold bumped to 50k temporarily (2026-07-02) following increased Argamon crypto flow. Threshold tuning pending; James acknowledged it needs updating. Dashboard does not clearly show net position — James uses Grafana directly.
- FIELD_VALIDATION_ERROR (`TOO_SMALL`) rejects seen 2026-04-30 — likely a Nado min-size change needing config update; unresolved in window.
- hedgerHrpCME1 shutdown-hang bug (2026-05-18): firewall tripped but process took ~10 min to come down, leaving Toa out of market and losing money. Volume limit also raised following repeated breaches. Root cause (shutdown hang) not resolved in window.
