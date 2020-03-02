import string
from typing import List
import sys
import sys

sys.stdin = open("input.txt", "r")


class Hierarchy:
    dictinary_classes = {}

    def add(self, name: string, parents=None) -> None:
        # As the name suggests, <filter> creates a list of elements for which a function returns true.
        if parents is None:
            parents = []
        self.dictinary_classes.update({''.join(list(filter(lambda ch: ch != ' ', name))): parents.split()})

    def is_base_of(self, base: string, derived: string) -> bool:
        for key in self.dictinary_classes:
            if key == derived:  # don`t understand why need derived[0] but derived don`t work
                for word in self.dictinary_classes[key]:
                    if word == base:
                        return 'Yes'
        return 'No'

    def print(self):
        print(self.dictinary_classes)


object_hierarchy = Hierarchy()


def my_input():
    n = int(sys.stdin.readline())
    for i in range(n):
        my_str = sys.stdin.readline()
        if my_str.find(':') == -1:
            name = my_str
            object_hierarchy.add(name.replace('\n', ''), 'None')
        else:
            name, parents = my_str.split(":")
            object_hierarchy.add(name, parents)

    n_2 = int(sys.stdin.readline())
    for i in range(n_2):
        my_str = sys.stdin.readline().split(' ')
        my_str[1] = ''.join(list(filter(lambda ch: ch != '\n', my_str[1])))
        print(object_hierarchy.is_base_of(my_str[0], my_str[1]))


my_input()
