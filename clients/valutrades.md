---
slug: valutrades
aliases: []
refs:
  vibepulse: ../VibePulse/.claude/clients/valutrades.yaml
  billing: ../MahiProduct/data/billing/clients.json     # entry: valutrades
  hosts: ../MahiProduct/data/client-hosts.json          # entry: valutrades
  wiki: ../MahiProduct/wiki/clients/valutrades.md
channels:
  internal-valutrades: CP7A1F8BT
  mahi-valutrades: CSLM3Q8AD
  mahi-valutrades-operations: C09HN93T0G2
contacts:
  - {name: "Graeme Watkins", role: "client senior decision-maker (commercial, algo/bridge strategy)", confidence: low}
  - {name: "Garry Bersnov", role: "client IT/integration — algo UAT, TT/QB, user admin", confidence: low}
  - {name: "Brandon Soo", role: "client infra — OneZero connections, LP feeds, IP whitelisting", confidence: low}
  - {name: "Andri Zamroni", role: "client trading ops — algo settings/limits, yield profiles", confidence: low}
  - {name: "Mohamad Richard", role: "client — Compass/Echo user requests", confidence: low}
  - {name: "Neil Whitehead", role: "client data/tech — backtesting, MySQL/Pulse queries (older lead)", confidence: low}
last_catchup: 2026-10-23T07:18:41Z
status: active
---

## Now
Active broker client (LDN + NYC, Beeks-hosted). Main work: algo order routing UAT through TT and QB via OneZero (tag 448 config strings), a new StoneX/Surya TT connection, and a pending bridge-to-production quote. Mahi offered ~$5k/month (Andrew Morgan, relayed 2026-10-12); client targets a 1 Jan launch with sign-off around mid-Nov. Client reported as very happy (GreySpark reference call 2026-08-26) but stopped CFD client onboarding globally (2026-09-09).

## Streams

### oz-backup-whitelist — Whitelist OneZero hub backup IPs
status: open · since: 2026-10-22 · last: 2026-10-23
State: Brandon is auditing the OneZero hubs' backup connections and asked Mahi to whitelist NY Surya hub backup 147.160.249.36 and NY Hub-Valutrades backup 147.160.249.37 towards 10.72.100.38 (MFX and MAHI_OZNY4 maker adapters, ports 9010/9011/9034/9035/9037). Maten Rehimi asked for traceroutes and whether a cross-connect is used; Brandon says it goes over the internet and posted traceroute screenshots from both IPs on 2026-10-23. Not yet whitelisted.
Next: Mahi (Maten) reviews traceroutes and whitelists.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792659558042959 https://mahifx.slack.com/archives/C09HN93T0G2/p1792736621899949

### profile-recs-creds — Programmatic access to Mahi profile recommendations
status: open · since: 2026-10-23 · last: 2026-10-23
State: Brandon asked for new credentials so the client IT team can pull the Mahi profile recommendations; he clarified they need programmatic access, i.e. DB access. Shyam Hari raised it with the dev team.
Next: Mahi dev team decides on and provides access.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792729759993029 https://mahifx.slack.com/archives/C09HN93T0G2/p1792729903877109

### lr-setting-location — Client cannot find Liquidity Reduction setting in new screen
status: open · since: 2026-10-22 · last: 2026-10-22
State: Garry also asked whether old-UI Position maps to the new Rate Limit Amount; Isaac Dann confirmed the old refresh quantity and rate are the new rate limit amount and period. Andri Zamroni asked where a setting (screenshot) now lives; Isaac Dann replied that in the new screen, selecting ICDX_MINI shows a configure channel button on the right with a Liquidity Reduction menu. No client confirmation yet.
Next: Andri confirms he found it.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792651200738679 https://mahifx.slack.com/archives/C09HN93T0G2/p1792658285372589

