import unittest
import re


def the_method(arg):
    if ',' in arg:
        return sum(int(i) for i in re.split('[^\d]', arg))
    if len(arg) > 0:
        return int(arg)
    return 0


class Tests(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        result = the_method("")
        self.assertEqual(0, result)

    def test_single_number_is_returned(self):
        result = the_method("31")
        self.assertEqual(31, result)

    def test_comma_separated_numbers_returns_sum(self):
        result = the_method("1,2")
        self.assertEqual(3, result)

    def test_unknown_number_of_comma_separated_numbers_returns_sum(self):
        result = the_method("1,2,3,4,5,6")
        self.assertEqual(21, result)

    def test_unknown_delimiters(self):
        result = the_method("1|2,3\n4A5~6")
        self.assertEqual(21, result)

    def test_unknown_delimiters_without_comma(self):
        result = the_method("1|2^3\n4A5~6")
        self.assertEqual(21, result)
