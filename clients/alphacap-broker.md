---
slug: alphacap-broker
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/alphacap-broker.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json
  wiki: ../MahiProduct/wiki/clients/alpha-capital-group.md
channels:
  internal-alpha-cap-broker: C09FFSWHZ8W
  mahi-alpha-cap-broker: C09F15FRTAB
contacts:
  - {name: "Gerard McConnell", role: "ACG Markets — sign-off / Prop side ops contact; queried abnormal rollover prints", confidence: low}
last_catchup: 2026-10-28T07:16:21Z
status: active
---

## Now
Going live: Alpha Broker's first live client was due 2026-10-28, so hedgers and expectedBookStatusOnTimezones come into play. Rollover and open spikes are being tuned hard (new WSS caps and widening factors on 2026-10-27; the 21:00 roll on 2026-10-28 is the first full test). Rapp wants redundancy against outages and a reliable swaps source for crosses, and Andrew said he can have redundancy. Outstanding Aug/Sep invoices remain a soft overhang.

## Streams

### redundancy-swaps — Redundancy, cross swaps and cross connect
status: open · since: 2026-10-27 · last: 2026-10-27
State: After the Beeks issue, Rapp wants redundancy against outages (asked again on the 2026-10-27 call about XC). Andrew Morgan replied "Rapp can have redundancy". Open questions from Cameron Hughes: multi-region servers and cost, whether redundancy belongs on Alpha's side, the best swaps source for crosses Argamon will not price (Rapp was swap-arbed for hundreds of thousands before), and whether a cross connect is needed (Beeks says no).
Next: Mahi to decide redundancy design and cost, swaps source and cross-connect answer for Rapp.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1793094782250149 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1793098215512009

### pricing-spikes — Open and rollover price spikiness
status: open · since: 2026-09-21 · last: 2026-10-27
State: Rapp reported on the 2026-10-27 call that many spiky candles had gone but some remained. Cameron Hughes cut cross widening factors on CLIENT_PRICE_LDN (AUDCAD 10.6 bps vs 276.7 the night before), added ARGAMON back as MWMS benchmark for Metals and AlphaCFDs, switched off XAGUSD benchmark minimum spread, re-firmed metals at 18:00:05 NY, and added WSS caps for 26 uncapped instruments (reset to about 3x LP average spread). Pricers and Beta restarted cleanly; CHFSGD added to AlphaFx. Earlier work (sanity checks, yardsticks, rollover backtests) stands.
Next: Cameron Hughes to check the 21:00 roll on 2026-10-28 with Rapp, the first full test of the new caps.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1790006846789019 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1793141646580879

### go-live-testing — Live test trading and go-live readiness
status: open · since: 2026-04-29 · last: 2026-10-27
State: Alpha's first live client was due 2026-10-28 (per the 2026-10-27 call). Argamon told Rapp on 2026-10-06 "I've enabled all instruments and volumes we can consider this live". Cameron Hughes ran manual, hybrid and GUI test trades (FX, metals, indices, CFDs, softs, XCUUSD, metal crosses) with hedger config tweaks (riskQuantisation, quantityDefinition, covariance matrix); all finished 2026-10-13, "systems working as expected". Hedgers are held off (startInOffState) so test trades do not reach Argamon; Argamon moved from Centroid to PXM, order and market-data connections were swapped on 2026-09-29 and PXM creds for position visibility obtained 2026-10-09. Earlier tests were slowed by the client's $1k deposit hitting NOP.
Next: Cameron Hughes to turn hedgers on and re-check monitoring once the first live client trades.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777462009649679 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791900870280529 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1793094782250149