### ab-book-queries — A/B book classification requests from overnight team
status: open · since: 2026-07-08 · last: 2026-10-21
State: Recurring: the client overnight desk posts "please advise Ac <id>" and a Mahi analyst replies A or B book with a chart, usually within minutes. Latest 2026-10-21 (95503831: B book from Isaac Dann; 68565319 answered later the same day by Isaac Dann: small sample, looking like A book). Client also asked what the Echo yield-profile "Off Market" filter means (Daria Horton explained 2026-08-20).
Refs: https://mahifx.slack.com/archives/CSLM3Q8AD/p1783493649978839 https://mahifx.slack.com/archives/CSLM3Q8AD/p1792571194326479

### algo-uat-testing — Algo config strings via TT / QB (UAT then prod)
status: open · since: 2026-08-19 · last: 2026-10-22
State: On 2026-10-22 a UAT GoldDec algo order was left running; Liam cancelled it on request. Client has no UAT GUI access (Graeme asked if one exists), and asked if Mahi can reject rather than cancel (Liam: not possible); client can cancel prod orders via Compass open-orders X. Client sends algo params in tag 58 from OneZero, which Mahi maps to tag 448 and parses (TWAP+, POV, ScalePOV to TT; BOLT to QB). Production release done around 2026-09-18/21; QB BOLT format fixed (7 positional fields) and tests passed; no params means Mahi config is used, malformed params reject. Open UAT issues: TT ScalePOV orders show no fills and TT sees no child orders (client to raise with TT); UAT orders cancelled after 30 min by a Mahi-side UAT timeout (Liam confirmed 30 min in UAT, 35 min on the UBS Algo prod connection, none for TT/QB) and offered to disable it; QB UAT order unfilled for 30 min with nothing from QB, client raising to QB.
Next: Liam answers Graeme on a UAT GUI; client answers Liam on disabling the UAT timeout; client chases TT and QB; Mahi supplies FIX logs on request.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787128423896719 https://mahifx.slack.com/archives/C09HN93T0G2/p1792673915629229

### stonex-surya-tt — New StoneX/Surya TT connection via OneZero
status: open · since: 2026-09-15 · last: 2026-10-13
State: Mahi built fixOrdersTT4 and ttPassthroughGateway4 (NY) for market TT_MHNY4_FUND_STONEX_SURYA_FIX_OR; OneZero connected and logged on 2026-10-09. A test trade on 2026-10-13 was rejected with "TT FIX: No connection_id found for BankAlgo with providerID RCM". William Denny asked the client to check with TT whether the account is connected; client said it would.
Next: client checks with TT.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1789466674694669 https://mahifx.slack.com/archives/C09HN93T0G2/p1791889319503849

### algo-order-limits — Max order size limits on TT sessions
status: open · since: 2026-10-08 · last: 2026-10-12
State: A 3800-lot gold order was rejected by a Mahi-side per-contract max, not TT. Liam removed UAT limits on 2026-10-12. Prod limits: TT UBSPB/Phillip sessions max 500, Surya retail and StoneX sessions Gold/Oil 1e9, US100 1000. Client (Graeme) asked Andri to decide whether prod limits need changing, then Garry adds to their limits knowledge base. Mahi noted a limit change applies to all client orders on the session.
Next: client decides on prod limits.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1791450035281399 https://mahifx.slack.com/archives/C09HN93T0G2/p1791802948207999

### bridge-commercial — Bridge to production: pricing and scope
status: open · since: 2026-08-03 · last: 2026-10-12
State: Graeme asked whether bridge deployment to production is still free; internally Andrew pushed back. On 2026-10-05 Graeme described a production system: one MT5 server to Compass to 1-3 regulated LPs (e.g. ISPrime), minimum volume, as an alternative to OneZero. Andrew agreed to quote up to $5k/month (revisit if volume or terms change), Bonnie relayed it 2026-10-12; Graeme replied it is a 1 Jan launch with sign-off by mid-Nov after his Jakarta trip.
Next: client sign-off mid-Nov; Mahi to hold quote and follow up on the named update cadence for build requests.
Refs: https://mahifx.slack.com/archives/CP7A1F8BT/p1785744760869439 https://mahifx.slack.com/archives/CP7A1F8BT/p1791798007442899

