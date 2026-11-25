---
slug: toponetrader
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/toponetrader.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: toponetrader
  hosts: ../MahiProduct/data/client-hosts.json          # entry: toponetrader
  wiki: ../MahiProduct/wiki/clients/toponetrader.md
channels:
  internal-toponetrader: C08TG143F4L
  mahi-toponetraders: C08U853T684
contacts:
  - {name: "Matt Morris", role: "CEO, Top One Trader"}
  - {name: "Lars Aerts", role: "Operations / integration lead at TOT"}
  - {name: "Shane Kalichurn", role: "TOT operations; payouts reporting, harsh-execution group requests"}
  - {name: "Daniel", role: "TOT trading/risk contact; raises slippage and fill queries in mahi-toponetraders"}
  - {name: "Priojit", role: "TOT hire working closer with Compass (Jan 2026)", confidence: low}
  - {name: "Todd Hodges", role: "TOT internal contact; Compass product training Jan 2026", confidence: low}
  - {name: "Arjie", role: "MatchTrader operations contact at TOT", confidence: low}
last_catchup: 2026-11-25T08:15:39Z
status: active
---

## Now
Prop firm; Mahi is dealing desk and risk. Payouts were high last week; Cameron Hughes widened spread-table spreads (TOT no longer on Prop Firm Match) as a first step. Cameron Hughes also sent TOT an NFP value-add note (about $4.3k over the release).
Open: TOT plans a perps offering in January (Mahi to ask instruments and funding); EURUSD PSM widening was stuck on 13-17 Nov (round-numbers override applied, $/M anomaly under investigation); Matt says TOT is back to #13 on Prop Firm Match spreads; no second price source if Mahi Central eu-west-2 drops (Liam Cordelle weighing options); MatchTrader IP whitelist (Mahi to action); CADCHF 4 ms-apart fills with 1.3 pip difference (Mahi to explain); drop-copy volume check with Shane.

## Streams

### prop-perps — Prop perps request
status: open · since: 2026-09-30 · last: 2026-11-24
State: Matt first asked about prop perps (Vest Markets, MyFundedPerps) in Oct; Cameron Hughes sees a growing area. On 2026-11-24 Matt forwarded that TOT plans to roll out a perps offering in January and asked if Mahi has put energy into perpetuals. Isaac Dann said Mahi should have enough pricing around and asked which instruments; Andrew Morgan asked whether TOT plans to do funding on it. Logged on the wiki Client requests section.
Next: Cameron Hughes to ask Matt for the instrument list and whether TOT will run funding, then reply.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1790787110596799 https://mahifx.slack.com/archives/C08TG143F4L/p1795509913481269

### psm-eurusd-widening — EURUSD PSM widening stuck on
status: open · since: 2026-11-13 · last: 2026-11-17
State: Daria Horton found PSM widened EURUSD on almost every sample from 2026-11-13 ~15:00 UTC to 2026-11-17 21:20 UTC (~54 trading hours vs a normal 20-30%), caused by the `round-numbers` input to PSM-W giving 1.1000 a 50-pip approach zone while price sat inside it. A client-wide registry override (`maxTiers: 3`, 5-pip zone) went live 2026-11-17 21:20 with the signalProcessFI1 restart (XAUUSD loses its $5 zone around $100 levels); two stale 2025 rules blocking imports were fixed first. Widening stays on until EURUSD moves >5 pips from 1.1000. Widened-period yield averaged 45-53 $/M from 16 Nov vs ~20 before, more than the cap explains, so still under investigation. Daria asked Andrew Morgan to review.
Next: Daria Horton to check widened share over 2026-11-18 session and explain the $/M excess; Andrew Morgan to review.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1794951032551019

### payout-ratio-levers — Payout ratio, skew and spread levers
status: open · since: 2026-09-30 · last: 2026-11-17
State: Call with Matt and Shane on 2026-09-30: 2-Step Pro payout ratio was 47% over 6 weeks; Mahi raised skew on 1-Step and 2-Step, spreads on majors restored on Prop Firm Match, max loss 9% to 8% the agreed fallback, Shane to flag each new Launchpad group for harsher execution. Re-opened 2026-11-09: Shane told Cameron Hughes TOT payouts were high last week and they want changes in place. TOT no longer uses Prop Firm Match (same as other props), so Cameron Hughes added wider spreads on the spread-table instruments as a first step. On 2026-11-17 Matt told Cameron Hughes TOT is #13 on the Prop Firm Match spreads list and "somehow it reverted back"; William Denny said Mahi will look into it.
Next: Mahi (Cameron Hughes / William Denny) to look into the Prop Firm Match ranking; watch payouts after the wider spreads; further levers (skew, max loss) if still high.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1789027773632959 https://mahifx.slack.com/archives/C08TG143F4L/p1794238452068779 https://mahifx.slack.com/archives/C08U853T684/p1794931416547649 https://mahifx.slack.com/archives/C08U853T684/p1794931621065459

