# task 2
import string
import sys

sys.stdin = open("input2.txt", "r")


class Hierarchy:
    dictinary_classes = {}
    all_parents = []
    lst_res = ""
    list_new_exception = []

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

    def my_input_frankenstein(self):
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
            my_str = sys.stdin.readline().split('\n')
            object_hierarchy.is_base_of(my_str[0], my_str[0])
            self.list_new_exception += my_str

            fl = 0
            #  if from all parent is being collision from already geted exception then not work with him
            for parent in self.all_parents:
                for exeption in self.list_new_exception:
                    if parent == exeption and fl == 0:
                        print(''.join(my_str))
                        fl = 1

            self.all_parents.clear()  # clear list after query


object_hierarchy = Hierarchy()
object_hierarchy.my_input_frankenstein()


# object_hierarchy.print()

# task 3
class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError


# lst = PositiveList()
# lst.append(4)
# lst.append(-3)

# task 1
def foo():
    pass


try:
    foo()
except ZeroDivisionError:
    print(type(ZeroDivisionError()).__name__)
except ArithmeticError:
    print(type(ArithmeticError()).__name__)
except AssertionError:
    print(type(AssertionError()).__name__)
