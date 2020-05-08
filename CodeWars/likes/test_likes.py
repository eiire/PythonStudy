from unittest import TestCase


class Test(TestCase):
    def test_likes(self):
        from CodeWars.likes.likes import likes
        self.assertEquals(likes([]), 'no one likes this')
        self.assertEquals(likes(['Peter']), 'Peter likes this')
        self.assertEquals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEquals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEquals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
