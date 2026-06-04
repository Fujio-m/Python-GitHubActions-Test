import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sample.sub_num import sub  # noqa: E402


class TestSubCalculator(unittest.TestCase):
    def test_sub(self):
        """引き算の検証（正常系・負の数）"""
        for a, b, expected in [(5, 3, 2), (2, 5, -3)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(sub(a, b), expected)


if __name__ == "__main__":
    unittest.main()
