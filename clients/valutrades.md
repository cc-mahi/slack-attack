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
last_catchup: 2026-11-11T08:13:38Z
status: active
---

## Now
Client has moved to its Indonesia entity PT Surya Anugrah Mulya (2026-11-01), with new contact addresses.
Active broker client (LDN + NYC, Beeks-hosted). Main work: algo order routing UAT through TT and QB via OneZero (tag 448 config strings), a new StoneX/Surya TT connection, and a pending bridge-to-production quote. Mahi offered ~$5k/month (Andrew Morgan, relayed 2026-10-12); client targets a 1 Jan launch with sign-off around mid-Nov. Client reported as very happy (GreySpark reference call 2026-08-26) but stopped CFD client onboarding globally (2026-09-09).

## Streams

### ab-book-queries — A/B book classification requests from overnight team
status: open · since: 2026-07-08 · last: 2026-11-10
State: Recurring: the client overnight desk posts "please advise Ac <id>" and a Mahi analyst replies A or B book with a chart, usually within minutes. Latest 2026-11-10 (69542274: trending B book over recent months, recent PnL dip to watch, Rory King, answered in 17 min); before that 2026-10-23 (92007741: A book, worth watching; 69011847: A book, both William Denny); before that 2026-10-21 (95503831: B book from Isaac Dann; 68565319 answered later the same day by Isaac Dann: small sample, looking like A book). Client also asked what the Echo yield-profile "Off Market" filter means (Daria Horton explained 2026-08-20).
Refs: https://mahifx.slack.com/archives/CSLM3Q8AD/p1783493649978839 https://mahifx.slack.com/archives/CSLM3Q8AD/p1794297052376269

### algo-uat-testing — Algo config strings via TT / QB (UAT then prod)
status: open · since: 2026-08-19 · last: 2026-11-08
State: On 2026-11-08 Garry told Mahi the client will send algo parameters from its side on 2026-11-09 and asked whether the algo parameter service is ready in Production; Graeme added that parameters already flow from OneZero to Mahi, the OneZero side needs amending, and the client will keep the current OneZero default for market open and change it on Monday. No Mahi reply yet. On 2026-11-03 Andri asked why a UAT order was cancelled; Rory King found TT's algo engine stopped it ("RCM-X: excessive child rejects") and asked the client to raise it with TT with the order ID. On 2026-10-22 a UAT GoldDec algo order was left running; Liam cancelled it on request. Client has no UAT GUI access (Graeme asked if one exists), and asked if Mahi can reject rather than cancel (Liam: not possible); client can cancel prod orders via Compass open-orders X. Client sends algo params in tag 58 from OneZero, which Mahi maps to tag 448 and parses (TWAP+, POV, ScalePOV to TT; BOLT to QB). Production release done around 2026-09-18/21; QB BOLT format fixed (7 positional fields) and tests passed; no params means Mahi config is used, malformed params reject. Open UAT issues: TT ScalePOV orders show no fills and TT sees no child orders (client to raise with TT); UAT orders cancelled after 30 min by a Mahi-side UAT timeout (Liam confirmed 30 min in UAT, 35 min on the UBS Algo prod connection, none for TT/QB) and offered to disable it; QB UAT order unfilled for 30 min with nothing from QB, client raising to QB.
Next: Mahi confirms to Garry whether the algo parameter service is ready in Production (client sends params 2026-11-09); client raises the TT cancel with TT; Liam answers Graeme on a UAT GUI; client answers Liam on disabling the UAT timeout; client chases TT and QB; Mahi supplies FIX logs on request.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787128423896719 https://mahifx.slack.com/archives/C09HN93T0G2/p1794135431610409

### echo-compass-users — Echo/Compass user admin
status: open · since: 2026-09-01 · last: 2026-11-04
State: Re-opened. On 2026-11-04 Brandon asked for Echo and Compass credentials for a new user at the Surya entity (Slava); Daria Horton said Mahi will send them directly once created. Liam Cordelle noted on 2026-10-23 that the client has logins in the system (one named, one overnight) and offered to arrange access. On 2026-10-26 Garry asked Liam to add his own email and reset the overnight password. Andri asked whether a screenshotted control is where to cancel an order in Compass; Shyam Hari confirmed. Earlier: Echo user audit and removal of 14 users (2026-09-01); new Compass and Echo account for a client analyst created 2026-09-29.
Next: Liam adds Garry's email and resets the overnight password; Mahi (Daria Horton) creates and sends Slava's Echo/Compass credentials.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1788234307503689 https://mahifx.slack.com/archives/C09HN93T0G2/p1793767610138899

