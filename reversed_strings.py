import unittest

def solution(string):
    result = ""
    for element in reversed(range(0, len(string))):
        result = result + string[element]
    return result


class TestReverseStrings(unittest.TestCase):
    def test_reverse_world(self):
        result = solution("world")
        self.assertEqual(result, "dlrow")