import unittest
import re

class TestSecurity(unittest.TestCase):
    def test_no_sensitive_paths_in_per_security_ws(self):
        """Ensure PerSecurityWS.py does not leak local workstation paths or user directories."""
        with open('PerSecurityWS.py', 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for local Windows or Unix workstation user paths
        match_win = re.search(r'[C-Z]:\\Users\\', content, re.IGNORECASE)
        match_unix = re.search(r'/home/[a-zA-Z0-9_-]+/', content)

        self.assertIsNone(match_win, "PerSecurityWS.py contains hardcoded local Windows user path")
        self.assertIsNone(match_unix, "PerSecurityWS.py contains hardcoded local Unix user path")

if __name__ == '__main__':
    unittest.main()
