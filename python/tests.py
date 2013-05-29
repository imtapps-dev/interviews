#!/usr/bin/env python

import unittest
from main import something


class TestSomething(unittest.TestCase):

    def test_fail(self):
        self.assertFalse(something())

    def test_pass(self):
        self.assertTrue(something())


if __name__ == '__main__':
    unittest.main()
