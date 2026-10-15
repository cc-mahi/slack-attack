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
