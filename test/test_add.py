import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sample.add_num import add  # noqa: E402

class TestAddCalculator(unittest.TestCase):
    def test_add(self):
        """足し算の検証（正常系・負の数）"""
        for a, b, expected in [(2, 3, 5), (2, -3, -1)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

if __name__ == "__main__":
    unittest.main()
