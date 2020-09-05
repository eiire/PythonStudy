from unittest import TestCase


class self(TestCase):
    def test_basic(self):
        from CodeWars.kyu_6.tasks import is_prime
        self.assertEquals(is_prime(0),  False, "0  is not tasks.py")
        self.assertEquals(is_prime(1),  False, "1  is not tasks.py")
        self.assertEquals(is_prime(2),  True, "2  is tasks.py")
        self.assertEquals(is_prime(73), True, "73 is tasks.py")
        self.assertEquals(is_prime(75), False, "75 is not tasks.py")
        self.assertEquals(is_prime(-1), False, "-1 is not tasks.py")
        self.assertEquals(is_prime(3),  True, "3  is tasks.py")
        self.assertEquals(is_prime(5),  True, "5  is tasks.py")
        self.assertEquals(is_prime(7),  True, "7  is tasks.py")
        self.assertEquals(is_prime(41), True, "41 is tasks.py")
        self.assertEquals(is_prime(5099), True, "5099 is tasks.py")
        self.assertEquals(is_prime(4),  False, "4  is not tasks.py")
        self.assertEquals(is_prime(6),  False, "6  is not tasks.py")
        self.assertEquals(is_prime(8),  False, "8  is not tasks.py")
        self.assertEquals(is_prime(9), False, "9 is not tasks.py")
        self.assertEquals(is_prime(45), False, "45 is not tasks.py")
        self.assertEquals(is_prime(-5), False, "-5 is not tasks.py")
        self.assertEquals(is_prime(-8), False, "-8 is not tasks.py")
        self.assertEquals(is_prime(-41), False, "-41 is not tasks.py")

    def test_comp(self):
        from CodeWars.kyu_6.tasks import comp
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertEquals(comp(a1, a2), True)

    def test_likes(self):
        from CodeWars.kyu_6.tasks import likes
        self.assertEquals(likes([]), 'no one likes this')
        self.assertEquals(likes(['Peter']), 'Peter likes this')
        self.assertEquals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEquals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEquals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

    def test_is_square(self):
        from CodeWars.kyu_6.tasks import is_square
        self.assertEqual(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
        self.assertEqual(is_square(0), True, "0 is a square number")
        self.assertEqual(is_square(3), False, "3 is not a square number")
        self.assertEqual(is_square(4), True, "4 is a square number")
        self.assertEqual(is_square(25), True, "25 is a square number")
        self.assertEqual(is_square(26), False, "26 is not a square number")

    def test_in_array(self):
        from CodeWars.kyu_6.tasks import in_array
        a1 = ["live", "arp", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        self.assertEquals(in_array(a1, a2), r)
        self.assertEquals(in_array(['duplicates', 'duplicates'], ['duplicates', 'duplicates']), ['duplicates'])

    def test_bouncingBall(self):
        from CodeWars.kyu_6.tasks import bouncingBall
        self.assertEqual(bouncingBall(3, 0.66, 1.5), 3)
        self.assertEqual(bouncingBall(30, 0.66, 1.5), 15)
        self.assertEqual(bouncingBall(30, 0.75, 1.5), 21)