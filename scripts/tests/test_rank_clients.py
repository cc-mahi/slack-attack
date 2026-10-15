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
