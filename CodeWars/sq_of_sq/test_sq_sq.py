from unittest import TestCase


class Test(TestCase):
    def test_is_square(self):
        from CodeWars.sq_of_sq.sq_sq import is_square
        self.assertEqual(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
        self.assertEqual(is_square(0), True, "0 is a square number")
        self.assertEqual(is_square(3), False, "3 is not a square number")
        self.assertEqual(is_square(4), True, "4 is a square number")
        self.assertEqual(is_square(25), True, "25 is a square number")
        self.assertEqual(is_square(26), False, "26 is not a square number")
        print("ff")
