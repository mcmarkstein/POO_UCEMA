# pylint: disable-all

import unittest
from suma_simple import sum4

class TestSumOfFour(unittest.TestCase):
    def test_numbers_0_0_0(self):
        self.assertEqual(sum4(0, 0, 0, 0), 0)

    def test_numbers_1_2_3(self):
        self.assertEqual(sum4(1, 2, 3, 4), 10)

    def test_numbers_4_5_6(self):
        self.assertEqual(sum4(4, 5, 6,7), 22)

    def test_with_negative_numbers(self):
        self.assertEqual(sum4(-1, 1, 1, -1), 0)
