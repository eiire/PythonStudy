# task 1
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
            try:  # X parent X and
                my_str = sys.stdin.readline().split(' ')
                my_str[1] = ''.join(list(filter(lambda ch: ch != '\n', my_str[1])))
            except IndexError:
                my_str += ''.join(list(filter(lambda ch: ch != '\n', my_str[0])))
                my_str[0] = ''.join(list(filter(lambda ch: ch != '\n', my_str[0])))

            check_nonexistent_class = 0
            for key in self.dictinary_classes:
                if my_str[1] == key:
                    check_nonexistent_class = 1

            if my_str[0] == my_str[1]:
                print('Yes')
            elif check_nonexistent_class == 1:
                object_hierarchy.is_base_of(my_str[0], my_str[1])
                fl = 0
                print(self.all_parents)
                for parents in self.all_parents:
                    if my_str[0] == parents and fl != 1:
                        print('Yes')
                        fl = 1
                if fl == 0:
                    print('No')
            else:
                print('No')
                print(self.all_parents)
            self.all_parents.clear()  # clear list after query


object_hierarchy = Hierarchy()
object_hierarchy.my_input_frankenstein()
# object_hierarchy.print()

# task 2
class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())

# object_stack = ExtendedStack()
# object_stack.append(1)
# object_stack.append(2)
# object_stack.sum()
# print(object_stack)
#
# object_stack.append(1)
# object_stack.append(2)
# object_stack.sub()
# print(object_stack)
#
# object_stack.append(1)
# object_stack.append(2)
# object_stack.mul()
# print(object_stack)
#
# object_stack.append(1)
# object_stack.append(2)
# object_stack.div()
# print(object_stack)

# task 3
import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, str):
        super(LoggableList, self).append(str)
        self.log(str)
