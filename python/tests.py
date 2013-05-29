#!/usr/bin/env python

import unittest


class Tests(unittest.TestCase):

    def test_fail(self):
        self.fail("Write a Test")


if __name__ == '__main__':
    unittest.main()