### hotspot-pegged — CBOE Hotspot pegged-order integration
status: open · since: 2026-09-03 · last: 2026-10-05
State: Graeme asked whether Mahi still has a CBOE Hotspot integration (ITCH MD plus FIX orders, in active use per James Furness) and the cost to map text strings to pegged order types. Mahi uses Auto Peg set up on the venue side today; mapping on Mahi's side estimated 1-3 days. Andrew Morgan is happy to SOW; Graeme said he will come back on Hotspot.
Next: client comes back on Hotspot.
Refs: https://mahifx.slack.com/archives/CP7A1F8BT/p1788444927995509 https://mahifx.slack.com/archives/CP7A1F8BT/p1791206090832099

### contract-rolls — Futures and CFD rolls announced by client
status: watching · since: 2026-08-18 · last: 2026-10-15
State: Client posts FYIs for rolls (USOIL Oct to Nov to Dec for AMB, US100 Sep to Dec, GC Dec26 gold). Mahi acknowledges; Garry asked on 2026-08-18 whether symbol pricing switches automatically on a roll.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787042749088329 https://mahifx.slack.com/archives/C09HN93T0G2/p1792043232458789

### dashboard-stability — Compass dashboard and admin outages
status: watching · since: 2026-08-17 · last: 2026-10-05
State: Compass errors on 2026-09-20 (fix deployed by Sam Hewitt, trading unaffected), LDN dashboard login bounce fixed by a dashboard-only deploy on 2026-09-28 (NY already fixed), and a transient all-tab error on 2026-10-05 that cleared after refresh. Sam raised LDN backgroundJobs memory 2048 to 3072MB on 2026-09-01.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1789937493122649 https://mahifx.slack.com/archives/C09HN93T0G2/p1791193345574799

### overnight-reconnects — Overnight connection fixes
status: watching · since: 2026-08-18 · last: 2026-09-21
State: Overnight desk posts a screenshot ("please can you fix this for us") out of hours; Sam Hewitt or Daria Horton fix it within about 2 minutes and the client confirms (2026-08-18, 2026-08-27, 2026-09-21).
Refs: https://mahifx.slack.com/archives/CSLM3Q8AD/p1787088431402609 https://mahifx.slack.com/archives/CSLM3Q8AD/p1790025740559209

### ip-whitelist-beeks — Brandon cannot reach Compass/Echo from new IP
status: watching · since: 2026-09-08 · last: 2026-09-16
State: Client asked to whitelist 108.136.145.119 for Echo and Compass; Brandon still could not connect as of 2026-09-16, Beeks running a TCP dump. Downgraded to watching: no activity for 35d, no resolution visible.
Next: confirm with client whether access works.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1788860536902869 https://mahifx.slack.com/archives/C09HN93T0G2/p1789557438771399

### vt-lp-removal — Edge, Jump, Commerz removed from VT feed
status: closed · since: 2026-10-20 · last: 2026-10-21 · closed: 2026-10-21
State: Rory noticed no prices since Friday's close from three NWPB VT streams (Edge, Jump, Commerz) while the session stayed up; Garry confirmed on 2026-10-21 the client is removing them. Expected, no fault.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792504266802319 https://mahifx.slack.com/archives/C09HN93T0G2/p1792553324672229

### surya-hedger-blocked — Surya RM gold hedger stopped hedging
status: closed · since: 2026-10-20 · last: 2026-10-20 · closed: 2026-10-21
State: Garry reported no orders on MFX_Echo hedging since 2026-10-19. Rory King found the Surya RM hedger blocked with a small XAUUSD position (short 59.4oz) not clearing; it trades via the INSTI LP and always has. Client briefly expected the RETAIL LP; after restarting hybridHedgerRM1 with unchanged config the position cleared and Garry confirmed no LP change needed. Root cause of the block not stated.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792487283744139 https://mahifx.slack.com/archives/C09HN93T0G2/p1792494285470129

