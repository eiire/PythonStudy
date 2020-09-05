from unittest import TestCase


class Test(TestCase):
    def test_josephus(self):
        from CodeWars.kyu_5.tasks import josephus
        self.assertEquals(josephus([1,2,3,4,5,6,7,8,9,10],1),[1,2,3,4,5,6,7,8,9,10])
        self.assertEquals(josephus([1,2,3,4,5,6,7,8,9,10],2),[2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
        self.assertEquals(josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
        self.assertEquals(josephus([1,2,3,4,5,6,7],3),[3, 6, 2, 7, 5, 1, 4])
        self.assertEquals(josephus([],3),[])

    def test_anangrams(self):
        from CodeWars.kyu_5.tasks import anagrams
        self.assertEquals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEquals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])

    def test_make_readeble(self):
        from CodeWars.kyu_5.tasks import make_readable
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(5), "00:00:05")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")

    def test_pig_it(self):
        from CodeWars.kyu_5.tasks import pig_it
        self.assertEquals(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        self.assertEquals(pig_it('This is my string'), 'hisTay siay ymay tringsay')