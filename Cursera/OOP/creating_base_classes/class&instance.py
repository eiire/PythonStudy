""" Checked same theory"""


class F:
    def __init__(self, data):
        self.data = data


class L:
    data = 0


if __name__ == '__main__':
    """ my mini_tests (different self.data and data from class) """
    F.data = 1
    f = F(2)  # data from instance
    l = L()
    print(l.data, "data from class")
    l.data = 3
    print(l.data, "data from instance")
    print(L.data, "changed data from class")
    F.data = 1  # data from class
    print(F.data, "data from class")
    print(f.data, "data from instance")
    m = F(5)  # data changed only from instance (not class), because "self.data" (!)
    print(m.data, "data from instance")  # data from instance
    print(F.data, "data from class")  # data from class
    print(L.data, "data from class before change data(class`s)")
    L.data = 4
    g = L
    print(g.data, "data from class after change data(class`s)")