### nfp-valueadd-post — Cameron Hughes' NFP value-add note to TOT
status: open · since: 2026-11-09 · last: 2026-11-09
State: Cameron Hughes posted to TOT on 2026-11-09 about Friday's US payrolls: $32M client volume in the 3 minutes from 13:30 UTC, LR about $3.6k ($113/M vs about $5/M the hour before; gold $2.7k on $19M), PSM about $0.7k, about $4.3k total over the release, plus skew about $8.2k ($5/M) across the day. Includes a Compass yield-profile link. No client reply yet.
Refs: https://mahifx.slack.com/archives/C08U853T684/p1794239357111729

### single-price-source — No second price source if Mahi Central eu-west-2 drops
status: open · since: 2026-10-30 · last: 2026-10-30
State: Cameron Hughes flagged TOT as the one client with no fallback price source: all FX, CFD and metal reference prices come via the Mahi Central eu-west-2 proxy (XAUUSD and RTYUSD each on a single LP); only a small crypto set would survive. This is by design (TOT was told in 2025 it needed no LP alongside MT5; Match feed dropped Dec 2025; BTC/ETH failover FIX sessions sent Sep 2025 never configured). Options: TOT re-enables a platform-side LP, or Mahi adds a second Mahi Central region to TOT's reference panel. Liam Cordelle said it is on his list to think about.
Next: Liam Cordelle to decide between the two options.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1793359672712069 https://mahifx.slack.com/archives/C08TG143F4L/p1793359694612209

### matchtrader-ip-allow — MatchTrader asks Mahi to whitelist an IP
status: open · since: 2026-10-27 · last: 2026-10-27
State: Lars forwarded a MatchTrader IT Support request for Mahi to whitelist 18.132.0.59. Cameron Hughes replied that Mahi will action it on 2026-10-27; no completion message seen yet.
Next: Mahi (Cameron Hughes) to whitelist the IP and confirm to Lars.
Refs: https://mahifx.slack.com/archives/C08U853T684/p1793098034378779 https://mahifx.slack.com/archives/C08U853T684/p1793098073453029

### prop-network-showcase — Mahi to show TOT its prop-network work
status: watching · since: 2026-10-21 · last: 2026-10-21
State: The 2026-10-21 check-in call was cancelled by Shane (kept in the calendar if needed); Cameron Copland was on leave. Will Carter said Mahi will pull together what it is working on for its prop network and show TOT over the next week.
Next: Will Carter / Mahi to send the prop-network material to Shane. Watching: no follow-up seen since 2026-10-21.
Refs: https://mahifx.slack.com/archives/C08U853T684/p1792585285879989 https://mahifx.slack.com/archives/C08U853T684/p1792585333046689

### drop-copy-volume — Drop-copy volume exceeds expected volume
status: watching · since: 2026-10-15 · last: 2026-10-15
State: Cameron Hughes saw drop copies carrying much more volume than expected. Shane (TOT) thinks the extra accounts are "competition" accounts not sent to Mahi, and is double-checking.
Next: Shane to confirm whether the excess is competition accounts. Watching: no follow-up seen since 2026-10-15.
Refs: https://mahifx.slack.com/archives/C08TG143F4L/p1792053381996649 https://mahifx.slack.com/archives/C08TG143F4L/p1792053398775309

### cadchf-slippage — CADCHF second fill 1.3 pips above quoted ask
status: watching · since: 2026-10-14 · last: 2026-10-14
State: Daniel forwarded TOT's analysis: two 3-lot buys at the same price, the second filled 4 ms after the first at 1.3 pips worse than Mahi's published ask. TOT wants Mahi to explain the fill. Shyam Hari acknowledged and said Mahi will check.
Next: Mahi (Shyam Hari) to investigate and revert to Daniel. Watching: no reply seen since 2026-10-14.
Refs: https://mahifx.slack.com/archives/C08U853T684/p1791943609687779 https://mahifx.slack.com/archives/C08U853T684/p1791943843239269

## Arc
- 2026-01 — Crypto symbols (34) enabled on MatchTrader alongside MT5
- 2026-03 — Brokerage expansion discussion: TOT wants a retail brokerage on its Comoros licence with an outsourced dealing desk
- 2026-07-18 — Compass upgrade completed
- 2026-08 — TOT shut off cTrader
- 2026-09-30 — Payout-ratio call with Matt and Shane; skew increase and spread restoration agreed
