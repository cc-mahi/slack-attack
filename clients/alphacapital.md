---
slug: alphacapital
refs:
  vibepulse: ../VibePulse/.claude/clients/alphacapital.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: ../MahiProduct/wiki/clients/alpha-capital-group.md
channels_override: null
key_people_overrides:
  - {name: "Gerry", role: "Analytics/risk, Alpha Capital (last name unknown)", confidence: low}
  - {name: "Jade", role: "Alpha Capital (last name and exact role unknown; raised statement of account request 2026-05-22)", confidence: low}
last_catchup: 2026-07-08T07:03:59Z
---

## Recent issues

> [open] 2026-06-30 — XAGUSD FI/skew PnL drop; skew floor lowered 2026-07-07
> Cameron Hughes flagged a drop in XAGUSD FI PnL, noting it is "very small relative to rest of the funded flow". Posted with screenshots; no thread discussion, no fix actioned. Potentially a recurrence of the Apr-23 XAG bleed pattern (signal was switched from neuron to synapse at that time). Worth monitoring whether it develops. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782821826950699)
> 2026-07-07 update — Shyam Hari: XAG skew PnL continuing to drop; min skew floor was oversized (2 pips = $0.02), lowered to [1 pip](https://alphacapital-ln-admin-1.s5e9.prod.mahimarkets.com:8400/configuration/edit/pricing.adjustmentSignalParameters/012dq42gld8avib). Flagged may need to move off the neuron signal if flow keeps picking it off. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1783393617807039)

> [watching] 2026-06-26 — False FI PnL drop on EURGBP (2026-06-25): news last-look delay interaction; FI PnL calculation methodology flagged for review
> Shyam Hari: false FI PnL drop on EURGBP at ~12:29–12:31 UTC 2026-06-25. Price was skewed up at execution *time* when House bought, but execution *price* was fine because `newsAdditionalLastLookDelay` kicked in over a news event. Root cause explained/benign, but Shyam then flagged a follow-up: "Potentially need to review which prices we use for FI PnL calculations" — open question, no action taken yet. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782445628932189) [TOB](https://echo.mahimarkets.com/topOfBook#clientId=alphacapital.LDN;from=2026-06-25T12:28:59.859Z;instrumentId=EURGBP;to=2026-06-25T12:31:01.859Z) [config](https://alphacapital-ln-admin-1.s5e9.prod.mahimarkets.com:8400/configuration/edit/distribution.liquidityThrottle.newsAdditionalLastLookDelay/012dq4frml1nmv)

> [open] 2026-06-24 — Oils instruments turned off: price spikes being arbed, very low volumes
> Cameron Hughes: bounced pricers to pick up signal params change on oils, then turned oils off due to price spikes being arbed and very low volumes. No further thread discussion. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782303349490299)

> [open] 2026-06-22 — Arber CP manually whitelisted; riskPath changed from BLACKWELL to VELOCITY; IFMS signal concern
> Shyam Hari: whitelisted a CP as an arber after it wasn't auto-detected (inception yield was positive, apparently because riskPath reference market was set to BLACKWELL which never gives a price). Changed riskPath reference market to VELOCITY (which is also the normalisation market). Also flagged that IFMS signal config may need reviewing — doesn't look like it's performing well. Screenshots posted (no further discussion yet). Zendesk ticket 23123. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782104351858689) [ticket](https://mahifx.zendesk.com/agent/tickets/23123)

> [open] 2026-06-10 — CLIENT_PRICE_LDN mass latency alerts: starfishFilePersister backpressure during tick bursts
> Cameron Copland: ~240 `distribution.marketDataLatency.CLIENT_PRICE_LDN.*` alerts fired in bursts since 11:03 UTC, recurring every ~15 min (worst ~9s staleness). LP feed latency stayed at ms-level throughout, but Aeron publish retries for CLIENT_PRICE_LDN exploded during each burst and `starfishFilePersisterExternalMarketData1` POOL-0 queue spiked from ~170 → ~26k at the same minutes (12:30 UTC = US data window). Hypothesis: persister falls behind on tick bursts and backpressures the full CLIENT_PRICE_LDN publication stream. Liam Cordelle replied: (1) check if alerts are busting through the summariser (should be low-priority — may have been changed); (2) look for allocation stalls on the box; (3) backgroundJobs may be under heavy memory pressure. No fix actioned yet. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1781100905794369) [pagerduty](https://mahifx.pagerduty.com/incidents/Q1CTD2XEHVAGWV)

> [open] 2026-06-01 — signalProcessCFDFI1 crash-loop: ADWeights counter lock (recurrence of 2026-05-15 pattern)
> Sam Hewitt: `signalProcessCFDFI1` has been crash-looping since ~2026-05-30 08:14 UTC on alphacapital-ln-trading-1. Cycle: process runs ~21 min, hangs on `ADWeights.*.counter` exclusive lock at startup, shutdown hook also hangs on same counter → SIGKILL → repeat (4/4 launches blocked). CFD CLIENT_PRICE (XAUUSD + other CFDs) cycling offline/online with spread whipsaw. Ruled out: Aeron infra (FX sibling `signalProcessFI1` stable ~41h), stale OS lock (ext4 flocks die with process; `lsof` shows no holder). Restart alone does not fix. Recommended: (1) stop wrapper to halt cycling; (2) quarantine/clear `ADWeights.*.counter` files under `…/signals/shared/var/` — resets signal weights, requires eng sign-off. Sam pinged Arun (who had the 2026-05-15 counter-lock incident). No reply yet. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1780278921326309)

