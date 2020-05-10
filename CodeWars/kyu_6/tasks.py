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


"""
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are 
substrings of strings of a2.
"""


def in_array(a1, a2):
    res_list = list()
    for el_a1 in a1:
        for el_a2 in a2:
            if el_a2.count(el_a1) > 0:
                if el_a1 not in res_list:
                    res_list.append(el_a1)
                res_list.sort()
                break

    return res_list


"""
A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
"""


def bouncingBall(h, bounce, window):
    counter = 1
    if h <= 0 or (bounce <= 0 or bounce >= 1) or window >= h:
        return -1
    new_height = h * bounce
    while new_height > window:
        new_height *= bounce
        counter+=2

    return counter



if __name__ == '__main__':
    # print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
    # print(bouncingBall(30, 0.75, 1.5))
    pass