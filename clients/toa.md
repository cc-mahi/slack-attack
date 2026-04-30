---
slug: toa
refs:
  vibepulse: ../VibePulse/.claude/clients/toa.yaml
  billing: null
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toa
  wiki: null
channels_override: null
key_people_overrides:
  - {name: "James", role: "primary engineer (Mahi-side)"}
last_catchup: 2026-04-30T12:00:00Z
---

## Status

- **Stage:** live (Toa sister company; Nado perpetual products quoting on APN1 since 2026-03-31; Mag7 perps (MSFT/NVDA/AAPL/AMZN/TSLA/META/GOOGL-UST-PERP) added 2026-04-08)
- **Integration:** Mahi infra hosting Toa's pricing/distribution across APN1, CHI, EUW2, USE2; CHAOS_ORACLE quoting ETF prices, CFD feeds weekday-only. Lee piloting Nado's new `/ws/v2` endpoint (testnet) for ordering — faster but out-of-order responses, replaces existing `/ws`.
- **Relationship:** sister company (same CTO); James effectively dedicated. Slack: `internal-toa-ops`, `toa-nado-shared` (cross-workspace, ink-foundation).

## Recent issues

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

> [open] 2026-04-15 — PnlDropAlerter false-positive on transient swings; fix committed, needs deploy
> Cameron raised a PnL drop alert (Argamon LDN, but the alerter is shared Toa-stack infra). James's writeup attributed it to a real ~$8.8K swing inside 2 minutes that Graphite's 60s TRADEPOSITIONPNL smoothed away — alerter not wrong, but operationally noise. systemStateMonitor `--binaryLogOutputPath` was rolled back 2026-03-08 so tick-by-tick binlogs unavailable. Fix committed 2026-04-23 (`MahiMain` c2cdb3b3) — needs release + config set. https://mahifx.slack.com/archives/C035H1VNCAD/p1776245271372289

> [open] 2026-04-29 — `/ws/v2` testnet rollout: intermittent connection-reset under load
> Nado asked Lee to pilot the new `/ws/v2` endpoint on testnet (faster, responses no longer strictly ordered across requests; per-request still atomic — would obviate IoC/PostOnly segregation per James). Lee hit `java.net.SocketException: Connection reset` running the test suite; Nado side has no error log around the timestamp and confirmed it didn't reach their gateway. Lee reproduced once on the old `/ws` URL too — likely an existing limit/proxy issue, not new to v2. Investigation continues. https://mahifx.slack.com/archives/C09RGU1T1GE/p1777450163783759

> [open] 2026-04-29 — Toa asking for NLP depth/size update post SLA reductions
> Toa-side asked James to update the shared NLP depth/size sheet given recent SLA reductions: https://docs.google.com/spreadsheets/d/1FocxIgFFc0MqDuxfi9GLWa2STdH28q0V7l6Fl0Rozm0/edit?gid=0#gid=0 . James replied in-thread; awaiting whether the sheet was actually updated. https://mahifx.slack.com/archives/C09RGU1T1GE/p1777452146937409

## Notable topics

- Cameron asked whether low-urgency PD alerts requiring prompt action will get missed in the noise; James says most should drop off PD entirely as EOD telemetry. Open design question for pagerbuddy / alert routing.
- `--binaryLogOutputPath` for systemStateMonitor remains commented out (rolled back 2026-03-08); without it pnlDropAlerter forensics rely on slower log digs. Worth tracking whether this gets re-enabled once the alerter fix lands.
