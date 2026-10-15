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
last_catchup: 2026-10-15T13:08:54Z
status: active
---

## Now
Active broker client (LDN + NYC, Beeks-hosted). Main work: algo order routing UAT through TT and QB via OneZero (tag 448 config strings), a new StoneX/Surya TT connection, and a pending bridge-to-production quote. Mahi offered ~$5k/month (Andrew Morgan, relayed 2026-10-12); client targets a 1 Jan launch with sign-off around mid-Nov. Client reported as very happy (GreySpark reference call 2026-08-26) but stopped CFD client onboarding globally (2026-09-09).

## Streams

### algo-uat-testing — Algo config strings via TT / QB (UAT then prod)
status: open · since: 2026-08-19 · last: 2026-10-15
State: Client sends algo params in tag 58 from OneZero, which Mahi maps to tag 448 and parses (TWAP+, POV, ScalePOV to TT; BOLT to QB). Production release done around 2026-09-18/21; QB BOLT format fixed (7 positional fields) and tests passed; no params means Mahi config is used, malformed params reject. Open UAT issues: TT ScalePOV orders show no fills and TT sees no child orders (client to raise with TT); UAT orders cancelled after 30 min by a Mahi-side UAT timeout (Liam confirmed 30 min in UAT, 35 min on the UBS Algo prod connection, none for TT/QB) and offered to disable it; QB UAT order unfilled for 30 min with nothing from QB, client raising to QB.
Next: client answers Liam on disabling the UAT timeout; client chases TT and QB; Mahi supplies FIX logs on request.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787128423896719 https://mahifx.slack.com/archives/C09HN93T0G2/p1792069544056769

### algo-order-limits — Max order size limits on TT sessions
status: open · since: 2026-10-08 · last: 2026-10-12
State: A 3800-lot gold order was rejected by a Mahi-side per-contract max, not TT. Liam removed UAT limits on 2026-10-12. Prod limits: TT UBSPB/Phillip sessions max 500, Surya retail and StoneX sessions Gold/Oil 1e9, US100 1000. Client (Graeme) asked Andri to decide whether prod limits need changing, then Garry adds to their limits knowledge base. Mahi noted a limit change applies to all client orders on the session.
Next: client decides on prod limits.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1791450035281399 https://mahifx.slack.com/archives/C09HN93T0G2/p1791802948207999

### stonex-surya-tt — New StoneX/Surya TT connection via OneZero
status: open · since: 2026-09-15 · last: 2026-10-13
State: Mahi built fixOrdersTT4 and ttPassthroughGateway4 (NY) for market TT_MHNY4_FUND_STONEX_SURYA_FIX_OR; OneZero connected and logged on 2026-10-09. A test trade on 2026-10-13 was rejected with "TT FIX: No connection_id found for BankAlgo with providerID RCM". William Denny asked the client to check with TT whether the account is connected; client said it would.
Next: client checks with TT.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1789466674694669 https://mahifx.slack.com/archives/C09HN93T0G2/p1791889319503849

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

### ip-whitelist-beeks — Brandon cannot reach Compass/Echo from new IP
status: open · since: 2026-09-08 · last: 2026-09-16
State: Client asked to whitelist 108.136.145.119 for Echo and Compass; Brandon still could not connect as of 2026-09-16, Beeks running a TCP dump. No resolution visible after that; older context not searched.
Next: confirm with client whether access works.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1788860536902869 https://mahifx.slack.com/archives/C09HN93T0G2/p1789557438771399

### ab-book-queries — A/B book classification requests from overnight team
status: open · since: 2026-07-08 · last: 2026-09-23
State: Recurring: the client overnight desk posts "please advise Ac <id>" and a Mahi analyst replies A or B book with a chart, usually within minutes. Window ran to 2026-09-23 (30041581: A book in XAUUSD, one to keep an eye on). Client also asked what the Echo yield-profile "Off Market" filter means (Daria Horton explained 2026-08-20).
Refs: https://mahifx.slack.com/archives/CSLM3Q8AD/p1783493649978839 https://mahifx.slack.com/archives/CSLM3Q8AD/p1790145964480289

