import unittest


def string_to_array(s):
    if len(s) == 0:
        return [""]
    return s.split()


class TestSplitWhitespace(unittest.TestCase):
    def test_split_string(self):
        result = string_to_array("Robin Singh")
        self.assertEqual(result, ["Robin", "Singh"])

    def test_split_empty_string(self):
        result = string_to_array("")
        self.assertEqual(result, [""])
