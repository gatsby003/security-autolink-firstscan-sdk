import json
from pathlib import Path
import unittest
from tenant_auth import require_tenant_access

class TenantAccessTests(unittest.TestCase):
    def test_synthetic_tenant_boundaries(self):
        cases = json.loads(Path(__file__).with_name("tenant_access_cases.json").read_text())
        for case in cases:
            with self.subTest(case_id=case["case_id"]):
                self.assertTrue(require_tenant_access(case["actor"], case["allowed_tenant_id"]))
                with self.assertRaises(PermissionError):
                    require_tenant_access(case["actor"], case["denied_tenant_id"])
    def test_missing_actor(self):
        with self.assertRaises(PermissionError):
            require_tenant_access(None, "synthetic-tenant")

if __name__ == "__main__":
    unittest.main()
