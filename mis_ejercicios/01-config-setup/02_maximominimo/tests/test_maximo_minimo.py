# pylint: disable-all

import unittest
from maximo_minimo import maximominimo

class TestSumOfFour(unittest.TestCase):
    def test_max_1(self):
        self.assertEqual(maximominimo([23, 2, 3, 4, 10]),[19, 40])

    def test_max_2(self):
        self.assertEqual(maximominimo([1, 2, 3, 4, 5]),[10, 14])

    def test_max_3(self):
        self.assertEqual(maximominimo([1, 2, 3, 4, 100]),[10, 109])


