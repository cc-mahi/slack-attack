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
last_catchup: 2026-10-27T07:19:05Z
status: active
---

## Now
Pre-live but close: Argamon enabled all instruments on 2026-10-06 and Cameron Hughes finished test trading on every asset class by 2026-10-13. Waiting on David Rapp to say when they go live for real and the hedgers get turned on. Outstanding Aug/Sep invoices (24+ days overdue) are the commercial overhang; Andrew wants it handled softly, not as a go-live gate. Pricing spikiness at open/rollover is being tuned, not closed.

## Streams

### invoices-fees — Overdue invoices and additional fees
status: open · since: 2026-10-14 · last: 2026-10-14
State: Bonnie Cassidy chased again on 2026-10-14: prop and broker August invoices 24 days overdue, September due next week. Andrew asked whether go-live unlocks additional fees and asked Cameron Hughes to raise arrears with multiple ACG contacts. Cameron Hughes told Rapp he wanted the final outstanding bill paid before go-live; Andrew judged that too harsh ("I don't want to disrupt their ability to make more money") and Cameron Hughes retracted it and sent a softer nudge. Rapp replied he would sort it. Broker-side work was unfunded until fees start.
Next: Cameron Hughes to keep raising arrears with several contacts without gating go-live.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791965549448229 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791966476920889 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791972502451699

### go-live-testing — Live test trading and go-live readiness
status: open · since: 2026-04-29 · last: 2026-10-13
State: Argamon told Rapp on 2026-10-06 "I've enabled all instruments and volumes we can consider this live". Cameron Hughes ran manual, hybrid and GUI test trades (FX, metals, indices, CFDs, softs, XCUUSD, metal crosses) with hedger config tweaks (riskQuantisation, quantityDefinition, covariance matrix); all finished 2026-10-13, "systems working as expected". Hedgers are held off (startInOffState) so test trades do not reach Argamon; Argamon moved from Centroid to PXM, order and market-data connections were swapped on 2026-09-29 and PXM creds for position visibility obtained 2026-10-09. Earlier tests were slowed by the client's $1k deposit hitting NOP.
Next: David Rapp to tell Cameron Hughes when they are live for real and the hedgers need turning on.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1777462009649679 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791298835824709 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791890559871449 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791900870280529

### argamon-shared-chan — Shared Slack channel with Argamon
status: open · since: 2026-10-08 · last: 2026-10-08
State: Rapp wants a Slack group including Argamon so the LP and Mahi can resolve issues directly when he is offline. Will Carter found a broker plus LP channel unusual and asked for risks; Cameron Hughes listed risks both ways (LP detail exposed to client, Argamon hearing pricing gripes first-hand, blame triangles, versus Alpha emailing Argamon anyway) and proposed a Mahi-admined, ops-only channel. Argamon already knows Mahi talks to Alpha on Slack.
Next: Will Carter to review and reply.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791455602185639 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791456535845149

### pricing-spikes — Open and rollover price spikiness
status: open · since: 2026-09-21 · last: 2026-10-05
State: Rapp flagged spikes at market open and rollover. Cameron Hughes added a sanity check (09-21), extra benchmarkMarkets and referencePriceMarketSelectors (09-23), then on 09-29 found the fixes covered only AlphaFx, a trailing space broke the central mid yardstick, and CFDs/softs often have only Argamon live at rollover. He fixed the yardstick, added a CFD yardstick and reference feed and a sanity rule for metal crosses and XCUUSD, and started before/after backtests on the 09-25 and 09-28 rollovers. Rapp was calmer once told these are teething issues of tailored pricing. A spikiness comparison doc vs Argamon was published 2026-10-05; backtest results not yet seen in channel.
Next: Cameron Hughes to report backtest results and tell Rapp when changes are live so they can fix MT chart issues.
Refs: https://mahifx.slack.com/archives/C09FFSWHZ8W/p1790006846789019 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1790671797926079 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1790699284890299 https://mahifx.slack.com/archives/C09FFSWHZ8W/p1791215036925529

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
