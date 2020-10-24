from unittest import TestCase


class Test(TestCase):
    def test_solve_task(self):
        from CodeWars.kyu_4.strip_comments import solve
        self.assertEqual(solve.solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
        self.assertEqual(solve.solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
        self.assertEqual(solve.solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
