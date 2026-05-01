---
slug: alphacapital
refs:
  vibepulse: ../VibePulse/.claude/clients/alphacapital.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: ../MahiProduct/wiki/clients/alpha-capital-group.md
channels_override: null
key_people_overrides: []
last_catchup: 2026-05-01T00:00:00Z
---

## Recent issues

> [resolved] 2026-04-23 — XAG FI PnL bleed, signal switched to synapse
> Cameron Hughes: FI PnL decreasing for 3+ days on XAG, price signal performing badly. Switched XAGUSD signal param from neuron to synapse and bounced pricers. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1776939603625359)

> [resolved] 2026-04-20 — System notification processors bounced for alert-key fix
> Inald bounced system notification processors to pick up alert-key changes, mirroring the Infinox fix. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1776682157335539)

> [resolved] 2026-04-07 — CLIENT_PRICE_LDN latency alerts on pager
> Inald: latency alerts firing on CLIENT_PRICE_LDN, said "will take a look when i get a chance". No follow-up visible in this window — verify whether absorbed or still active. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1775571838771069)
> Resolved 2025-05-02: NFP-triggered latency spike (up to 4s on CLIENT_PRICE_LDN and CLIENT_PRICE_MAHI) traced to riskPathQualifying running on a non-low-latency node. Inald moved it to low-latency node 0 and infra-deployed. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1746190417423999)

> [open] 2025-05-12 — SI hedging to Argamon: new infra deployed, connectivity blocked then unblocked, live TBD
> SI processes (hybridHedgerSI1, arbHedgerSI1, fixMarketDataArgamon1, fixOrdersArgamon1) configured for FX-only hedging via Argamon/OZ (NY4). 2025-05-12: Beeks connectivity from Argamon to OZ failed, blocking test trades. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747063818928149) 2025-05-19: still blocked by Beeks; meanwhile Daria flagged riskSplit config errors causing dists and systemStateMonitor to drop on 2025-05-18 — Amir fixed and moved back to global override. 2025-05-21: OZ whitelisting still pending (separate from Beeks step which completed Mon 2025-05-19). 2025-05-22: OZ whitelisting confirmed, Argamon MD flow resolved, order connectivity tested successfully (Alpha→Argamon XAUUSD test trade verified). Hedger briefly struggled clearing risk ($4k VaR); spread predicate removed and hedger bounced. Amir declared plumbing happy. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747924833729009) George agreed to go live Tuesday 2025-05-27; 2025-05-28 Amir clarified counterparty analysis still pending before going fully live. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1747930147397559) Status: waiting on counterparty selection before live.

> [open] 2025-05-12 — DX/TradeLocker direct FIX integration (bypassing T4B bridge)
> George requested moving DX flow off T4B B-book into a direct Mahi FIX connection. DX does not send group/competition info in FIX messages via T4B, so flow cannot be split by stage. 2025-05-14 call: agreed to set up a TEMP_MIXED book (all DX+TradeLocker flow unsplit) as a short-term solution; longer-term goal is direct integration. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747239206609589) 2025-05-19: Andrew/George huddle — George bought in to Mahi bridge; sloppy TEMP_MIXED FIX creds issued to George (TempMixedOrders/TempMixedPrices). [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1747663034270589) 2025-05-21: T4B (Replicator Trade Processor) connecting and querying IP — Amir confirmed 185.212.82.54. 2025-05-27: Amir chased George on whether DX/TradeLocker would go live that day — no reply in window. 2025-05-30: George asked how to start DX direct without T4B; Amir issued separate dedicated DX FIX creds (TempDXOrders/TempDXPrices) on 2025-06-02. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1748872273132859) George said he'd organise an email chain with DX to progress; 2025-06-09 Amir chased — no update yet in window. Status: DX direct creds issued, waiting on George/DX to connect and test.

> [open] 2025-05-14 — Alpha Trader new in-house platform FIX integration
> Alpha building in-house trading platform "Alpha Trader" (separate to TradeLocker). Amir followed up with T4B Telegram group re FIX connections; Liam noted Alpha Trader may bypass T4B entirely. Andrew flagged concerns about mixing funded/challenge flow and advocated using existing direct DX bridge. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747239206609589) No further concrete next steps in window — pending Alpha Trader development completion.

> [open] 2025-06-11 — Payout data integration request
> Cameron Hughes asked George for weekly/monthly CSV exports of individual payout data for analytics/optimal config. George replied same day: Mahi already has API access (via Swarnab) to their system including payouts and account tags (stage1→qual linkage). Cameron confirmed he'd test with the API. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1749632476664279) Status: Cameron testing API integration.

> [resolved] 2025-06-06 — Open Argamon position requested closed
> George flagged an open position running with Argamon (shared screenshot). Kate Stagg confirmed position closed same day. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1749205646044129)

## Notable topics

- 2026-04-02 — Alpha's alpha-signals lag fleet defaults. Andrew Morgan: "the alpha signals are not currently running the best and latest stuff" — neuron/synapse eclipsed by newer signals; signal-default-registry now exists for fleet-wide rollout. Tied to the XAG switch on Apr 23. Also flagged: should auto-handle skew abusers via an ER. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1775126095434959)

- 2025-05-02 — New signals deployed (not yet live) ahead of NFP. Andrew: "be interesting to review performance next week on NFP". Infra deploy on 2025-05-08 to switch hedgers to new SI portfolio. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1746174594656159)

- 2025-05-05/06 — Challenge rule simulation: George's 8% pro channel is near break-even; George wants to understand why Funding Pips runs same program profitably. Cameron ran sims: 7% increase in pass rate dropping profit target 10%→8%. George requested deeper sim on 8% target with 4%/8% daily/max vs 5%/10% drawdown rules; call with Cameron on 2025-05-06. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1746203301383319)

- 2025-05-14 — Andrew Morgan flagged Alpha Capital as a "blue chip" client for world-class direct trading platform integrations. Noted they have $98T total capital under management figure, and sounded out whether Mahi could build a margin component for 150k active accounts across multiple platforms. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747238745585139)

- 2025-05-19 — George authorized Mahi to represent Alpha with TradeLocker to bash T4B on pricing. Andrew's position: use Alpha as leverage with trading platforms (DeusX/TradeLocker) to drive direct integrations and reduce platform fees. Agreed order: DX & TradeLocker first, then MT5 & cTrader. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747660857701689)

- 2025-05-20 — George requested 6m–1yr tick data (historical pricing) via S3/CSV for trade latency analysis. Liam: ~175GB for 1yr CSV, proposed S3 bucket delivery. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1747743800788239)
