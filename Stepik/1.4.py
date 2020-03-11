import sys

sys.stdin = open("input_namespaces.txt", "r")


def my_namespaces():

    #  Словари в словаре , ключ по сути namespace , а lst его область видимости
    dict_nspaces = {"global": []}
    # dict_nspaces["global"].append({"foo": []})  # TEST add
    n = int(sys.stdin.readline())
    for i in range(n):
        line = sys.stdin.readline().split()
        if line[0] == 'add':
            add(dict_nspaces, line[1], line[2])
        elif line[0] == 'create':
            create(dict_nspaces, line[1], line[2])
        elif line[0] == 'get':
            print(get(dict_nspaces, line[1], line[2]))
            # pass
    print(dict_nspaces)
    return 0

#  Иду по всем ключам и значениям, из значений ищу словарь и иду потов по нему --> захожу вглубь (рекурсией)
def add(dict_nspaces, namespace, adder):
    for k, lst_val in dict_nspaces.items():
        for el in lst_val:
            if type(el) == dict:
                add(el, namespace, adder)
        if namespace == k:
            dict_nspaces[namespace].append(adder)


def create(dict_nspaces, namespace, where):
    for k, lst_val in dict_nspaces.items():
        for el in lst_val:
            if type(el) == dict:
                create(el, namespace, where)
        if where == k:
            dict_nspaces[where].append({namespace: []})


j = []
def get(dict_nspaces, namespace, var):
    for k, lst_val in dict_nspaces.items():
        for el in lst_val:
            j.append(k)
            if el == var:
                return j
            if type(el) == dict:
                # print(namespace)
                get(el, namespace, var)


my_namespaces()