"""
Define a function that takes an integer argument and returns logical value true or false depending on if the integer
is a tasks.py. O(sqrt(n)).
"""


def is_prime(n):
    d = 2
    if n <= 0 or n == 1: return False
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


"""
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays 
have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the 
elements in a squared, regardless of the order.
"""


def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    elif len(array1) == 0 or len(array2) == 0:
        if len(array1) == 0 and len(array2) == 0:
            return True
        return False
    else:
        for el in array1:
            if el * el not in array2:
                return False

            if el * el in array2:
                array2.remove(el * el)

        return True


"""You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures 
or other items. We want to create the text that should be displayed next to such an item."""


def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


"""
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
"""


def is_square(n):
    i = 0

    if n < 0:
        return False

    while True:
        if i * i == n:
            return True

        if i * i > n:
            return False

        i = i + 1


if __name__ == '__main__':
    # print(is_prime(4))
    pass