> [open] 2026-05-28 — GBPUSD price spike (2026-05-27 14:20 UTC): bad Velocity ticks → TOBPN off-market → skew overamplified
> Nathan Burch: rogue price spike on GBPUSD at 14:20:13 UTC on 2026-05-27. Root cause: bad ticks from Velocity caused crossed bid/offer, which corrupted the TOBPN (top-of-book price node), causing mid formation to be off-market. SIGNPN config skews by 100% of benchmark, so the bad mid produced a disproportionately large skew magnitude. Nathan proposes reducing max skew from 10,000 pips to 2 pips — not yet actioned; awaiting further input. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1779945147921969)

> [open] 2026-05-22 — Statement of account request from Jade (Bonnie following up)
> Jade (Alpha Capital, external) posted in #mahi-alphacapitalgroup asking who to contact for a statement of account. Shyam Hari (Mahi Training) responded to Jade saying he'd sort it, and separately posted in #internal-alphacapitalgroup asking the team to create the statement / provide Jade with a contact. 2026-05-22 10:33 UTC: Bonnie Cassidy replied internally — "I'm not entirely sure what it is that she's requesting but will find out and follow up from there." No further update visible yet. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1779427327328109) [internal](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1779427896627129) [bonnie](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1779442392670229)

> [resolved] 2026-05-15 — signalProcessCFDFI1 down: counter file lock contention with signalProcessFI1
> Arun Patel: signalProcessCFDFI1 failed to start due to both FI1 and CFDFI1 contending for the same ADWeights counter file (NZDUSD IFMS). signalProcessFI1 held the exclusive lock, blocking CFDFI1. Arun had bumped `jvm_max_memory` on CFDFI1 as a prior workaround for allocation stalls; separately flagged whether some signals could be removed from signalProcessFI1/CFDFI1 to free compute and reduce downstream aeron subscriber latency spikes. Process was back up within ~1h. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778847108444079)

> [open] 2026-05-05 — XAGUSD skew abuse: arbitrageur classifier lag costing ~$35K/week
> Andrew Morgan (handover to Cameron): /skew-health-check run on alphacapital found 5 of 8 stage-c CPs inception-negative on 3–8 May (CPs: 2685507, 2696788, 2698331, 2697815, 2695337). Cohort detection-lag cost: $24.8K inception leakage across $555M volume in 5 days, ~$35K/week extrapolated. CP 2685507 alone accounts for 63% ($290M traded in single day before being caught, 4-day tag lag). 3 of 5 tagged on Qualifying FX.arbitrageurs.list (Bot wrote 2026-05-05 17:03 UTC); 2 still untagged (2696788, 2695337). Open items: (1) why offline classifier took 4 days on 2685507; (2) whether post-17:03Z trades on 2685507 route through Q1-Arbitrageurs vs Q1-Small-Tickets; (3) curation mechanism behind 13,120-CP arbitrageurs population (no arbitrageurs.badCheck configured); (4) analytics.realtimeArbDetection.* entirely unconfigured; (5) Q1-Arbitrageurs execution profile uses FORCE_INTERNALISATION + 200-300ms last-look with priceCheckThreshold: -1 (Andrew expected continuity-pool routing). Full report: docs/skew-health/alphacapital/2026-05-05-skew-health.md (commit cf26e5e). Context: Cameron Hughes had identified neuron signal as best-performing for XAG and promoted it; Andrew flagged this neuron-wins-while-all-flow-imbalance-signals-bleed pattern as a skew-abuse signature (CPs flipping positions to harvest skew, neuron lights up on reversal). Right fix is classifier auto-tagging, not signal tuning. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778009823301759)
> 2026-05-06 update — Andrew Morgan confirmed: continuity-pool fills on arbitrageur-classified flow do not apply LR (last-look/last-resort rules). Noted with grimacing reaction — no fix actioned yet. Directly addresses open item (5): the Q1-Arbitrageurs execution profile is routing via continuity pool as expected, but absence of LR is a further concern. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778057583339569)
> 2026-06-22 update — Shyam Hari manually whitelisted a further CP as an arber after auto-detection failed (BLACKWELL riskPath never prices → inception yield appeared positive). Changed riskPath to VELOCITY. See separate entry 2026-06-22 above (Zendesk #23123). IFMS signal concern also flagged in same message.

> [open] 2026-05-05 — Velocity FX BMSL spread blowouts on GBPUSD/EURUSD/USDJPY (2026-05-04 21:10 UTC)
> Cameron Hughes: spread blowouts at 21:10 on 2026-05-04 across GBPUSD, EURUSD, USDJPY; Alpha reached out about GBPUSD. Backtest confirmed spike caused by BMSL. MAHI_BENCHMARK_LDN looks firm through each event; backtesting MAHI_BENCHMARK_LDN in BMSL to verify it would have prevented the blowouts. Investigation ongoing. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1777994333748779)