### xau-mini-micro-source — Client queries source of XAUUSD mini/micro pricing
status: open · since: 2026-11-03 · last: 2026-11-03
State: On 2026-11-03 Andri Zamroni urgently asked where mini and micro (XAUUSD, XAUUSD3) pricing comes from, saying around 06:17 UTC it was higher than ISPrime (bid 3923 / ask 3922 vs 3921.9 / 3922.2 on the direct ISPrime symbol). Daria Horton found both configured to the same reference markets with only ISP_OZNY4_RETAIL_MARGIN_VT pricing, and Compass max TOB offer 06:14-06:19 was 3922.61, in line with ISPrime. Andri said the client has no other feed and will check further on their side; no Mahi fault identified.
Next: client checks their side; Mahi on request.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1793686895184259 https://mahifx.slack.com/archives/C09HN93T0G2/p1793689672004209

### surya-entity-move — Client moved to Indonesian entity PT Surya Anugrah Mulya
status: open · since: 2026-11-01 · last: 2026-11-01
State: Nicole Vivian posted on 2026-11-01 that Valutrades has moved to its Indonesia entity, PT Surya Anugrah Mulya, with new commercial and Mahi-system-support contacts on the client side (addresses in the thread). Implications for contract party, billing and the Surya TT connection are not discussed yet.
Next: Mahi to check whether the contracting/billing party and client-channel contacts need updating.
Refs: https://mahifx.slack.com/archives/CP7A1F8BT/p1793566129040399

### feed-lp-routing — LP feed routing (B2Broker, JT)
status: open · since: 2026-08-12 · last: 2026-10-28
State: Re-opened. New LPs (JT, GCEX, B2_OZNY4_RETAIL_MARGIN_VT) caused FEED4 disconnections; B2 duplicated on FEED1 and FEED4, resolved 2026-10-05 when Shyam Hari moved the market selector from FEED4 to FEED1. On 2026-10-28 Garry asked Rory what to do to add JT_OZNY4_RETAIL_MARGIN_VT given another LP shares FEED4 with JT; Shyam Hari said Mahi will check.
Next: Mahi (Shyam Hari/Rory) answers Garry on how to add the JT market.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787633651014009 https://mahifx.slack.com/archives/C09HN93T0G2/p1793168593978109

### support-channel-teams — Client asks about Microsoft Teams support channel
status: open · since: 2026-10-27 · last: 2026-10-27
State: Brandon asked whether Mahi supports Microsoft Teams for support because of a client compliance requirement to possibly switch platforms. Shyam Hari replied Mahi does not support Teams and prefers Slack or email, and asked for more detail on the requirement to take back to the team. No client reply yet.
Next: Brandon shares the compliance detail; Mahi decides whether to accommodate.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1793071670570599 https://mahifx.slack.com/archives/C09HN93T0G2/p1793072932042059

### oz-backup-whitelist — Whitelist OneZero hub backup IPs
status: open · since: 2026-10-22 · last: 2026-10-23
State: Brandon is auditing the OneZero hubs' backup connections and asked Mahi to whitelist NY Surya hub backup 147.160.249.36 and NY Hub-Valutrades backup 147.160.249.37 towards 10.72.100.38 (MFX and MAHI_OZNY4 maker adapters, ports 9010/9011/9034/9035/9037). The connection goes over the internet, and Maten Rehimi pointed out 10.72.100.38 is private, so Brandon traced to public 192.81.111.24 from both IPs on 2026-10-23 and asked if that can be the backup. Maten asked whether the backup only connects when the primary is down and for telnet confirmation on all the flagged ports. Not yet whitelisted.
Next: Brandon answers Maten (backup behaviour, telnet to 192.81.111.24 on all ports); Mahi then whitelists.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792659558042959 https://mahifx.slack.com/archives/C09HN93T0G2/p1792746206556109

### profile-recs-creds — Programmatic access to Mahi profile recommendations
status: open · since: 2026-10-23 · last: 2026-10-23
State: Brandon asked for new credentials so the client IT team can pull the Mahi profile recommendations; he clarified they need programmatic access, i.e. DB access. Shyam Hari raised it with the dev team (2026-10-23); Brandon acknowledged.
Next: Mahi dev team decides on and provides access.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792729759993029 https://mahifx.slack.com/archives/C09HN93T0G2/p1792729903877109

### phillip-tt-removal — Remove deactivated Phillip TT connection
status: open · since: 2026-10-23 · last: 2026-10-23
State: Graeme said the client stopped using the Phillip TT connection, which Phillip appears to have deactivated, leaving an error on Compass. Liam Cordelle removed it from Mahi's side on 2026-10-23. Andri then flagged another error screenshot and Liam asked if it was that connection; Graeme asked Brandon to remove the same connection on the OneZero side too.
Next: Brandon removes it on the OneZero side.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792758756367069 https://mahifx.slack.com/archives/C09HN93T0G2/p1792776666037109

