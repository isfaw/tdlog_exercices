def solution(string, ending):
    return string.endswith(ending)
import unittest

class TestSolution(unittest.TestCase):

    def test_fixed_tests_true(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )
        for s, e in fixed_tests_True:
            with self.subTest(s=s, e=e):
                self.assertTrue(solution(s, e))

    def test_fixed_tests_false(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )
        for s, e in fixed_tests_False:
            with self.subTest(s=s, e=e):
                self.assertFalse(solution(s, e))

if __name__ == "__main__":
    unittest.main()
