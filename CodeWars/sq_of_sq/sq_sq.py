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
    print(is_square(25))

