import unittest


def even_or_odd(number):
    if (number % 2) == 0:
        return "Even"
    else:
        return "Odd"


class TestEvenOrOdd(unittest.TestCase):
    def test_two_is_even(self):
        result = even_or_odd(2)
        self.assertEqual(result, "Even")

    def test_three_is_odd(self):
        result = even_or_odd(3)
        self.assertEqual(result, "Odd")
