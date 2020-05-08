from unittest import TestCase


class Test(TestCase):
    def test_josephus(self):
        from CodeWars.Josephus.permutation import josephus
        self.assertEquals(josephus([1,2,3,4,5,6,7,8,9,10],1),[1,2,3,4,5,6,7,8,9,10])
        self.assertEquals(josephus([1,2,3,4,5,6,7,8,9,10],2),[2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
        self.assertEquals(josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
        self.assertEquals(josephus([1,2,3,4,5,6,7],3),[3, 6, 2, 7, 5, 1, 4])
        self.assertEquals(josephus([],3),[])
