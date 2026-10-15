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
