"""This problem takes its name by arguably the most important event in the life of the ancient historian Josephus:
according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.

Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and
proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to
end the act)."""


def josephus(items, k):
    new_arr = list()

    while len(items) != 0:
        if k > len(items):
            res = items[k % len(items) - 1]
        else:
            res = items[k - 1]

        items = items[items.index(res):] + items[:items.index(res)]
        items.remove(res)
        new_arr.append(res)

    return new_arr


if __name__ == '__main__':
    print(josephus(["C","o","d","e","W","a","r","s"],4))