### oil-order-status — OneZero shows unfilled, Mahi shows filled
status: closed · since: 2026-10-20 · last: 2026-10-20 · closed: 2026-10-21
State: Client questioned an oil order (CLZ6, 5 lots, 2026-10-18) reported unfilled in OneZero but filled at Mahi. Liam Cordelle showed it was partially filled for 1 unit at 22:26:48, then cancelled at the client's request at 22:27:51.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792497831920379 https://mahifx.slack.com/archives/C09HN93T0G2/p1792499760182229

### qb-session-hours — fixOrdersQB1 session schedule
status: closed · since: 2026-10-05 · last: 2026-10-06 · closed: 2026-10-15
State: Client confirmed QB hours 5pm Chicago to 4pm next day (18:00-17:00 NYT). Mahi changed fixOrdersQB1 session times on 2026-10-07 (low-risk change CHG-2610-P1WP).
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1791169713201199 https://mahifx.slack.com/archives/C09HN93T0G2/p1791325982612159

### feed-lp-routing — B2Broker LP feed routing
status: closed · since: 2026-08-12 · last: 2026-10-05 · closed: 2026-10-15
State: New LPs (JT, GCEX, B2_OZNY4_RETAIL_MARGIN_VT) caused FEED4 disconnections; B2 duplicated on FEED1 and FEED4. On 2026-10-05 client confirmed B2 comes via FEED1 and Shyam Hari moved the market selector from FEED4 to FEED1.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787633651014009 https://mahifx.slack.com/archives/CP7A1F8BT/p1791230817547969

### echo-compass-users — Echo/Compass user admin
status: closed · since: 2026-09-01 · last: 2026-09-29 · closed: 2026-10-15
State: Echo user audit list and removal of 14 users (2026-09-01); new Compass and Echo account for a client analyst created 2026-09-29, credentials emailed.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1788234307503689 https://mahifx.slack.com/archives/C09HN93T0G2/p1790654563743499

### tt-stunnel-pinning — TT certificate pinning removal
status: closed · since: 2026-09-23 · last: 2026-09-23 · closed: 2026-10-15
State: Liam confirmed no Mahi impact (no stunnel/cert loading); UAT bounced and reconnected cleanly.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1790154246462319 https://mahifx.slack.com/archives/C09HN93T0G2/p1790154788215129

### beeks-hosting — Client exit from Beeks, Compass hosting move
status: closed · since: 2026-07-30 · last: 2026-07-31 · closed: 2026-10-21
State: No activity since 2026-07-31; assumed dormant (hosts still Beeks-based in October, no transfer decision seen). Graeme said the client is done with Beeks and asked whether Mahi prefers the servers transferred to Mahi's account (rebilled) or moved to a new provider. Beeks (Martyna) offered no price rise for Mahi and a monthly capacity call. No later activity seen in window; hosts still Beeks-based in October.
Refs: https://mahifx.slack.com/archives/CP7A1F8BT/p1785399649401229 https://mahifx.slack.com/archives/CP7A1F8BT/p1785496853098919

## Arc
- 2026-05-21 — Both SOWs signed: Scale POV and Quantitative Brokers (QB)
- 2026-07 — QB production session live (early July)
- 2026-07-30 — Client asks to move Compass hosting off Beeks
- 2026-08-26 — GreySpark reference call (Project Redwood): NPS 9/10, very happy to promote
- 2026-09-09 — Press report: Valutrades stops CFD client onboarding globally
- 2026-10-12 — Bridge-to-production quote (~$5k/month) relayed to Graeme; targets 1 Jan launch