> [resolved] 2026-04-23 — XAG FI PnL bleed, signal switched to synapse
> Cameron Hughes: FI PnL decreasing for 3+ days on XAG, price signal performing badly. Switched XAGUSD signal param from neuron to synapse and bounced pricers. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1776939603625359)

> [resolved] 2026-04-20 — System notification processors bounced for alert-key fix
> Inald bounced system notification processors to pick up alert-key changes, mirroring the Infinox fix. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1776682157335539)

> [open] 2026-04-07 — CLIENT_PRICE_LDN latency alerts on pager
> Inald: latency alerts firing on CLIENT_PRICE_LDN, said "will take a look when i get a chance". No follow-up visible in this window — verify whether absorbed or still active. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1775571838771069)


## Notable topics

- 2026-07-02 — Compass Bridge Operator (Restricted) access provisioned for David Rapp / FastMT on alphacap-broker instance. Justin Young created the new restricted role (alphacap-broker-ln-admin-1) in response to the long-standing FastMT markup-visibility request. Cameron Hughes approved ("Looks good I think"); Andrew Morgan: caveat it as a cut-down view and invite feedback. Cameron Hughes will also create a standard Compass account for David Rapp and ask FastMT who else needs accounts. Justin flagged the Channel Explorer rework is coming soon (embedded analytics, better UX) — suggested mentioning it on handover. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782978915962429) [follow-up](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1782992195022159)

- 2026-06-05 — Compass version upgrade scheduled for weekend of 2026-06-07/08. Liam Cordelle notified client channel that the system would be upgraded to the latest Compass version over the weekend, with Mahi monitoring the open for issues. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1780673128888239)

- 2026-05-13 — Argamon LD Centroid bridge IP migration (2026-05-16 weekend). David Rapp (Argamon) notified that the LD Centroid bridge instance was migrating servers Saturday 16 May (downtime 2100 UTC Fri–2100 UTC Sat). Clients targeting the DNS `arguk.centroidsol.com` required no action; those with hardcoded IPs needed to update to `192.109.17.170`. Forwarded to Cameron Hughes and Maten Rehimi in client channel; Cameron Hughes confirmed changes actioned. [permalink](https://mahifx.slack.com/archives/C070016ND6X/p1778658472423589)

- 2026-05-10 — clientDistributionGateway3 removal query. Nathan Burch noted the gateway does not appear to be in use and asked if it could be removed; Daria Horton tagged Cameron Hughes for a decision. No resolution visible in window. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778449279618189)

- 2026-05-07 — Compass UI: Execution Rule editor reworked for Arbitrageurs routing. Justin Young (release/26.3): (1) Recognised Arbitrageurs rules now show a plain-English banner instead of full config form (profile matched when targeting dynamically-classified arbitrageurs, routing to internal/continuity-pool, zero fees, no price improvement, last-look fills accepted regardless of price-check). Analytics invited to flag if matcher params need tightening. (2) Rules with no Arbitrageurs profile now flagged in pale orange with tooltip explaining consequence (arb-classified CPs won't route to Continuity Pool). (3) New LR P&L column in Execution Rules and Profiles tables alongside Spread and 30s P&L. A fleet-wide scan skill (for profiles missing Arbitrageurs rule) is forthcoming. Directly relevant to open XAGUSD skew-abuse issue (open item: Q1-Arbitrageurs execution profile, FORCE_INTERNALISATION + continuity-pool fills with no LR). [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1778150187657269)

- 2026-04-02 — Alpha's alpha-signals lag fleet defaults. Andrew Morgan: "the alpha signals are not currently running the best and latest stuff" — neuron/synapse eclipsed by newer signals; signal-default-registry now exists for fleet-wide rollout. Tied to the XAG switch on Apr 23. Also flagged: should auto-handle skew abusers via an ER. [permalink](https://mahifx.slack.com/archives/C06UHTDQ8JF/p1775126095434959)

