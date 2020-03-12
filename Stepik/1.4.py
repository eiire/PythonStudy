import sys

sys.stdin = open("input_namespaces.txt", "r")

fl = 0
fl_2 = 0


def my_namespaces():
    #  Словари в словаре , ключ по сути namespace , а lst его область видимости
    dict_nspaces = {"global": []}
    # dict_nspaces["global"].append({"foo": []})  # TEST add
    n = int(sys.stdin.readline())
    for i in range(n):
        global fl
        global fl_2
        line = sys.stdin.readline().split()
        if line[0] == 'add':
            add(dict_nspaces, line[1], line[2])
        elif line[0] == 'create':
            create(dict_nspaces, line[1], line[2])
        elif line[0] == 'get':
            get(dict_nspaces, line[1], line[2])
            # if str(dict_nspaces).find(line[2]) == -1:
            #     print('None')

            if fl == 0:
                j(dict_nspaces, line[1], line[2])
                fl = 0

            # elif line[1] == 'global' and (line[2] in dict_nspaces.keys()) == False:
            #     print('None')

            if fl_2 == 0 and fl != 0:
                print('None')
        fl_2 = 0

    print(dict_nspaces)
    return 0

c = 0
def j(dict_nspaces, namespace, adder):
    global c
    for k, el in dict_nspaces.items():
        # print(el)

        try:
            # print(k == namespace, k, namespace)
            # print(type(dict) in el)
            # print(type(dict))
            for e in el:
                if type(e) == dict:
                    # print(dict in list(e.values()))
                    print(e.values())
                    for h in e.values():
                        print(h, "gg")
                        if dict in h:
                            c = 1

            if adder in el and c == 1: #  and namespace == or and dict in el
                print(g, "dd")
                c = 0
        except:
            pass

        for e in el:
            if type(e) == dict:
                j(e, namespace, adder)

# def check_for_exist(dict_nspaces, namespace, adder):
#     for k, lst_val in dict_nspaces.items():
#         for el in lst_val:
#             if adder == el:
#                 yield el
#
#             if type(el) == dict:
#                 check_for_exist(el, namespace, adder)


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


g = ""


def get(dict_nspaces, namespace, var):
    for k, el in dict_nspaces.items():
        global fl
        global fl_2
        for e in el:
            global g
            for g in el:
                try:
                    if g == var:
                        g = k
                except:
                    pass

            # Если во внешнем np есть наше пространство и одновременно переменная, то берем из него переменную
            if type(e) == dict and list(e.keys())[0] == namespace and (var in el):
                print(k)  # <--
                # return k
                fl = 1
                fl_2 = 1

            try:
                if type(e) == dict and list(e.keys())[0] == namespace and (var in e.get(namespace)):
                    # print(e.get(namespace))
                    # print(type(e) == dict)
                    # print(list(e.keys())[0], namespace)
                    print(namespace)  # <--
                    # return namespace
                    fl = 1
                    fl_2 = 1
            except:
                pass

            # Дмижемся вглубь
            if type(e) == dict:
                # print(namespace, var)
                get(e, namespace, var)


my_namespaces()

{'global': [{'first': [{'second': [{'third': []}]}, 'my_var']}]}
{'global': [{'a': ['a1', 'a2', 'a3', {'sub_a': ['a000']}]}]}
