import unittest
from error_handling import explain, retryable

class T(unittest.TestCase):
    def test_documented(self):
        for c in (400, 401, 403, 404, 463, 500):
            self.assertNotIn("Undocumented", explain(c))
    def test_unknown(self):
        self.assertIn("Undocumented", explain(418))
    def test_retry(self):
        self.assertTrue(retryable(500)); self.assertFalse(retryable(401))

if __name__ == "__main__":
    unittest.main()
