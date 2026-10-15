"""Parsing, checks and pruning for stream-format dossiers.

Format contract: docs/superpowers/specs/2026-10-14-stream-dossiers-design.md.
CLIs: scripts/check-dossiers, scripts/prune-dossiers. Stdlib only.
"""

import datetime as dt
import os
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


HARD_BYTES = 20480
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
