from math import sqrt
# from contracts import contract


# @contract
def factorize(x):
    # """
    # Factorize positive integer and return its factors.
    # :type x: int,>=0
    # :rtype: tuple[N],N>0
    # """
    if type(x) != type(int()):
        raise TypeError

    if x < 0:
        raise ValueError

    if x == 0:
        return (0,)

    if x == 1:
        return (1,)

    res_list = []
    j = 2
    while x > 1:
        for i in range(j, int(sqrt(x + 0.05)) + 1):
            if x % i == 0:
                x /= i
                j = i
                res_list.append(int(i))
                break
        else:
            if x > 1:
                res_list.append(int(x))
                break

    return tuple(res_list)


if __name__ == '__main__':
    print(factorize(-1))
