import string
import sys

sys.stdin = open("input.txt", "r")


class Hierarchy:
    dictinary_classes = {}
    all_parents = []
    lst_res = ""

    def add(self, name: string, parents=None) -> None:
        # As the name suggests, <filter> creates a list of elements for which a function returns true.
        if parents is None:
            parents = []
        self.dictinary_classes.update({''.join(list(filter(lambda ch: ch != ' ', name))): parents.split()})

    def is_base_of(self, base: string, derived: string) -> bool:
        self.all_parents += self.dictinary_classes[derived]

        for element_of_child in self.dictinary_classes[derived]:
            self.is_base_of(base, element_of_child)

    def print(self):
        print(self.dictinary_classes)

    def my_input(self):
        n = int(sys.stdin.readline())
        for i in range(n):
            my_str = sys.stdin.readline()
            if my_str.find(':') == -1:
                name = my_str
                object_hierarchy.add(name.replace('\n', ''), '')
            else:
                name, parents = my_str.split(":")
                object_hierarchy.add(name, parents)

        n_2 = int(sys.stdin.readline())
        for i in range(n_2):
            my_str = sys.stdin.readline().split(' ')
            my_str[1] = ''.join(list(filter(lambda ch: ch != '\n', my_str[1])))
            object_hierarchy.is_base_of(my_str[0], my_str[1])
            fl = 0
            print(self.all_parents)
            for parents in self.all_parents:
                if my_str[0] == parents:
                    print('Yes')
                    fl = 1
            if fl == 0:
                print('No')
            self.all_parents = []  # clear list after query


object_hierarchy = Hierarchy()
object_hierarchy.my_input()
object_hierarchy.print()