### invoices-fees — Overdue invoices and additional fees
status: open · since: 2026-10-14 · last: 2026-10-14
State: Bonnie Cassidy chased again on 2026-10-14: prop and broker August invoices 24 days overdue, September due next week. Andrew asked whether go-live unlocks additional fees and asked Cameron Hughes to raise arrears with multiple ACG contacts. Cameron Hughes told Rapp he wanted the final outstanding bill paid before go-live; Andrew judged that too harsh ("I don't want to disrupt their ability to make more money") and Cameron Hughes retracted it and sent a softer nudge. Rapp replied he would sort it. Broker-side work was unfunded until fees start.
Next: Cameron Hughes to keep raising arrears with several contacts without gating go-live.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791965549448229 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791966476920889 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791972502451699

### argamon-shared-chan — Shared Slack channel with Argamon
status: open · since: 2026-10-08 · last: 2026-10-08
State: Rapp wants a Slack group including Argamon so the LP and Mahi can resolve issues directly when he is offline. Will Carter found a broker plus LP channel unusual and asked for risks; Cameron Hughes listed risks both ways (LP detail exposed to client, Argamon hearing pricing gripes first-hand, blame triangles, versus Alpha emailing Argamon anyway) and proposed a Mahi-admined, ops-only channel. Argamon already knows Mahi talks to Alpha on Slack.
Next: Will Carter to review and reply.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791455602185639 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791456535845149

### alert-suppression — Monitoring noise before hedgers go on
status: watching · since: 2026-08-17 · last: 2026-09-10
State: expectedBookStatusOnTimezones was set empty on 2026-08-17 to stop false alerts while hedgers are off and must be switched back on at go-live. On 2026-09-10 a PagerDuty alert for the SYNAPSE_MT5_B and backup sessions was a stopped Windows service on the backup MT5 trade server; Maten restarted it.
Next: Cameron Hughes to re-enable expectedBookStatusOnTimezones when hedgers go on.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1786998729725629 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1789031144504449

### retail-lpoa-groups — MT5 groups for retail-under-corporate accounts
status: watching · since: 2026-08-24 · last: 2026-09-03
State: fastMT had not replied (as of 2026-08-24) on trading accounts and counterparty tags. Rapp said (09-02) some corporate-name accounts have retail clients trading under an LPOA, coming from the prop side, and must be treated as retail; George says Mahi holds profiles per prop trader. Cameron Hughes asked Rapp to create MT5 groups for both cases and plans execution tailoring per trading account; exact classification may be hard if counterparty tags do not carry over. No outcome seen since.
Next: Rapp and fastMT to confirm MT5 groups; Cameron Hughes to match prop profiles to live accounts.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1787584267363759 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1788421751250899

### tick-data-feed — Tick-level CFD data for ACG risk tool
status: closed · since: 2026-07-17 · last: 2026-07-17 · closed: 2026-10-19
State: Rapp wanted historical and live tick-by-tick CFD data for a client-facing analytics tool; Liam Cordelle proposed an S3 Parquet backfill and a new FIX connection for live. No activity since 2026-07-17; assumed dropped.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1784280180924189 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1784281130919229

### instrument-coverage — Argamon symbol coverage and subscriptions
status: closed · since: 2026-04-29 · last: 2026-10-12 · closed: 2026-10-15
State: Resolved. Phased gaps (FX, commodities, crypto, softs, XCUUSD) were closed through pricer bounces and subscription mapping changes; Argamon enabled all instruments on 2026-10-06 and the final XCUUSD mapping and quantityDefinition (Argamon minimum 100oz) landed 2026-10-12, with test trades done.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777538204659809 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791800338181079

## Arc
- 2026-04-16 — MT5 group/symbol plan signed off by Rapp and Gerard McConnell; test trades succeeded 2026-04-17.
- 2026-04-24 — Spread/commission/markup file V5.4 signed off by Rapp.
- 2026-04-27 — Account manager handoff from Maten back to Cameron Hughes for setup work.
- 2026-10-06 — Argamon enabled all instruments and volumes; live test trading began.
- 2026-10-13 — Test trading finished across all asset classes; awaiting client go-live.
- 2026-10-28 — First live client expected (per 2026-10-27 call).
