#!/usr/bin/env python

import unittest
from main import roman
from main import PIRVal

class TestPIRVal(unittest.TestCase):
    def test_one_returned_when_given_1_and_2_with_max_of_1(self):
        self.assertEqual(1,PIRVal([1,2], 1))

    def test_2_returned_when_given_1_and_2_with_max_of_2(self):
        self.assertEqual(2,PIRVal([1,2], 2))

    def test_5_returned_when_given_1_and_5_and_10_with_max_of_7(self):
        self.assertEqual(5,PIRVal([1,5,10], 7))

class TestRoman(unittest.TestCase):

    def test_1(self):
        self.assertEqual("I", roman(1))

    def test_2(self):
        self.assertEqual("II",roman(2))

    def test_3(self):
        self.assertEqual("III",roman(3))

    def test_4(self):
        self.assertEqual("IV",roman(4))

    def test_5(self):
        self.assertEqual("V",roman(5))

    def test_6(self):
        self.assertEqual("VI",roman(6))

    def test_7(self):
        self.assertEqual("VII",roman(7))

    def test_8(self):
        self.assertEqual("VIII",roman(8))

    def test_9(self):
        self.assertEqual("IX",roman(9))

    def test_10(self):
        self.assertEqual("X",roman(10))

    def test_11(self):
        self.assertEqual("XI",roman(11))

if __name__ == '__main__':
    unittest.main()
