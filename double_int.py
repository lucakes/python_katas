import unittest


def double_integer(i):
    return i * 2


class TestDoubleInteger(unittest.TestCase):
    def test_three_times_two(self):
        result = double_integer(3)
        self.assertEqual(result, 6)
