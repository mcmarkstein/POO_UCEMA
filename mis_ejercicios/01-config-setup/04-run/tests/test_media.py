# pylint: disable-all

import unittest
from media import calculate_mean

class TestSumOfFour(unittest.TestCase):
    def test_mean_10(self):
        self.assertEqual(calculate_mean([10,10,10,10]), 10)

    def test_mean_2(self):
        self.assertEqual(calculate_mean([1, 2, 3, 4]), 2.5)

    def test_mean_20(self):
        self.assertEqual(calculate_mean([23, 44, 12, 3]), 20.5)