### lr-setting-location — Client cannot find Liquidity Reduction setting in new screen
status: open · since: 2026-10-22 · last: 2026-10-22
State: Garry also asked whether old-UI Position maps to the new Rate Limit Amount; Isaac Dann confirmed the old refresh quantity and rate are the new rate limit amount and period. Andri Zamroni asked where a setting (screenshot) now lives; Isaac Dann replied that in the new screen, selecting ICDX_MINI shows a configure channel button on the right with a Liquidity Reduction menu. No client confirmation yet.
Next: Andri confirms he found it.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1792651200738679 https://mahifx.slack.com/archives/C09HN93T0G2/p1792658285372589

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

### dashboard-stability — Compass dashboard and admin outages
status: watching · since: 2026-08-17 · last: 2026-11-05
State: On 2026-11-05 the overnight desk reported the NY admin trading/orders page slow to load (a filtered NQZ6 view); Shyam Hari and Daria Horton could load it fine, a refresh fixed it and the client confirmed. Earlier: Compass errors on 2026-09-20 (fix deployed by Sam Hewitt, trading unaffected), LDN dashboard login bounce fixed by a dashboard-only deploy on 2026-09-28 (NY already fixed), and a transient all-tab error on 2026-10-05 that cleared after refresh. Sam raised LDN backgroundJobs memory 2048 to 3072MB on 2026-09-01.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1789937493122649 https://mahifx.slack.com/archives/CSLM3Q8AD/p1793838767664399 https://mahifx.slack.com/archives/CSLM3Q8AD/p1793858285175349

### overnight-reconnects — Overnight connection fixes
status: watching · since: 2026-08-18 · last: 2026-10-25
State: Overnight desk posts a screenshot ("please can you fix this for us") out of hours; Sam Hewitt or Daria Horton fix it within about 2 minutes and the client confirms (2026-08-18, 2026-08-27, 2026-09-21). On 2026-10-25 Brandon asked Mahi to confirm whether a screenshotted item was an issue; Shyam Hari checked and found everything fine.
Refs: https://mahifx.slack.com/archives/CSLM3Q8AD/p1787088431402609 https://mahifx.slack.com/archives/CSLM3Q8AD/p1792962970307259

### contract-rolls — Futures and CFD rolls announced by client
status: watching · since: 2026-08-18 · last: 2026-10-15
State: Client posts FYIs for rolls (USOIL Oct to Nov to Dec for AMB, US100 Sep to Dec, GC Dec26 gold). Mahi acknowledges; Garry asked on 2026-08-18 whether symbol pricing switches automatically on a roll.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787042749088329 https://mahifx.slack.com/archives/C09HN93T0G2/p1792043232458789

### hotspot-pegged — CBOE Hotspot pegged-order integration
status: watching · since: 2026-09-03 · last: 2026-10-05
State: Graeme asked whether Mahi still has a CBOE Hotspot integration (ITCH MD plus FIX orders, in active use per James Furness) and the cost to map text strings to pegged order types. Mahi uses Auto Peg set up on the venue side today; mapping on Mahi's side estimated 1-3 days. Andrew Morgan is happy to SOW; Graeme said he will come back on Hotspot. Downgraded to watching: no activity for 31d, client has not returned.
Next: client comes back on Hotspot.
Refs: https://mahifx.slack.com/archives/CP7A1F8BT/p1788444927995509 https://mahifx.slack.com/archives/CP7A1F8BT/p1791206090832099

### ip-whitelist-beeks — Brandon cannot reach Compass/Echo from new IP
status: watching · since: 2026-09-08 · last: 2026-09-16
State: Client asked to whitelist 108.136.145.119 for Echo and Compass; Brandon still could not connect as of 2026-09-16, Beeks running a TCP dump. Downgraded to watching: no activity for 35d, no resolution visible.
Next: confirm with client whether access works.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1788860536902869 https://mahifx.slack.com/archives/C09HN93T0G2/p1789557438771399

## Arc
- 2026-05-21 — Both SOWs signed: Scale POV and Quantitative Brokers (QB)
- 2026-07 — QB production session live (early July)
- 2026-07-30 — Client asks to move Compass hosting off Beeks
- 2026-08-26 — GreySpark reference call (Project Redwood): NPS 9/10, very happy to promote
- 2026-09-09 — Press report: Valutrades stops CFD client onboarding globally
- 2026-10-12 — Bridge-to-production quote (~$5k/month) relayed to Graeme; targets 1 Jan launch
- 2026-11-01 — Valutrades moves to Indonesian entity PT Surya Anugrah Mulya; new contact details
