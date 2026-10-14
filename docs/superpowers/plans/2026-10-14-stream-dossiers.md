# Stream-based dossiers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace event-log dossiers with small, current-state, stream-based dossiers (git as the event log), speed up the daily routine, and rebuild every existing dossier once.

**Architecture:** A stdlib-only Python module `scripts/dossierlib.py` parses the new format and holds all checks/pruning; thin CLIs (`check-dossiers`, `prune-dossiers`) wrap it and the pre-commit hook calls `check-dossiers --staged`. Skills (`catchup`, `slack-attack`, `weekly-overview`) are rewritten around streams and a `streams:` commit trailer; `catchup` carries a temporary legacy-conversion mode that rebuilds each old dossier during the restart catch-up.

**Tech Stack:** Python 3 stdlib (`unittest`, `re`, `datetime`, `subprocess`), git, Markdown skills, Slack MCP, RemoteTrigger.

**Spec:** `docs/superpowers/specs/2026-10-14-stream-dossiers-design.md`

## Global Constraints

- No writes outside this repo. `../VibePulse`, `../MahiProduct`, Slack are read-only sources.
- Python: stdlib only, no `X | None` annotations or other 3.10+ syntax (the cloud routine's interpreter is unknown).
- Commits: conventional, imperative, lowercase, subject ≤72 chars, no trailing period; end with the session's `Co-Authored-By` / `Claude-Session` trailer lines.
- Dossier hard cap 15360 bytes (15KB); soft target 10240 bytes.
- Stream ID: kebab-case, ≤24 chars, unique per dossier, never renamed or reused.
- Meta line exactly: `status: <open|watching|closed> · since: YYYY-MM-DD · last: YYYY-MM-DD[ · closed: YYYY-MM-DD]` (separator is ` · `, U+00B7).
- Forced review thresholds: open `last` >30d, watching `last` >60d. Prune closed streams whose `closed` is >14d old.
- Permalinks are bare URLs `https://mahifx.slack.com/archives/<CID>/p<16 digits>`; never fabricated.
- Run tests with: `python3 -m unittest discover -s scripts/tests -v` from the repo root.

## Review Focus

1. Agent writes the meta line with `|` or `-` separators, or puts it after `State:` → check must fail with a message that shows the exact expected format (Task 2 test `test_meta_with_wrong_separator_reports_expected_format`).
2. Pruning the last stream in `## Streams` must not swallow the following `## Arc` heading or its lines (Task 3 test `test_prune_last_stream_keeps_arc`).
3. `--staged` on a brand-new dossier (no HEAD blob) must not crash, and removing an open stream must block the commit (Task 3 CLI tests).
4. A dossier where `last` is one day off its permalink (London vs UTC date) must pass; one a year off must fail (Task 2 tests `test_last_one_day_off_ok`, `test_last_year_off_fails`).
5. Parallel catchup subagents committing in one repo hit `.git/index.lock` → skill text mandates retry (Task 6 text; verified in the Task 10 pilot by running two conversions concurrently).

---

### Task 1: Dossier parser (`scripts/dossierlib.py`)

**Files:**
- Create: `scripts/dossierlib.py`
- Test: `scripts/tests/test_dossierlib.py`, `scripts/tests/helpers.py`

**Interfaces:**
- Produces:
  - `parse(text: str, path: str = "") -> Dossier`
  - `Dossier` fields: `path`, `text`, `lines` (list of str, `text.split("\n")`), `frontmatter` (str, raw, `""` if none), `sections` (dict lower-case name → `(start, end)` line indices, start = `## ` line, end exclusive), `streams` (list of `Stream`); property `legacy` (True when no `streams` section).
  - `Stream` fields: `id`, `title`, `start` (index of `### ` line), `end` (exclusive), `body` (lines after heading), `meta` (dict with keys `status`, `since`, `last`, `closed` or `None`), `heading_ok` (bool). Methods: `field(name) -> str|None` (value after `Name:` on a body line), `status` property, `date(key) -> datetime.date|None`.
  - `permalink_dates(text: str) -> list[datetime.date]`
  - `frontmatter_keys(frontmatter: str) -> set[str]`
  - `remove_streams(d: Dossier, ids) -> str`
  - Constants `PERMALINK_RE`, `ID_RE`, `META_RE`, `MAX_ID_LEN = 24`.

- [ ] **Step 1: Write test helpers**

`scripts/tests/helpers.py`:

```python
import datetime as dt
import os
import sys

SCRIPTS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, SCRIPTS)

TODAY = dt.date(2026, 10, 14)


def link(day, cid="C09D8V41JAG"):
    """A real-shaped Slack permalink whose ts falls at 12:00 UTC on `day`."""
    secs = int(dt.datetime.fromisoformat(day + "T12:00:00+00:00").timestamp())
    return f"https://mahifx.slack.com/archives/{cid}/p{secs}000123"


def stream(sid="tegis-api", status="open", since="2026-09-02", last="2026-10-14",
           closed=None, refs=None, title="Tegis direct integration",
           state="Paused for algo testing.", meta=None):
    if meta is None:
        meta = f"status: {status} · since: {since} · last: {last}"
        if closed:
            meta += f" · closed: {closed}"
    if refs is None:
        refs = f"{link(since)} {link(last)}"
    return f"### {sid} — {title}\n{meta}\nState: {state}\nRefs: {refs}\n"


CLIENT_FM = (
    "slug: basemarkets\n"
    "refs:\n"
    "  wiki: null\n"
    "channels:\n"
    "  mahi-base-markets: C09D8V41JAG\n"
    "last_catchup: 2026-10-14T09:00:57Z\n"
)


def dossier(*streams, now="Tegis paused.", arc="- 2026-06-29 — C Book live\n", fm=CLIENT_FM):
    body = "\n".join(streams)
    return f"---\n{fm}---\n\n## Now\n{now}\n\n## Streams\n\n{body}\n## Arc\n{arc}"


LEGACY = (
    "---\nslug: x\nlast_catchup: 2026-08-17T08:00:00Z\n---\n\n"
    "## Recent issues\n\n"
    "> [open] 2026-08-10 — Something\n"
    f"> Detail. [permalink]({link('2026-08-10')})\n"
)
```

- [ ] **Step 2: Write failing parser tests**

`scripts/tests/test_dossierlib.py`:

```python
import unittest

from helpers import LEGACY, dossier, link, stream
import dossierlib as dl


class ParseTest(unittest.TestCase):
    def test_parses_streams_and_meta(self):
        d = dl.parse(dossier(stream(), stream("mt4-decom", status="closed", since="2026-10-11",
                                               last="2026-10-13", closed="2026-10-13")))
        self.assertFalse(d.legacy)
        self.assertEqual([s.id for s in d.streams], ["tegis-api", "mt4-decom"])
        s = d.streams[1]
        self.assertTrue(s.heading_ok)
        self.assertEqual(s.status, "closed")
        self.assertEqual(str(s.date("closed")), "2026-10-13")
        self.assertEqual(s.field("State"), "Paused for algo testing.")
        self.assertIn("frontmatter", dl.Dossier.__dataclass_fields__)
        self.assertIn("slug", dl.frontmatter_keys(d.frontmatter))

    def test_legacy_detected(self):
        self.assertTrue(dl.parse(LEGACY).legacy)

    def test_invalid_calendar_date_gives_no_meta(self):
        d = dl.parse(dossier(stream(since="2026-02-30")))
        self.assertIsNone(d.streams[0].meta)

    def test_bad_heading_flagged(self):
        d = dl.parse(dossier(stream().replace(" — ", " - ", 1)))
        self.assertFalse(d.streams[0].heading_ok)

    def test_permalink_dates(self):
        self.assertEqual([str(x) for x in dl.permalink_dates(link("2026-10-14"))], ["2026-10-14"])

    def test_remove_streams_roundtrip(self):
        text = dossier(stream("a-one"), stream("b-two"))
        d = dl.parse(text)
        out = dl.remove_streams(d, {"a-one"})
        self.assertEqual([s.id for s in dl.parse(out).streams], ["b-two"])
        self.assertEqual(dl.remove_streams(d, set()), text)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: FAIL / ERROR with `ModuleNotFoundError: No module named 'dossierlib'`

- [ ] **Step 4: Implement the parser**

`scripts/dossierlib.py`:

```python
"""Parsing, checks and pruning for stream-format dossiers.

Format contract: docs/superpowers/specs/2026-10-14-stream-dossiers-design.md.
CLIs: scripts/check-dossiers, scripts/prune-dossiers. Stdlib only.
"""

import datetime as dt
import re
from dataclasses import dataclass

PERMALINK_RE = re.compile(r"https://mahifx\.slack\.com/archives/[A-Z0-9]+/p(\d{10})\d+")
SECTION_RE = re.compile(r"^## (.+?)\s*$")
STREAM_RE = re.compile(r"^### (\S+) — (.+?)\s*$")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
META_RE = re.compile(
    r"^status: (?P<status>open|watching|closed)"
    r" · since: (?P<since>\d{4}-\d{2}-\d{2})"
    r" · last: (?P<last>\d{4}-\d{2}-\d{2})"
    r"(?: · closed: (?P<closed>\d{4}-\d{2}-\d{2}))?\s*$"
)
META_FORMAT = "status: open|watching|closed · since: YYYY-MM-DD · last: YYYY-MM-DD[ · closed: YYYY-MM-DD]"
MAX_ID_LEN = 24


def permalink_dates(text):
    return [dt.datetime.fromtimestamp(int(s), tz=dt.timezone.utc).date()
            for s in PERMALINK_RE.findall(text or "")]


@dataclass
class Stream:
    id: str
    title: str
    start: int
    end: int
    body: list
    meta: object
    heading_ok: bool

    def field(self, name):
        prefix = name + ":"
        for line in self.body:
            if line.startswith(prefix):
                return line[len(prefix):].strip()
        return None

    @property
    def status(self):
        return self.meta["status"] if self.meta else None

    def date(self, key):
        value = self.meta.get(key) if self.meta else None
        return dt.date.fromisoformat(value) if value else None


@dataclass
class Dossier:
    path: str
    text: str
    lines: list
    frontmatter: str
    sections: dict
    streams: list

    @property
    def legacy(self):
        return "streams" not in self.sections


def _parse_meta(line):
    m = META_RE.match(line)
    if not m:
        return None
    try:
        for key in ("since", "last", "closed"):
            if m.group(key):
                dt.date.fromisoformat(m.group(key))
    except ValueError:
        return None
    return m.groupdict()


def parse(text, path=""):
    lines = text.split("\n")
    frontmatter, body_start = "", 0
    if lines and lines[0] == "---":
        for i in range(1, len(lines)):
            if lines[i] == "---":
                frontmatter, body_start = "\n".join(lines[1:i]), i + 1
                break

    heads = []
    for i in range(body_start, len(lines)):
        m = SECTION_RE.match(lines[i])
        if m:
            heads.append((m.group(1).strip().lower(), i))
    sections = {}
    for k, (name, start) in enumerate(heads):
        end = heads[k + 1][1] if k + 1 < len(heads) else len(lines)
        sections.setdefault(name, (start, end))

    streams = []
    if "streams" in sections:
        s0, s1 = sections["streams"]
        starts = [i for i in range(s0 + 1, s1) if lines[i].startswith("### ")]
        for k, i in enumerate(starts):
            end = starts[k + 1] if k + 1 < len(starts) else s1
            m = STREAM_RE.match(lines[i])
            sid, title = (m.group(1), m.group(2)) if m else (lines[i][4:].split(" ")[0], "")
            body = lines[i + 1:end]
            first = next((line for line in body if line.strip()), "")
            streams.append(Stream(sid, title, i, end, body, _parse_meta(first), bool(m)))

    return Dossier(path, text, lines, frontmatter, sections, streams)


def frontmatter_keys(frontmatter):
    keys = set()
    for line in frontmatter.split("\n"):
        if line and line[0] not in " \t#-" and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def remove_streams(d, ids):
    drop = set()
    for s in d.streams:
        if s.id in ids:
            drop.update(range(s.start, s.end))
    if not drop:
        return d.text
    return "\n".join(line for i, line in enumerate(d.lines) if i not in drop)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: 6 tests, OK

- [ ] **Step 6: Commit**

```bash
git add scripts/dossierlib.py scripts/tests/helpers.py scripts/tests/test_dossierlib.py
git commit -m "feat(scripts): add stream-dossier parser"
```

---

### Task 2: Checks (`check`, `stale`, legacy date check)

**Files:**
- Modify: `scripts/dossierlib.py` (append)
- Test: `scripts/tests/test_checks.py`

**Interfaces:**
- Consumes: Task 1 `parse`, `Dossier`, `Stream`, `permalink_dates`, `frontmatter_keys`, `ID_RE`, `META_FORMAT`, `MAX_ID_LEN`.
- Produces:
  - `check(d: Dossier, today: date, head: Dossier|None = None) -> (list[str] errors, list[str] warnings)`
  - `stale(d: Dossier, today: date) -> list[str]` (one line per stream due review: `"<path>: <id> <status> last <date> (<n>d)"`)
  - `legacy_violations(text: str, path: str, today: date) -> list[str]` (ported from `scripts/check-dossier-dates`)
  - Constants `HARD_BYTES = 15360`, `SOFT_BYTES = 10240`, `NOW_MAX_LINES = 4`, `ARC_SOFT_LINES = 20`, `REFS_SOFT = 4`, `STALE_OPEN_DAYS = 30`, `STALE_WATCHING_DAYS = 60`.

- [ ] **Step 1: Write failing tests**

`scripts/tests/test_checks.py`:

```python
import unittest

from helpers import CLIENT_FM, LEGACY, TODAY, dossier, link, stream
import dossierlib as dl


def run(text, path="clients/basemarkets.md", head=None):
    return dl.check(dl.parse(text, path), TODAY, dl.parse(head, path) if head else None)


def errors(text, **kw):
    return run(text, **kw)[0]


class CheckTest(unittest.TestCase):
    def test_valid_dossier_clean(self):
        self.assertEqual(run(dossier(stream())), ([], []))

    def test_missing_frontmatter_key(self):
        fm = CLIENT_FM.replace("channels:\n  mahi-base-markets: C09D8V41JAG\n", "")
        self.assertTrue(any("channels" in e for e in errors(dossier(stream(), fm=fm))))

    def test_channel_dossier_needs_channel_keys(self):
        errs = errors(dossier(stream()), path="channels/dev.md")
        self.assertTrue(any("channel_id" in e for e in errs))

    def test_missing_arc_section(self):
        text = dossier(stream()).split("## Arc")[0]
        self.assertTrue(any("## Arc" in e for e in errors(text)))

    def test_now_too_long(self):
        self.assertTrue(any("Now" in e for e in errors(dossier(stream(), now="a\nb\nc\nd\ne"))))

    def test_bad_ids(self):
        self.assertTrue(errors(dossier(stream("Tegis_API"))))
        self.assertTrue(errors(dossier(stream("a" * 25))))

    def test_duplicate_id(self):
        self.assertTrue(any("duplicate" in e for e in errors(dossier(stream(), stream()))))

    def test_meta_with_wrong_separator_reports_expected_format(self):
        bad = stream(meta="status: open | since: 2026-09-02 | last: 2026-10-14")
        errs = errors(dossier(bad))
        self.assertTrue(any(dl.META_FORMAT in e for e in errs))

    def test_missing_state_and_refs(self):
        bad = "### x-one — X\nstatus: open · since: 2026-10-14 · last: 2026-10-14\n"
        errs = errors(dossier(bad))
        self.assertTrue(any("State:" in e for e in errs))
        self.assertTrue(any("permalink" in e for e in errs))

    def test_last_one_day_off_ok(self):
        self.assertEqual(errors(dossier(stream(last="2026-10-13", refs=link("2026-10-14")))), [])

    def test_last_year_off_fails(self):
        errs = errors(dossier(stream(since="2025-09-02", last="2026-10-14",
                                     refs=f"{link('2025-09-02')} {link('2025-10-14')}")))
        self.assertTrue(any("year-off" in e for e in errs))

    def test_future_date_fails(self):
        errs = errors(dossier(stream(last="2026-10-20", refs=link("2026-10-20"))))
        self.assertTrue(any("future" in e for e in errs))

    def test_since_after_last_fails(self):
        self.assertTrue(errors(dossier(stream(since="2026-10-14", last="2026-10-01",
                                              refs=link("2026-10-01")))))

    def test_closed_needs_closed_date_and_vice_versa(self):
        self.assertTrue(errors(dossier(stream(status="closed"))))
        self.assertTrue(errors(dossier(stream(status="open", closed="2026-10-14"))))

    def test_size_caps(self):
        big = dossier(stream(state="x" * 16000))
        self.assertTrue(any("hard cap" in e for e in errors(big)))
        mid_errs, mid_warns = run(dossier(stream(state="x" * 11000)))
        self.assertEqual(mid_errs, [])
        self.assertTrue(any("10240" in w for w in mid_warns))

    def test_refs_and_arc_soft_warnings(self):
        many = " ".join(link("2026-10-14") for _ in range(5))
        self.assertTrue(run(dossier(stream(refs=many)))[1])
        self.assertTrue(run(dossier(stream(), arc="- 2026-01-01 — x\n" * 21))[1])

    def test_open_stream_removed_vs_head_fails(self):
        head = dossier(stream(), stream("mt4-decom"))
        errs = errors(dossier(stream()), head=head)
        self.assertTrue(any("mt4-decom" in e for e in errs))

    def test_closed_stream_removed_vs_head_ok(self):
        head = dossier(stream(), stream("mt4-decom", status="closed", closed="2026-10-14"))
        self.assertEqual(errors(dossier(stream()), head=head), [])

    def test_legacy_routes_to_old_check(self):
        self.assertEqual(run(LEGACY), ([], []))
        corrupt = LEGACY.replace("> [open] 2026-08-10", "> [open] 2025-08-10")
        self.assertTrue(errors(corrupt))


class StaleTest(unittest.TestCase):
    def test_stale_lists(self):
        d = dl.parse(dossier(
            stream("old-open", last="2026-09-01", refs=link("2026-09-01")),
            stream("fresh-open", last="2026-10-01", refs=link("2026-10-01")),
            stream("old-watch", status="watching", since="2026-08-01", last="2026-08-01",
                   refs=link("2026-08-01")),
            stream("young-watch", status="watching", last="2026-09-01", refs=link("2026-09-01")),
            stream("done", status="closed", last="2026-07-01", closed="2026-07-01",
                   since="2026-07-01", refs=link("2026-07-01")),
        ), "clients/x.md")
        ids = [line.split()[1] for line in dl.stale(d, TODAY)]
        self.assertEqual(ids, ["old-open", "old-watch"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: `test_checks` errors with `AttributeError: module 'dossierlib' has no attribute 'check'`

- [ ] **Step 3: Implement checks** — append to `scripts/dossierlib.py`:

```python
import os

HARD_BYTES = 15360
SOFT_BYTES = 10240
NOW_MAX_LINES = 4
ARC_SOFT_LINES = 20
REFS_SOFT = 4
STALE_OPEN_DAYS = 30
STALE_WATCHING_DAYS = 60
CLIENT_KEYS = {"slug", "refs", "channels", "last_catchup"}
CHANNEL_KEYS = {"name", "channel_id", "purpose", "scope", "last_catchup"}
REQUIRED_SECTIONS = ("now", "streams", "arc")


def _is_channel_dossier(path):
    return os.path.basename(os.path.dirname(path)) == "channels"


def _section_lines(d, name):
    start, end = d.sections[name]
    return [line for line in d.lines[start + 1:end] if line.strip()]


def check(d, today, head=None):
    p = d.path
    if d.legacy:
        return legacy_violations(d.text, p, today), []

    errs, warns = [], []
    size = len(d.text.encode("utf-8"))
    if size > HARD_BYTES:
        errs.append(f"{p}: {size} bytes exceeds hard cap {HARD_BYTES} — consolidate or close streams")
    elif size > SOFT_BYTES:
        warns.append(f"{p}: {size} bytes over soft target {SOFT_BYTES}")

    need = CHANNEL_KEYS if _is_channel_dossier(p) else CLIENT_KEYS
    missing = need - frontmatter_keys(d.frontmatter)
    if missing:
        errs.append(f"{p}: frontmatter missing {', '.join(sorted(missing))}")
    for name in REQUIRED_SECTIONS:
        if name not in d.sections:
            errs.append(f"{p}: missing ## {name.capitalize()} section")
    if "now" in d.sections and len(_section_lines(d, "now")) > NOW_MAX_LINES:
        errs.append(f"{p}: ## Now has more than {NOW_MAX_LINES} lines")
    if "arc" in d.sections:
        arc = [line for line in _section_lines(d, "arc") if line.startswith("- ")]
        if len(arc) > ARC_SOFT_LINES:
            warns.append(f"{p}: ## Arc has {len(arc)} lines (soft cap {ARC_SOFT_LINES}) — merge the oldest")

    latest_ok = today + dt.timedelta(days=1)
    seen = set()
    for s in d.streams:
        loc = f"{p}:{s.start + 1}: stream {s.id}"
        if not s.heading_ok or not ID_RE.match(s.id) or len(s.id) > MAX_ID_LEN:
            errs.append(f"{loc}: heading must be '### <kebab-id> — <title>', id ≤{MAX_ID_LEN} chars")
        if s.id in seen:
            errs.append(f"{loc}: duplicate stream id")
        seen.add(s.id)
        if s.meta is None:
            errs.append(f"{loc}: first line must be '{META_FORMAT}'")
            continue
        if s.field("State") is None:
            errs.append(f"{loc}: missing 'State:' line")
        refs = permalink_dates(s.field("Refs"))
        if not refs:
            errs.append(f"{loc}: 'Refs:' line needs at least one Slack permalink")
        elif len(refs) > REFS_SOFT:
            warns.append(f"{loc}: {len(refs)} permalinks in Refs (keep ≤{REFS_SOFT})")

        since, last, closed = s.date("since"), s.date("last"), s.date("closed")
        if since > last:
            errs.append(f"{loc}: since {since} is after last {last}")
        for key, value in (("since", since), ("last", last), ("closed", closed)):
            if value and value > latest_ok:
                errs.append(f"{loc}: {key} {value} is in the future (today {today})")
        if s.status == "closed" and not closed:
            errs.append(f"{loc}: closed stream needs '· closed: YYYY-MM-DD'")
        if s.status != "closed" and closed:
            errs.append(f"{loc}: only closed streams carry a closed: date")
        if refs and min(abs((last - r).days) for r in refs) > 1:
            cited = ", ".join(str(r) for r in sorted(set(refs)))
            errs.append(f"{loc}: last {last} matches no Refs permalink date [{cited}] — "
                        "update Refs to the latest message, or this is the year-off date bug")

    if head is not None and not head.legacy:
        current = {s.id for s in d.streams}
        for s in head.streams:
            if s.status in ("open", "watching") and s.id not in current:
                errs.append(f"{p}: stream {s.id} was {s.status} in HEAD and has been removed — "
                            "close it instead; only scripts/prune-dossiers removes closed streams")
    return errs, warns


def stale(d, today):
    out = []
    for s in d.streams:
        if not s.meta or s.status == "closed":
            continue
        age = (today - s.date("last")).days
        limit = STALE_OPEN_DAYS if s.status == "open" else STALE_WATCHING_DAYS
        if age > limit:
            out.append(f"{d.path}: {s.id} {s.status} last {s.date('last')} ({age}d)")
    return out


# --- legacy (pre-stream) dossiers: the old year-off guard, kept until conversion finishes ---

LEGACY_SECTIONS = ("recent issues", "recent topics", "notable topics")
LEGACY_HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*$")
LEGACY_ISSUE_RE = re.compile(r"^>\s*\[[a-z]+\]\s+(\d{4}-\d{2}-\d{2})\b")
LEGACY_BULLET_RE = re.compile(r"^-\s+(\d{4}-\d{2}-\d{2})\b")
LEGACY_MAX_DRIFT_DAYS = 180


def legacy_violations(text, path, today):
    lines = text.split("\n")
    out, in_target, i, n = [], False, 0, len(lines)
    while i < n:
        line = lines[i]
        heading = LEGACY_HEADING_RE.match(line)
        if heading:
            in_target = heading.group(1).strip().lower() in LEGACY_SECTIONS
            i += 1
            continue
        if not in_target:
            i += 1
            continue
        lineno, block = i + 1, [line]
        issue, bullet = LEGACY_ISSUE_RE.match(line), LEGACY_BULLET_RE.match(line)
        if issue:
            label = issue.group(1)
            j = i + 1
            while j < n and lines[j].lstrip().startswith(">") and not LEGACY_ISSUE_RE.match(lines[j]):
                block.append(lines[j])
                j += 1
            i = j
        elif bullet:
            label = bullet.group(1)
            i += 1
        else:
            i += 1
            continue
        try:
            label_date = dt.date.fromisoformat(label)
        except ValueError:
            out.append(f"{path}:{lineno}: invalid date {label}")
            continue
        if label_date > today:
            out.append(f"{path}:{lineno}: future-dated entry {label} (today is {today})")
            continue
        pdates = permalink_dates("\n".join(block))
        if pdates and min(abs((label_date - p).days) for p in pdates) > LEGACY_MAX_DRIFT_DAYS:
            out.append(f"{path}:{lineno}: label {label} far from its cited permalinks — likely year-off date bug")
    return out
```

Move `import os` to the top-level import block with the other imports (keep imports at the top of the file).

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: all tests OK (6 parser + 20 check/stale)

- [ ] **Step 5: Commit**

```bash
git add scripts/dossierlib.py scripts/tests/test_checks.py
git commit -m "feat(scripts): add stream-dossier checks and stale review"
```

---

### Task 3: Prune + CLIs + pre-commit hook

**Files:**
- Modify: `scripts/dossierlib.py` (append `prune_text`)
- Create: `scripts/check-dossiers`, `scripts/prune-dossiers` (executable)
- Delete: `scripts/check-dossier-dates`
- Modify: `.githooks/pre-commit`
- Test: `scripts/tests/test_prune.py`, `scripts/tests/test_cli.py`

**Interfaces:**
- Consumes: Task 1–2 (`parse`, `remove_streams`, `check`, `stale`).
- Produces:
  - `prune_text(text: str, today: date, path: str = "") -> (str new_text, list[str] removed_ids)`; constant `PRUNE_AFTER_DAYS = 14`.
  - CLI `scripts/check-dossiers FILE...|--staged|--stale FILE...` (exit 0 clean, 1 violations, 2 usage/IO).
  - CLI `scripts/prune-dossiers FILE...` prints `<path>: pruned <id>` per removal.

- [ ] **Step 1: Write failing tests**

`scripts/tests/test_prune.py`:

```python
import unittest

from helpers import TODAY, dossier, link, stream
import dossierlib as dl


def closed(sid, day):
    return stream(sid, status="closed", since=day, last=day, closed=day, refs=link(day))


class PruneTest(unittest.TestCase):
    def test_prunes_only_old_closed(self):
        text = dossier(stream("live-one"), closed("old-done", "2026-09-20"), closed("new-done", "2026-10-05"))
        out, removed = dl.prune_text(text, TODAY)
        self.assertEqual(removed, ["old-done"])
        self.assertEqual([s.id for s in dl.parse(out).streams], ["live-one", "new-done"])

    def test_prune_last_stream_keeps_arc(self):
        text = dossier(stream("live-one"), closed("old-done", "2026-09-01"))
        out, _ = dl.prune_text(text, TODAY)
        d = dl.parse(out)
        self.assertIn("arc", d.sections)
        self.assertIn("- 2026-06-29 — C Book live", out)
        self.assertEqual(dl.check(d, TODAY)[0], [])

    def test_noop_and_legacy_untouched(self):
        text = dossier(stream())
        self.assertEqual(dl.prune_text(text, TODAY), (text, []))
        from helpers import LEGACY
        self.assertEqual(dl.prune_text(LEGACY, TODAY), (LEGACY, []))


if __name__ == "__main__":
    unittest.main()
```

`scripts/tests/test_cli.py`:

```python
import os
import shutil
import subprocess
import tempfile
import unittest

from helpers import SCRIPTS, dossier, link, stream

CHECK = os.path.join(SCRIPTS, "check-dossiers")
PRUNE = os.path.join(SCRIPTS, "prune-dossiers")


def git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


class CliTest(unittest.TestCase):
    def setUp(self):
        self.repo = tempfile.mkdtemp()
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.email", "t@example.com")
        git(self.repo, "config", "user.name", "t")
        os.makedirs(os.path.join(self.repo, "clients"))
        self.path = os.path.join(self.repo, "clients", "x.md")

    def tearDown(self):
        shutil.rmtree(self.repo)

    def write(self, text):
        with open(self.path, "w") as fh:
            fh.write(text)

    def run_check(self, *args):
        return subprocess.run([CHECK, *args], cwd=self.repo, capture_output=True, text=True)

    def test_staged_new_file_passes(self):
        self.write(dossier(stream()))
        git(self.repo, "add", "clients/x.md")
        r = self.run_check("--staged")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_staged_removed_open_stream_blocks(self):
        self.write(dossier(stream(), stream("mt4-decom")))
        git(self.repo, "add", "clients/x.md")
        git(self.repo, "commit", "-qm", "seed")
        self.write(dossier(stream()))
        git(self.repo, "add", "clients/x.md")
        r = self.run_check("--staged")
        self.assertEqual(r.returncode, 1)
        self.assertIn("mt4-decom", r.stderr)

    def test_file_mode_and_stale_and_usage(self):
        self.write(dossier(stream("old-open", last="2026-01-05", since="2026-01-05", refs=link("2026-01-05"))))
        self.assertEqual(self.run_check("clients/x.md").returncode, 0)
        r = self.run_check("--stale", "clients/x.md")
        self.assertEqual(r.returncode, 0)
        self.assertIn("old-open", r.stdout)
        self.assertEqual(self.run_check().returncode, 2)

    def test_prune_cli(self):
        day = "2026-01-05"
        self.write(dossier(stream(), stream("old-done", status="closed", since=day, last=day,
                                            closed=day, refs=link(day))))
        r = subprocess.run([PRUNE, "clients/x.md"], cwd=self.repo, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("clients/x.md: pruned old-done", r.stdout)
        with open(self.path) as fh:
            self.assertNotIn("old-done", fh.read())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: `prune_text` AttributeError; CLI tests fail with `FileNotFoundError` for `check-dossiers`.

- [ ] **Step 3: Implement `prune_text`** — append to `scripts/dossierlib.py`:

```python
PRUNE_AFTER_DAYS = 14


def prune_text(text, today, path=""):
    d = parse(text, path)
    if d.legacy:
        return text, []
    cutoff = today - dt.timedelta(days=PRUNE_AFTER_DAYS)
    ids = [s.id for s in d.streams
           if s.status == "closed" and s.date("closed") and s.date("closed") < cutoff]
    if not ids:
        return text, []
    return remove_streams(d, set(ids)), ids
```

- [ ] **Step 4: Create `scripts/check-dossiers`**

```python
#!/usr/bin/env python3
"""Validate stream-format dossiers (contract: docs/superpowers/specs/2026-10-14-stream-dossiers-design.md).

Usage:
  scripts/check-dossiers FILE ...          check files
  scripts/check-dossiers --staged          check staged dossiers (pre-commit), incl. stream-ID stability vs HEAD
  scripts/check-dossiers --stale FILE ...  list streams due a forced review (never fails)

--staged validates the working-tree copy of each staged dossier (catchup stages exactly what it wrote).
Exit: 0 clean (warnings allowed), 1 violations, 2 usage/IO error.
"""

import datetime as dt
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dossierlib as dl  # noqa: E402

DOSSIER_RE = re.compile(r"^(clients|channels)/(?!_template\.md$)[^/]+\.md$")


def staged_files():
    out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                         capture_output=True, text=True, check=True).stdout.splitlines()
    return [f for f in out if DOSSIER_RE.match(f)]


def head_text(path):
    r = subprocess.run(["git", "show", f"HEAD:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    today = dt.datetime.now(dt.timezone.utc).date()

    if args[0] == "--stale":
        for path in args[1:]:
            d = dl.parse(read(path), path)
            if not d.legacy:
                for line in dl.stale(d, today):
                    print(line)
        return 0

    staged = args == ["--staged"]
    try:
        files = staged_files() if staged else [a for a in args if os.path.basename(a) != "_template.md"]
    except subprocess.CalledProcessError as exc:
        print(f"check-dossiers: git failed: {exc}", file=sys.stderr)
        return 2

    errs, warns = [], []
    for path in files:
        try:
            text = read(path)
        except OSError as exc:
            errs.append(f"{path}: cannot read ({exc})")
            continue
        head = None
        if staged:
            ht = head_text(path)
            head = dl.parse(ht, path) if ht is not None else None
        e, w = dl.check(dl.parse(text, path), today, head)
        errs.extend(e)
        warns.extend(w)

    for w in warns:
        print(f"warning: {w}", file=sys.stderr)
    if errs:
        print("Dossier check FAILED:", file=sys.stderr)
        for e in errs:
            print(f"  {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 5: Create `scripts/prune-dossiers`**

```python
#!/usr/bin/env python3
"""Remove closed streams whose closed: date is more than 14 days old.

Usage: scripts/prune-dossiers FILE ...
Prints '<path>: pruned <id>' per removed stream (use these for the commit's streams: trailer).
Legacy (pre-stream) dossiers are left untouched. Exit 0, or 2 on IO error.
"""

import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dossierlib as dl  # noqa: E402


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    today = dt.datetime.now(dt.timezone.utc).date()
    for path in argv[1:]:
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            new, removed = dl.prune_text(text, today, path)
            if removed:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
        except OSError as exc:
            print(f"prune-dossiers: {path}: {exc}", file=sys.stderr)
            return 2
        for sid in removed:
            print(f"{path}: pruned {sid}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 6: Wire up and remove the old checker**

```bash
chmod +x scripts/check-dossiers scripts/prune-dossiers
git rm -q scripts/check-dossier-dates
```

Replace `.githooks/pre-commit` with:

```sh
#!/bin/sh
# Validate staged dossiers: stream-format structure, size cap, stream-ID stability vs HEAD,
# and the year-off date guard (stream last: must match a cited permalink date; legacy
# dossiers keep the old entry-date check until conversion finishes).
# Rules live in scripts/dossierlib.py; contract in docs/superpowers/specs/2026-10-14-stream-dossiers-design.md.

root=$(git rev-parse --show-toplevel)

if ! python3 "$root/scripts/check-dossiers" --staged; then
    echo ""
    echo "Commit blocked: dossier check failed (see above)."
    echo "For the agent: ABORT this run — do not bump last_catchup, do not --no-verify."
    echo "To bypass for a deliberate, verified human edit: git commit --no-verify"
    exit 1
fi
```

- [ ] **Step 7: Run all tests and the checker over the current tree**

Run: `python3 -m unittest discover -s scripts/tests -v && scripts/check-dossiers clients/*.md channels/*.md; echo exit=$?`
Expected: all tests OK; `exit=0` (every current dossier is legacy and already passes the old guard).

- [ ] **Step 8: Commit**

```bash
git add scripts/ .githooks/pre-commit
git commit -m "feat(scripts): add check-dossiers and prune-dossiers CLIs"
```

---

### Task 4: `rank-clients --due`

**Files:**
- Modify: `scripts/rank-clients`
- Test: `scripts/tests/test_rank_clients.py`

**Interfaces:**
- Produces: `is_due(last_catchup: str|None, now: datetime) -> bool` in `scripts/rank-clients`; CLI flag `--due` filters rows to `is_due`.

- [ ] **Step 1: Write failing test**

`scripts/tests/test_rank_clients.py`:

```python
import datetime as dt
import importlib.machinery
import importlib.util
import os
import unittest

from helpers import SCRIPTS

loader = importlib.machinery.SourceFileLoader("rank_clients", os.path.join(SCRIPTS, "rank-clients"))
spec = importlib.util.spec_from_loader("rank_clients", loader)
rc = importlib.util.module_from_spec(spec)
loader.exec_module(rc)

NOW = dt.datetime(2026, 10, 14, 7, 0, tzinfo=dt.timezone.utc)


class DueTest(unittest.TestCase):
    def test_due(self):
        self.assertTrue(rc.is_due(None, NOW))
        self.assertTrue(rc.is_due("2026-10-13T23:59:59Z", NOW))
        self.assertFalse(rc.is_due("2026-10-14T00:00:01Z", NOW))
        self.assertTrue(rc.is_due("garbage", NOW))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: `AttributeError: module 'rank_clients' has no attribute 'is_due'`

- [ ] **Step 3: Implement** — in `scripts/rank-clients`, add after `days_since`:

```python
def is_due(iso, now):
    """True if never caught up, unparseable, or last caught up before today's UTC start."""
    if not iso or iso.lower() == "null":
        return True
    try:
        last = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return True
    if last.tzinfo is None:
        last = last.replace(tzinfo=timezone.utc)
    return last < now.replace(hour=0, minute=0, second=0, microsecond=0)
```

In `main()`, add the flag and filter:

```python
    ap.add_argument("--due", action="store_true",
                    help="Only clients whose last_catchup is before today's UTC start (or never)")
```

and inside the row loop, after the retired filter:

```python
        if args.due and not is_due(info["last_catchup"], datetime.now(timezone.utc)):
            continue
```

Update the module docstring's Output section with one line: `--due: only rows with last_catchup before today's UTC start (what the daily run must process).`

- [ ] **Step 4: Run tests and a smoke run**

Run: `python3 -m unittest discover -s scripts/tests -v && scripts/rank-clients --due | wc -l`
Expected: tests OK; a count ≥ 25 (nearly every client is due today).

- [ ] **Step 5: Commit**

```bash
git add scripts/rank-clients scripts/tests/test_rank_clients.py
git commit -m "feat(rank-clients): add --due filter for the daily run"
```

---

### Task 5: Templates

**Files:**
- Modify: `clients/_template.md`, `channels/_template.md`
- Test: `scripts/tests/test_templates.py`

- [ ] **Step 1: Write failing test** — `scripts/tests/test_templates.py`:

```python
import datetime as dt
import os
import unittest

from helpers import SCRIPTS
import dossierlib as dl

REPO = os.path.dirname(SCRIPTS)


class TemplateTest(unittest.TestCase):
    def check(self, rel, as_path):
        with open(os.path.join(REPO, rel)) as fh:
            d = dl.parse(fh.read(), as_path)
        self.assertFalse(d.legacy)
        self.assertEqual(dl.check(d, dt.date(2026, 10, 14))[0], [])

    def test_client_template_valid(self):
        self.check("clients/_template.md", "clients/example.md")

    def test_channel_template_valid(self):
        self.check("channels/_template.md", "channels/example.md")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: `test_templates` FAIL (`legacy` is True).

- [ ] **Step 3: Replace `clients/_template.md`** with:

```markdown
---
slug: example
aliases: []                       # other slugs (billing etc.) that map to this dossier
refs:                             # sources only — never copy their contents into the body
  vibepulse: ../VibePulse/.claude/clients/example.yaml   # hosts, slack names, party names, distribution
  billing: ../MahiProduct/data/billing/clients.json       # entry: example
  hosts: ../MahiProduct/data/client-hosts.json            # entry: example
  wiki: null                                               # ../MahiProduct/wiki/clients/example.md if it exists
channels:                         # Slack channel name: ID — catchup's read list
  internal-example: C0000000000
  mahi-example: C0000000001
contacts: []                      # external people NOT in ../MahiProduct/wiki/people/: {name, role[, confidence: low]}
last_catchup: null                # ISO8601 UTC; updated by /catchup
status: active                    # active | retired (+ retired_at: YYYY-MM-DD, retired_reason: text)
---

## Now
Up to 4 lines: what matters with this client right now, for the next agent.

## Streams

### example-topic — Example stream title
status: open · since: 2026-10-01 · last: 2026-10-01
State: Current truth in 1–4 sentences, rewritten in place each time the stream moves.
Next: What we're waiting on / who owes what (omit if nothing).
Refs: https://mahifx.slack.com/archives/C0000000000/p1790856000000100

## Arc
- 2026-10-01 — One line per relationship-level milestone
```

(`p1790856000…` = 2026-10-01 UTC, so the example passes the date check.)

- [ ] **Step 4: Replace `channels/_template.md`** with:

```markdown
---
name: example-channel             # without leading #
channel_id: C0000000000
purpose: ""                       # one line — what this channel is for
scope: cross-cutting              # cross-cutting | team | announcements | other
last_catchup: null                # ISO8601 UTC
---

## Now
Up to 4 lines: why this channel is tracked and what's live in it.

## Streams

### example-topic — Example stream title
status: open · since: 2026-10-01 · last: 2026-10-01
State: Current truth in 1–4 sentences. Client-specific issues belong in that client's dossier.
Refs: https://mahifx.slack.com/archives/C0000000000/p1790856000000100

## Arc
- 2026-10-01 — One line per notable channel-level milestone
```

- [ ] **Step 5: Run tests**

Run: `python3 -m unittest discover -s scripts/tests -v`
Expected: all OK.

- [ ] **Step 6: Commit**

```bash
git add clients/_template.md channels/_template.md scripts/tests/test_templates.py
git commit -m "feat(dossiers): switch templates to stream format"
```

---

### Task 6: Rewrite the `catchup` skill

**Files:**
- Modify: `.claude/skills/catchup/SKILL.md` (full rewrite)

The Bash sandbox denies writes under `.claude/skills/`; use the Write tool.

- [ ] **Step 1: Replace the file with:**

````markdown
---
name: catchup
description: Worker — pulls Slack activity since last_catchup for one client or channel, updates its stream-based dossier in place, and commits. Writes the dossier; does not produce a readable digest. Use when the user says "/catchup <slug>" or "/catchup #<channel>". For the readable brief or a multi-client run, use /slack-attack instead.
---

`/catchup` is the worker. Its product is one dossier file (`clients/<slug>.md` or `channels/<name>.md`) and one commit. Dossiers are read by **agents in this repo**, not humans: keep them small, current and structured. Git is the event log — the dossier holds current state only. It does **not** write a readable brief; that's `/slack-attack`'s job.

A target is required. With no arg, stop and point at `/slack-attack`.

If the client dossier has `status: retired`, emit one line and stop — no Slack pull, no `last_catchup` bump:

```
catchup: <slug> — retired (<retired_at>); skipping. Remove `status: retired` from frontmatter to re-activate.
```

## Who the user is

The reader is **Cameron Copland** (Slack user ID `U099FA0D7CP`). Direct mentions / DMs that target this ID are notable; mentions of other Camerons (notably **Cameron Hughes**, an Analyst — see `../MahiProduct/.claude/org-chart.md`) are not. Match strictly on the Slack user ID — never infer audience from first names.

## Sources — read, never write

- Hosts / Slack channel names / party names / distribution markets → `../VibePulse/.claude/clients/<slug>.yaml`.
- Commercial terms → `../MahiProduct/data/billing/clients.json`.
- Internal Mahi staff → `../MahiProduct/.claude/org-chart.md`. Use it for attribution; never put staff in `contacts`.
- External contacts → `../MahiProduct/wiki/people/`. Only people *not* there go in the dossier's `contacts`.

Never write outside this repo. Never copy into a dossier anything one read of these sources returns (hosts, terms, party names, contact details). The dossier stores the synthesis — what is going on and where it stands — plus permalinks to dig further.

## Dossier format (the contract)

Enforced by `scripts/check-dossiers` (pre-commit runs it). Templates: `clients/_template.md`, `channels/_template.md`.

```markdown
---
slug, aliases, refs, channels (name: ID), contacts, last_catchup, status
---
## Now
≤4 lines: what matters with this client right now.

## Streams

### <id> — <title>
status: open|watching|closed · since: YYYY-MM-DD · last: YYYY-MM-DD[ · closed: YYYY-MM-DD]
State: current truth, 1–4 sentences, rewritten in place.
Next: who owes what (omit if nothing).
Refs: <origin permalink> <latest permalink>   (bare URLs, 1–4)

## Arc
- YYYY-MM-DD — one line per relationship-level milestone (≤~20 lines)
```

- **Stream** = one ongoing topic (an integration, a recurring pricing problem, a commercial thread), not one incident. Ten XAUUSD rejection incidents are one stream. Target 5–15 streams per client.
- **ID**: kebab-case, ≤24 chars, unique, **never renamed or reused**. The heading line is the stable anchor git history is queried by. Edit the title if needed, never the ID.
- **Meta line** is the first line under the heading, exact format above (separator ` · `). `since` = first Slack signal; `last` = date of the latest Slack message on the stream and **must match a permalink in Refs** (±1 day). Dates in UTC.
- **State** is rewritten, never appended to. No "2026-10-07 update —" lines; that history is in git.
- **Order**: open (newest `last` first), then watching, then closed.
- **Size**: ≤10KB target, 15KB hard cap. Over target → merge or close streams, tighten State.
- Never delete a stream by hand. Close it; `scripts/prune-dossiers` removes closed streams 14 days later.

## Resolving the target

- `/catchup <slug>` → `clients/<slug>.md`. Read channels from frontmatter `channels:` (name → ID); skip names matching the skip list in `.claude/docs/slack-conventions.md`.
- If `channels:` is missing a channel the client should have: resolve names from the VibePulse `slack:` block (it's `{internal: <name>, client: <name>}` — **use both**; the internal channel carries the root-cause diagnosis), get IDs with `slack_search_channels` (`channel_types: "public_channel,private_channel"`), and write `name: ID` into `channels:`. Never skip a missing internal channel — that omission cost the axiory LD4 root cause on 2026-04-27.
- `/catchup #<channel>` or `/catchup <channel-name>` → `channels/<name>.md`, reading `channel_id` from frontmatter.
- Dossier has no `## Streams` section → it's legacy: follow **Legacy conversion** below.

### Bootstrap a client dossier

If `clients/<slug>.md` doesn't exist:

1. Find the client: `../VibePulse/.claude/clients/<slug>.yaml` (try hyphen/underscore and `-crypto`/`-cfd` variants). Pre-live clients often have none — then check `../MahiProduct/data/client-hosts.json`, the "Signed but not yet live" section of `../MahiProduct/data/fleet.txt`, `../MahiProduct/data/onboarding/<slug>.json`, and `../MahiProduct/wiki/clients/`. Only if none know it, report unknown and stop.
2. Copy `clients/_template.md` to `clients/<slug>.md`; set `slug`, `refs` (unknown refs `null` with a short trailing comment), `aliases` if billing/onboarding use another slug, `channels` (resolve as above), `contacts: []`, `last_catchup: null`. Delete the template's example stream and Arc line.
3. This run populates Now / Streams / Arc. Use the 30d window (see Reading activity) and expand on ambiguity.
4. Commit subject `chore(catchup): bootstrap <slug> dossier`.

### Bootstrap a channel dossier

If `channels/<name>.md` doesn't exist: copy `channels/_template.md`; `slack_search_channels` for the ID and purpose (skim ~20 recent messages if the purpose is generic); `scope` is a best guess; delete the template example; populate from this run.

## Sanity-check the window — before reading Slack

Anchor every date to **bash output, not your own reasoning**. Three documented corruptions came from the agent miscalculating "today" by a year.

1. Run via Bash and use the output verbatim for the whole run:

   ```
   now_unix=$(date +%s)
   now_iso=$(date -u +%FT%TZ)
   ```

   Never infer "today" from the conversation, the dossier, commit dates or training context.

2. `oldest_unix` = Unix seconds of the dossier's `last_catchup` (`date -u -j -f %Y-%m-%dT%H:%M:%SZ <iso> +%s` on macOS, `date -u -d <iso> +%s` on Linux); for `last_catchup: null`, `now_unix - 30*86400`; for an ambiguity expansion, the wider anchor you chose. Decode it back (`date -u -r $oldest_unix +%FT%TZ` / `date -u -d @$oldest_unix +%FT%TZ`) and confirm it matches what you expected — a year off means abort.
3. If `now_unix - oldest_unix > 90*86400`, abort. The cap is both a cost bound and a year-off tripwire.
4. The `last_catchup` you will write must be ≤ `now_unix + 60`.

On any failure, abort before reading Slack:

```
catchup: <target> — ABORT: window sanity-check failed.

<one line per violation>

Inspect the dossier and your date conversions before retrying.
```

## Reading activity

1. `oldest` = `last_catchup`; if null, 30 days ago.
2. For each channel in `channels:` (minus skip list): `slack_read_channel` with `oldest`, `limit: 100`. If the response has a `next_cursor`, keep paginating until you reach `oldest`.
3. For notable threads, `slack_read_thread` with the real `message_ts` (searches need `response_format: "detailed"` to return it).
4. **Work budget** — so one client can't stall a parallel run: at most 3 pages per channel per 30 days of window (9 pages for 90d) and at most 15 thread expansions (30 in a legacy conversion). If you hit it, stop reading, write what you have, and report `Budget hit on: <channel>`.
5. **Discard out-of-window results.** Drop any message (from search or channel read) whose `ts` falls outside `[oldest_unix, now_unix]` — decode `ts`, don't eyeball it.

## Resolving ambiguity — expand the window

The windows are starting points. If in-window messages reference events you can't see, dig before writing: every stream's State must stand on its own, without "per an earlier event" or "pre-window".

Triggers: a message refers to an earlier event you lack context for; channels contradict each other on lifecycle; a new or converted dossier leaves you guessing about the client's status.

How, in order (expansions count against the work budget):

1. Widen channel reads to 60d, then 90d (never beyond — hard cap).
2. Search the slug across channels with `slack_search_public_and_private` (default context on), **always time-bounded** with `after`/`before` (or the `after:YYYY-MM-DD` / `before:YYYY-MM-DD` modifiers). Unbounded searches are the root of the year-off corruption. Use hits to decide where to read next, not as facts (see next section).
3. Read parent threads via `slack_read_thread`.
4. Follow the breadcrumb to the original message and read around it.

Stop when each stream's State is self-contained with dated permalinks, or at the 90d cap — then say so in State ("earliest signal in window; older context not searched").

## What counts as notable

In priority order:

1. **Direct mentions of the user** (`<@U099FA0D7CP>`) or DMs.
2. **Questions awaiting a reply** — unanswered `?`, especially in threads the user was in.
3. **Decisions** — "we're going to", "agreed", "let's do X".
4. **Escalations** — client dissatisfaction, outages, urgent language, incidents.
5. **Recurring issues** — something an existing stream covers flaring again → update that stream.
6. **New external people** with a known role and expected repeat contact, not in `../MahiProduct/wiki/people/` → `contacts`.
7. **Facts contradicting the dossier or upstream** — fix the stream/Now; don't edit upstream.

Routine bot pings, deployment notifications and single-reaction chatter are not notable.

## Cross-channel signals — trigger, not truth

`slack_read_channel` on the dossier's own channels is authoritative. Search hits from other channels (#sales, #frontoffice, #internal-trading-daily-checks) are **triggers to investigate**:

1. Corroborate against the client's own channels in the same window before writing a claim as fact. (2026-04-29: #sales grouped Fintokei with Errante as offboarded; Fintokei's channels were live — a typo.)
2. Read the search context, don't keyword-match; neighbouring messages often carry the correction. If context is thin, read the source channel or thread around the hit.
3. If corroboration fails, write the contradiction ("sales says X, client channels show Y") in the stream, not the claim.

Never retire a dossier on cross-channel signal alone.

## Updating the dossier

Use `Edit` (small diffs), except bootstrap and legacy conversion (`Write`).

1. **Map** each notable in-window item to a stream. Same topic, counterparty, project or recurring problem → existing stream. Prefer extending a stream over creating a sibling.
2. **Update** a stream that moved: rewrite `State` (current truth, not a log) and `Next`; set `last` to the date of its latest in-window message; in `Refs` keep the origin permalink and replace the previous "latest" with the newest one (max 4).
3. **Create** a new stream for a genuinely new topic: new ID, `since` = its first message date.
4. **Forced review**: run `scripts/check-dossiers --stale <file>` and decide every stream it lists — open >30d without activity: close it (State says how it ended, or "no activity since <date>; assumed resolved") or downgrade to `watching` with a reason; watching >60d: close it, or re-open with a `Next:` naming a concrete pending action. Never leave a listed stream untouched.
5. **Close**: `status: closed`, append `· closed: <today>` to the meta line, State gives the outcome. Relationship-level outcomes (go-live, decommission, contract change, key person change, major incident) also get an Arc line.
6. **Merge**: close the absorbed stream with `State: merged into <id>.`
7. **Now**: rewrite if the client's posture changed (≤4 lines).
8. **Order** streams: open (newest `last` first), watching, closed.
9. **contacts**: add per notability rule 6; `confidence: low` only when unsure.
10. Set `last_catchup` to `now_iso`.

## Legacy conversion (temporary — removed once every dossier is converted)

A dossier without `## Streams` was written by older, less capable models and may contain errors. Rebuild it:

1. Treat the old content (`Status`, `History`, `Recent issues`, `Notable topics`, `key_people_overrides`) as **leads, not facts**.
2. Read Slack for the normal window (`last_catchup` → now) per the sections above.
3. For each old `[open]`/`[watching]` entry: if in-window activity covers it, it's live. Otherwise read the thread of its newest permalink (`slack_read_thread`). No sign of life for >30 days → drop it as `stale` — unless it is an explicit unanswered commitment, which becomes a `watching` stream.
4. Group surviving items and new activity into streams (target 5–15).
5. **Arc**: from old `History` and significant resolved entries (go-lives, decommissions, contract events, major incidents, key people changes); ≤20 lines; exact dates where the source pins them, `YYYY-MM` otherwise.
6. **Frontmatter**: `channels:` from `channels_override` / the VibePulse `slack:` block plus IDs from the table in `.claude/docs/slack-conventions.md` (search for any missing); `contacts` from `key_people_overrides`, minus anyone in `../MahiProduct/wiki/people/` or the org chart; drop `channels_override` and `key_people_overrides`. Keep `slug`, `aliases`, `refs`, `status`/`retired_*`.
7. Write the whole file with `Write` from the template shape; no `Status`, `History`, `Recent issues` or `Notable topics` sections remain. Aim ≤10KB.
8. Commit with subject `refactor(dossiers): convert <slug> to streams` and body:

   ```
   Window <oldest_iso>..<now_iso>.
   streams: <id>(new) <id>(new) ...
   dropped: <N> old entries — <a> resolved, <b> stale, <c> merged
   stale: <short title>; <short title>; ...
   ```

   The `stale:` line lists the titles (≤60 chars each) of every entry dropped as stale, so the user can audit the risky drops.

## Sanity-check before commit

1. `scripts/prune-dossiers <file>` — note any `pruned <id>` lines for the trailer.
2. `scripts/check-dossiers <file>` must exit 0. Warnings: fix size/Arc/Refs warnings if cheap.
3. Every stream you created or updated has `last` within `[date(oldest_iso) - 1 day, date(now_iso)]`.

If 2 or 3 fails and you can't fix it from what you read, **abort**: leave the file dirty, don't commit, don't bump `last_catchup`:

```
catchup: <target> — ABORT: sanity-check failed before commit.

<check-dossiers output / violations>

Likely date-math bug. Inspect with `git diff` before committing manually.
```

The pre-commit hook re-runs the check as a backstop; a clean self-abort is the intended path. Never `--no-verify`.

## Committing

- Stage only the target dossier. Never `git add -A`. If the dossier already had unrelated uncommitted edits before this run, stop and report instead of guessing.
- Subject ≤72 chars (`.githooks/commit-msg` enforces it); dates `YYYY-MM-DD`:

  | Case | Subject |
  |---|---|
  | Refresh | `chore(catchup): refresh <slug> (<YYYY-MM-DD>..<YYYY-MM-DD>)` |
  | Quiet window | `chore(catchup): bump <slug> (quiet window)` |
  | Bootstrap | `chore(catchup): bootstrap <slug> dossier` |
  | Legacy conversion | `refactor(dossiers): convert <slug> to streams` |

- Body (refresh/bootstrap): `Window <oldest_iso>..<now_iso>.` then one trailer line listing every stream touched:

  ```
  streams: tegis-api(updated) mt4-decom(new) xau-hedging(closed) old-thing(pruned) fx-gaps(watching) ack-x(merged>xau-hedging)
  ```

  Verbs: `new | updated | closed | watching | merged>ID | pruned`. `/slack-attack` and `/weekly-overview` read this line; `git log --grep=<id>` depends on it.
- Other catchups commit to this repo in parallel. If `git commit` fails on `.git/index.lock`, `sleep 3` and retry, up to 5 times.
- Don't push. The caller pushes.

## Output (to caller)

```
catchup: <target> — <oldest_iso>..<now_iso>

Commit: <short-sha>
streams: <same trailer line>
Stale review: <n> streams reviewed (<c> closed, <w> → watching, <o> re-opened)
Channels read: <n>, messages scanned: ~<m>, threads expanded: <t>
Budget hit on: <list or "none">
Quiet channels: <list or "none">
```

Quiet window (no notable human activity, nothing reviewed or pruned): bump `last_catchup` only, commit, and output one line:

```
catchup: <target> — quiet window (<N> bot pings, no human discussion). last_catchup bumped (commit <short-sha>).
```

If anything in the window is addressed to the user (direct mention or DM awaiting reply), add a final `Action items:` line with permalinks. Match strictly on `U099FA0D7CP`.

No prose digest. The dossier and commit are the artefact.

## Constraints

- Never fabricate a Slack permalink. Re-search with `response_format: "detailed"` for a real `message_ts`.
- Never rename a stream ID or delete a stream by hand.
- Never write outside this repo.
- Leave empty sections empty — no placeholder text (an empty `## Arc` is fine).
````

- [ ] **Step 2: Verify references resolve**

Run: `grep -nE 'check-dossier-dates|Recent issues entry|key_people_overrides|backfill' .claude/skills/catchup/SKILL.md`
Expected: only the intentional mentions inside "Legacy conversion" (`key_people_overrides`, `Recent issues` as old section names); no `check-dossier-dates`, no `backfill`.

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/catchup/SKILL.md
git commit -m "feat(catchup): rewrite for stream-based dossiers"
```

---

### Task 7: Rewrite the `slack-attack` skill

**Files:**
- Modify: `.claude/skills/slack-attack/SKILL.md` (full rewrite, Write tool)

- [ ] **Step 1: Replace the file with:**

````markdown
---
name: slack-attack
description: Orchestrator and reader-facing entrypoint. Runs /catchup for every due client (or one slug) in parallel subagents, then synthesises a readable natural-language brief from the resulting commits. Use when the user says "/slack-attack" or "/slack-attack <slug>".
---

`/slack-attack` is what the user runs to catch up, and what the daily routine runs once per weekday. It:

1. **Dispatches catchup** for the target client(s) in **subagents**, so Slack reads stay out of the main thread.
2. **Synthesises a brief** from what each catchup committed. Prose, not checklists.

The brief is the product the user reads; dossiers are the durable state agents read.

## Who the brief is for

**Cameron Copland** (Slack `U099FA0D7CP`) — not Cameron Hughes (Analyst) or anyone else in `../MahiProduct/.claude/org-chart.md`.

## Targets

- `/slack-attack <slug>` → one client.
- `/slack-attack` → every **due** client: `scripts/rank-clients --due` (never-caught-up first, then oldest `last_catchup`). Don't reimplement the parse — the script handles frontmatter, aliases, billing and retired filtering.

Retired clients are excluded by the script. For `/slack-attack <slug>` on a retired client, print one line and stop:

```
<slug> — retired since <retired_at> (<retired_reason>). Edit frontmatter to re-activate.
```

## Probe-skip pre-flight

Most clients are quiet most days; a subagent just to discover that is the dominant waste. For each candidate:

1. Read frontmatter: `last_catchup`, `channels`. If `last_catchup` is null, the dossier lacks `## Streams` (legacy), or it has no `channels:` → **don't probe**; dispatch.
2. For each channel ID in `channels` (minus the skip list in `.claude/docs/slack-conventions.md`): `slack_read_channel(channel_id, oldest=<last_catchup unix>, limit=20)`. On any API error → dispatch.
3. Count messages with neither `subtype` nor `bot_id` set.
4. Total 0 → probe-skip; otherwise dispatch.

Probe-skip action (the only dossier write this skill makes): edit the `last_catchup:` line to the current UTC ISO time (from `date -u +%FT%TZ`), then

```bash
git add clients/<slug>.md && git commit -m "chore(catchup): bump <slug> (probe-skip, no activity)"
```

Retry on `.git/index.lock` (sleep 3, up to 5 times). Known acceptable miss: a notable bot-only message — alert channels are on the skip list anyway.

## Dispatch

Print one line up front: which slugs are dispatched, which probe-skipped.

Dispatch in **waves of up to 6** parallel subagents: all Agent calls for a wave in a single message, foreground (no `run_in_background` — background subagents previously returned before doing any work). `subagent_type: general-purpose`, `model: sonnet`. Prompt:

> Working directory: <repo root>. Run the `catchup` skill for `<slug>`: `Skill(skill="catchup", args="<slug>")`, following it exactly. Other catchups are committing to this repo in parallel; retry on `.git/index.lock` as the skill says. When done, paste the catchup output verbatim and stop. No prose digest.

Wait for the wave to finish, then dispatch the next. When all waves are done, synthesise.

If a subagent returns an ABORT or no `Commit:` line, record its output verbatim for the brief's failures paragraph; don't retry in this run.

## Reading results

For each dispatched client, from the subagent's `Commit:` SHA:

1. `git show <sha> --format=%B -s` → the `streams:` trailer: the **complete list** of what the brief may cover for that client.
2. `git show <sha> -- clients/<slug>.md` → the diff: the new State / Next / Refs for each listed stream, and Now/Arc changes.
3. Streams not in the trailer are **silent** in the brief, however open or recent.
4. Legacy conversions (`refactor(dossiers): convert …`) rebuild the whole file: brief only from the streams whose `last` falls inside the reported window, plus one sentence on the conversion itself (streams created, entries dropped as stale).

## Window-anchor sanity check

Use only the window the subagent reported (not your own date math, not the bumped `last_catchup`). For every permalink you cite as `[N]`, decode the first 10 digits of `p<TS>` to Unix seconds; it must be ≥ `window_oldest_unix - 60`. A link outside the window means drop the paragraph.

## Output

Per client, natural-language prose with numbered **bare-URL** references, one paragraph per stream that matters:

```
**<client>**

<Lead: the shape of the window — what dominated. Skip if one stream.>

<One paragraph per stream: who/what/status in plain English, then detail. [N] inline.>
[N] https://mahifx.slack.com/archives/.../p...
```

Rules:

- **One stream per paragraph.** Don't chain unrelated topics with "meanwhile".
- **Plain-English lead.** The first sentence of each paragraph must make sense to someone away for a week: who, what, status. Acronyms only after the topic is anchored, with the surrounding words making their role legible ("the LR throttle on B_CLIENTS_RA").
- **Status through verbs**, not markers: "got closed", "is still being debugged", "is waiting on Gerard".
- **Closed streams** get one sentence ("the MT4 bridge question closed when Base confirmed decommission").
- **Bare URLs only**, each on its own line under its paragraph. `[N]` inline. Numbering resets per client.
- **Don't restate upstream refs** (hosts, commercial terms, party names).
- Test: read each paragraph's first sentence in order — that alone should give the shape of the day.

Multi-client: order client sections by **significance**, not staleness — direct mentions of the user, escalations and real decisions first. Low-key clients get one short paragraph mid-brief. Truly quiet clients (probe-skipped or quiet window) collapse into one final line:

```
Quiet today (N): slug, slug, ...
```

Then, if any subagent aborted or failed, a closing paragraph with their output verbatim.

## Tone

Terse, no preamble, lead with what's hot. Past tense for what happened, present for what's still rough, future for what's coming. Don't speculate past what the thread says.

## What this skill does NOT do

- Pull Slack for content (the probe only counts messages).
- Edit dossier bodies — catchup owns them. The only write is the probe-skip `last_catchup` bump.
- Write outside this repo, or push (the routine pushes).

## Constraints

- Never fabricate a permalink; cite only links present in the commit diff.
- Every paragraph traces to a stream in that commit's `streams:` trailer.
- Match length to activity.
````

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/slack-attack/SKILL.md
git commit -m "feat(slack-attack): process all due clients in waves of six"
```

---

### Task 8: weekly-overview, docs, cleanup

**Files:**
- Modify: `.claude/skills/weekly-overview/SKILL.md`, `.claude/docs/slack-conventions.md`, `CLAUDE.md`
- Delete: `.claude/skills/backfill/`, `todo.md`

- [ ] **Step 1: weekly-overview — replace the "## Source" numbered list (steps 1–4) with:**

```markdown
1. Anchor the window from bash (see "Window-anchor sanity check" below). Default: the previous seven full days ending at today 00:00 UTC.
2. `git log --since="<window-start>" --until="<window-end>" --format='%H%x09%ad%x09%s%n%b' --date=short -- clients/ channels/` to enumerate commits and their bodies.
3. Skip probe-skip/quiet bumps and `refactor(dossiers): convert …` commits (conversions rebuild whole files and would restate history). For each remaining commit, read its `streams:` trailer and `git show <sha> -- <dossier>` for the touched streams' new State / Next / Refs.
4. Group by client, then by stream ID. A stream touched on 3+ distinct days is a multi-day arc; a stream that went `new` → `closed` inside the week is usually daily-brief material, not weekly.
```

and in "What's major", replace the bullet starting `**Multi-day arcs**` with:

```markdown
- **Multi-day arcs** — the same stream ID appears in `streams:` trailers on several days. One spike is a daily-brief paragraph; the same stream moving across three days is a weekly story.
```

- [ ] **Step 2: Delete backfill and todo**

```bash
git rm -rq .claude/skills/backfill todo.md
```

(If the Bash sandbox blocks `.claude/skills`, run that one command with the sandbox disabled — it only deletes tracked files in this repo.)

- [ ] **Step 3: slack-conventions.md** — replace the `## Known channel IDs` section heading and intro line with:

```markdown
## Known channel IDs (legacy — delete after conversion)

Channel IDs now live in each dossier's `channels:` frontmatter. Legacy conversion reads this table once; remove it when every dossier is converted (plan Task 12).
```

Leave the table rows as they are for now.

- [ ] **Step 4: CLAUDE.md** — apply these edits:

1. In the numbered list near the top, replace item 1 with:

   ```markdown
   1. **Client / channel dossiers** (`clients/<slug>.md`, `channels/<name>.md`) — Slack-derived **current state** per target, read by agents in this repo (not humans): `## Now` (≤4 lines), `## Streams` (one `### <id> — <title>` per ongoing topic with status/since/last, a rewritten State, Next, 1–4 permalinks), `## Arc` (one line per relationship milestone), plus pointers to canonical data elsewhere. Git is the event log; the dossier holds only what's current.
   ```

2. In the skills list, delete the `/backfill` bullet and change the `/slack-attack` bullet's last sentence to: `With no slug it processes every due client (scripts/rank-clients --due) in waves of six parallel catchups and produces one brief.`
3. Replace the whole `## Dossier discipline` section with:

   ```markdown
   ## Dossier discipline

   Format contract: `docs/superpowers/specs/2026-10-14-stream-dossiers-design.md`; enforced by `scripts/check-dossiers` (pre-commit). The `catchup` skill holds the working rules.

   - `/catchup` edits one dossier and commits it itself, with a `streams:` trailer listing every stream touched (`new | updated | closed | watching | merged>ID | pruned`).
   - Streams are rewritten in place, never appended to. Stream IDs are permanent. Open streams quiet >30d (watching >60d) must be explicitly reviewed each catchup. Closed streams are pruned by `scripts/prune-dossiers` 14 days after closing.
   - `/slack-attack` probe-skips clients with zero human messages since `last_catchup`, committing `chore(catchup): bump <slug> (probe-skip, no activity)`.
   - `last_catchup` is the source of truth for where we left off. Catchup refuses windows >90 days, so a client left untouched for 90 days needs a manual reset.
   - Don't store anything one read of VibePulse / MahiProduct / Slack returns; store the synthesis plus permalinks.
   - Bootstrap: `/catchup <slug>` creates a missing dossier from the template.

   ### Stream history

   - `git log --grep='<id>' -- clients/<slug>.md` — every run that touched a stream.
   - `git log -L '/^### <id> /,/^### /:clients/<slug>.md'` — how its text evolved.
   - `git log -S'### <id> ' -- clients/<slug>.md` — when it was created / pruned.
   ```

4. In `## Source-of-truth boundary`, replace the rules bullets about `key_people_overrides` and the `## Status` section with:

   ```markdown
   - `contacts` (frontmatter) holds only external people not in `../MahiProduct/wiki/people/`.
   - Never write to `../MahiProduct/` or `../VibePulse/` — read-only sources. This repo is for individual use and writes nowhere else.
   ```

5. In `## Layout`, replace the skills block with:

   ```
     skills/
       catchup/          /catchup <target>         — worker, updates one dossier's streams + commits
       slack-attack/     /slack-attack [slug]      — orchestrator + reader-facing brief
       weekly-overview/  /weekly-overview          — Monday prose digest from the week's streams: trailers
   ```

   and add under `scripts/` a line: `scripts/   dossierlib.py, check-dossiers, prune-dossiers, rank-clients; tests in scripts/tests/`.
6. In `## Setup`, replace the `pre-commit` bullet with: `- **pre-commit** — runs scripts/check-dossiers --staged: stream format, 15KB cap, stream-ID stability, and the year-off date guard. Tests: python3 -m unittest discover -s scripts/tests.`

- [ ] **Step 5: Verify no stale references**

Run: `grep -rnE 'check-dossier-dates|/backfill|Recent issues|key_people_overrides' CLAUDE.md .claude/skills .claude/docs .githooks scripts`
Expected: hits only in `.claude/skills/catchup/SKILL.md` (Legacy conversion section), `scripts/dossierlib.py` (legacy constants) and `scripts/tests/helpers.py` (`LEGACY` fixture).

- [ ] **Step 6: Commit**

```bash
git add -A CLAUDE.md .claude/skills/weekly-overview/SKILL.md .claude/docs/slack-conventions.md
git commit -m "docs: document stream dossiers and retire backfill"
```

---

### Task 9: Routine prompt (repo file only)

**Files:**
- Modify: `.claude/routines/slack-attack-daily.md`

- [ ] **Step 1: Replace step 3** with:

```markdown
3. Catch up all due clients. Invoke /slack-attack (no arg) **once**. It runs `scripts/rank-clients --due`, probe-skips quiet clients, dispatches the rest in waves of up to 6 parallel catchup subagents, and returns one globally ordered brief.
```

- [ ] **Step 2: Replace step 4** with:

```markdown
4. Collect, don't send. Capture the brief. Each client section (`**<client>**` header through its references) is already in significance order; the `Quiet today` line and any failures paragraph come at the end. Don't send anything to Slack yet.
```

- [ ] **Step 3: In step 6**, change the run-stats line to `run stats: dispatched D, probe-skipped P, streams +N ~U ✓C, weekly Y|N|-, wall ~Mm` and replace the run-stats bullets with:

```markdown
   - `git log --format='%s%n%b' ${RUN_START_SHA}..HEAD` lists every commit and trailer this run produced.
   - P = commits whose subject contains `(probe-skip`.
   - D = remaining `chore(catchup):` and `refactor(dossiers): convert` commits.
   - N / U / C = counts of `(new)`, `(updated)`, `(closed)` across all `streams:` trailer lines.
   - M = round((now_unix - RUN_START_TS) / 60).
   - weekly indicator: `-` for non-Mondays; `Y`/`N` filled in by step 9 on Mondays.
```

and in the step 6 template remove the `<If you stopped at the batch cap: …>` line.

- [ ] **Step 4: In step 8**, change the stats line to `quiet: N · dispatched D · probe-skipped P · wall ~Mm`.

- [ ] **Step 5: Commit** (do NOT push to the remote routine yet — Task 13)

```bash
git add .claude/routines/slack-attack-daily.md
git commit -m "feat(routine): single slack-attack pass over all due clients"
```

---

### Task 10: Pilot conversion — amana + axiory (CHECKPOINT)

- [ ] **Step 1:** Record `PILOT_BASE=$(git rev-parse HEAD)`. Dispatch two catchup subagents **in one message** (exercises the index.lock retry), `model: sonnet`, prompt as in the slack-attack skill's Dispatch section, for `amana` and `axiory`. Both dossiers are legacy, so catchup runs Legacy conversion over the 2026-08-17 → now window.
- [ ] **Step 2: Verify**

```bash
git log --oneline ${PILOT_BASE}..HEAD
scripts/check-dossiers clients/amana.md clients/axiory.md; echo exit=$?
wc -c clients/amana.md clients/axiory.md
git show --format=%B -s HEAD~1 HEAD
```

Expected: two `refactor(dossiers): convert …` commits; `exit=0`; amana ≤15360 bytes (target ≤10240); bodies carry `streams:`, `dropped:` and `stale:` lines.

- [ ] **Step 3: STOP — review with the user.** Show both dossiers and the `stale:` drop lists. Ask: is stream granularity right, did anything important get dropped, is Now useful? Apply any agreed changes to the catchup skill (and re-run a conversion if needed) before Task 11.

---

### Task 11: Convert everything else, bootstrap kama-capital

- [ ] **Step 1:** Run `/slack-attack` (no arg). Every remaining legacy dossier is due and unprobeable, so all get dispatched in waves of 6; kama-capital is bootstrapped (it's in `rank-clients --due` as `never`).
- [ ] **Step 2:** Convert `channels/dev.md` with `/catchup dev`. Its `last_catchup` (2026-04-27) is beyond the 90d cap: first set its frontmatter `last_catchup: null` (30d bootstrap window), commit as `chore(dossiers): reset dev channel window`, then run the catchup.
- [ ] **Step 3: Verify**

```bash
scripts/check-dossiers clients/*.md channels/*.md; echo exit=$?
grep -L '^## Streams' clients/*.md channels/*.md | grep -v _template
scripts/rank-clients --due
```

Expected: `exit=0`; the `grep -L` prints only retired dossiers (easton, errante, finotive, fundingpips, ig); `--due` prints nothing (or only clients whose catchup aborted — rerun those individually).

Retired dossiers stay legacy (frozen record; catchup never touches them).

---

### Task 12: Remove legacy mode

**Files:**
- Modify: `.claude/skills/catchup/SKILL.md`, `.claude/skills/slack-attack/SKILL.md`, `.claude/docs/slack-conventions.md`, `scripts/dossierlib.py`, `scripts/tests/test_checks.py`, `scripts/tests/test_prune.py`, `scripts/tests/helpers.py`

- [ ] **Step 1: Test first** — in `scripts/tests/test_checks.py` replace `test_legacy_routes_to_old_check` with:

```python
    def test_non_retired_legacy_rejected(self):
        self.assertTrue(any("## Streams" in e for e in errors(LEGACY)))

    def test_retired_legacy_ignored(self):
        retired = LEGACY.replace("slug: x\n", "slug: x\nstatus: retired\n")
        self.assertEqual(run(retired), ([], []))
```

Run: `python3 -m unittest discover -s scripts/tests -v` → the first new test FAILS.

- [ ] **Step 2: Implement** — in `scripts/dossierlib.py`, delete the `# --- legacy …` block (`LEGACY_*` constants and `legacy_violations`), and replace the first lines of `check` with:

```python
    p = d.path
    if d.legacy:
        if re.search(r"^status: retired\b", d.frontmatter, re.M):
            return [], []
        return [f"{p}: missing ## Streams section — not in stream format"], []
```

- [ ] **Step 3:** Run tests → all OK. Run `scripts/check-dossiers clients/*.md channels/*.md` → exit 0.
- [ ] **Step 4: Skills/docs** — delete the `## Legacy conversion …` section and the "Dossier has no `## Streams` section → it's legacy" bullet from `catchup/SKILL.md`, and "(30 in a legacy conversion)" from its work budget; delete the "the dossier lacks `## Streams` (legacy)," clause and step 4 of "Reading results" from `slack-attack/SKILL.md`; delete the whole `## Known channel IDs (legacy …)` section from `.claude/docs/slack-conventions.md`.
- [ ] **Step 5: Commit**

```bash
git add -A scripts .claude/skills .claude/docs
git commit -m "refactor(catchup): drop legacy dossier conversion"
```

---

### Task 13: Ship — push, update and enable the routine (needs user go-ahead)

- [ ] **Step 1:** Ask the user to confirm pushing `main` and re-enabling the routine (outward-facing). Then `git push origin main` (SSH needs the sandbox disabled).
- [ ] **Step 2:** Per `CLAUDE.md` "Remote routines": `RemoteTrigger get trig_01SVZcK2nQJkRv1YWcHRwdbK`; `RemoteTrigger update` with the existing `job_config`, replacing only `events[0].data.message.content` with the routine file body (everything after the second `---` line's intro paragraph), plus `"enabled": true`.
- [ ] **Step 3:** Re-fetch and diff the remote prompt against the file; confirm `enabled: true` and `next_run_at` is the next weekday 07:00 UTC. Report both to the user.
- [ ] **Step 4:** Optional cleanup, with the user's OK: `git push origin --delete` the 10 `claude/epic-hawking-*` branches.
