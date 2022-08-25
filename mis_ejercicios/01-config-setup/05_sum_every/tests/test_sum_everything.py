# pylint: disable-all

import unittest
from sum_everything import sum_every

class TestSumOfFour(unittest.TestCase):
    def test_sumeve_13(self):
        self.assertEqual(sum_every(5, 3.8, 5), 13.8)

    def test_sumeve_13(self):
        self.assertEqual(sum_every(1, 2, 3, 4), 10)

    def test_sumeve_13(self):
        self.assertEqual(sum_every(23, 44, 12, 3), 100)


