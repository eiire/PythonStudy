import string
from typing import List
import sys


class Hierarchy:
    dictinary_classes = {}

    def add(self, name: string, parents: List = []) -> None:
        # As the name suggests, <filter> creates a list of elements for which a function returns true.
        self.dictinary_classes.update({''.join(list(filter(lambda ch: ch!=' ', name))): parents.split()})

    def is_base_of(self, base: string, derived: string) -> bool:
        #  algorithm
        pass

    def print(self):
        print(self.dictinary_classes)


object_hierarchy = Hierarchy()


n = int(sys.stdin.readline())


def my_input(n):
    for i in range(n):
        my_str = sys.stdin.readline()
        if my_str.find(':') == -1:
            name = my_str
            object_hierarchy.add(name.replace('\n', ''), '')
        else:
            name, parents = my_str.split(":")
            object_hierarchy.add(name, parents)


my_input(n)


object_hierarchy.print()