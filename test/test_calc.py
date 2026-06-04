import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sample.calc_num import multiply  # noqa: E402


class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        """掛け算の検証（正数、負数、ゼロ）"""
        test_cases = [
            (2, 3, 6),
            (5, 5, 25),  # 正数
            (-2, 3, -6),
            (5, -5, -25),  # 負数
            (2, 0, 0),
            (0, 5, 0),  # ゼロ
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiply(a, b), expected)


if __name__ == "__main__":
    unittest.main()