### overnight-reconnects — Overnight connection fixes
status: watching · since: 2026-08-18 · last: 2026-09-21
State: Overnight desk posts a screenshot ("please can you fix this for us") out of hours; Sam Hewitt or Daria Horton fix it within about 2 minutes and the client confirms (2026-08-18, 2026-08-27, 2026-09-21).
Refs: https://mahifx.slack.com/archives/CSLM3Q8AD/p1787088431402609 https://mahifx.slack.com/archives/CSLM3Q8AD/p1790025740559209

### dashboard-stability — Compass dashboard and admin outages
status: watching · since: 2026-08-17 · last: 2026-10-05
State: Compass errors on 2026-09-20 (fix deployed by Sam Hewitt, trading unaffected), LDN dashboard login bounce fixed by a dashboard-only deploy on 2026-09-28 (NY already fixed), and a transient all-tab error on 2026-10-05 that cleared after refresh. Sam raised LDN backgroundJobs memory 2048 to 3072MB on 2026-09-01.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1789937493122649 https://mahifx.slack.com/archives/C09HN93T0G2/p1791193345574799

### contract-rolls — Futures and CFD rolls announced by client
status: watching · since: 2026-08-18 · last: 2026-10-15
State: Client posts FYIs for rolls (USOIL Oct to Nov to Dec for AMB, US100 Sep to Dec, GC Dec26 gold). Mahi acknowledges; Garry asked on 2026-08-18 whether symbol pricing switches automatically on a roll.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787042749088329 https://mahifx.slack.com/archives/C09HN93T0G2/p1792043232458789

### beeks-hosting — Client exit from Beeks, Compass hosting move
status: watching · since: 2026-07-30 · last: 2026-07-31
State: Graeme said the client is done with Beeks and asked whether Mahi prefers the servers transferred to Mahi's account (rebilled) or moved to a new provider. Beeks (Martyna) offered no price rise for Mahi and a monthly capacity call. No later activity seen in window; hosts still Beeks-based in October.
Next: Mahi decision on transfer or new provider; reply to client.
Refs: https://mahifx.slack.com/archives/CP7A1F8BT/p1785399649401229 https://mahifx.slack.com/archives/CP7A1F8BT/p1785496853098919

### feed-lp-routing — B2Broker LP feed routing
status: closed · since: 2026-08-12 · last: 2026-10-05 · closed: 2026-10-15
State: New LPs (JT, GCEX, B2_OZNY4_RETAIL_MARGIN_VT) caused FEED4 disconnections; B2 duplicated on FEED1 and FEED4. On 2026-10-05 client confirmed B2 comes via FEED1 and Shyam Hari moved the market selector from FEED4 to FEED1.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1787633651014009 https://mahifx.slack.com/archives/CP7A1F8BT/p1791230817547969

### qb-session-hours — fixOrdersQB1 session schedule
status: closed · since: 2026-10-05 · last: 2026-10-06 · closed: 2026-10-15
State: Client confirmed QB hours 5pm Chicago to 4pm next day (18:00-17:00 NYT). Mahi changed fixOrdersQB1 session times on 2026-10-07 (low-risk change CHG-2610-P1WP).
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1791169713201199 https://mahifx.slack.com/archives/C09HN93T0G2/p1791325982612159

### echo-compass-users — Echo/Compass user admin
status: closed · since: 2026-09-01 · last: 2026-09-29 · closed: 2026-10-15
State: Echo user audit list and removal of 14 users (2026-09-01); new Compass and Echo account for a client analyst created 2026-09-29, credentials emailed.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1788234307503689 https://mahifx.slack.com/archives/C09HN93T0G2/p1790654563743499

### tt-stunnel-pinning — TT certificate pinning removal
status: closed · since: 2026-09-23 · last: 2026-09-23 · closed: 2026-10-15
State: Liam confirmed no Mahi impact (no stunnel/cert loading); UAT bounced and reconnected cleanly.
Refs: https://mahifx.slack.com/archives/C09HN93T0G2/p1790154246462319 https://mahifx.slack.com/archives/C09HN93T0G2/p1790154788215129

## Arc
- 2026-05-21 — Both SOWs signed: Scale POV and Quantitative Brokers (QB)
- 2026-07 — QB production session live (early July)
- 2026-07-30 — Client asks to move Compass hosting off Beeks
- 2026-08-26 — GreySpark reference call (Project Redwood): NPS 9/10, very happy to promote
- 2026-09-09 — Press report: Valutrades stops CFD client onboarding globally
- 2026-10-12 — Bridge-to-production quote (~$5k/month) relayed to Graeme; targets 1 Jan launch
