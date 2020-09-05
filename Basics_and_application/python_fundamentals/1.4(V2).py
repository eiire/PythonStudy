import sys

sys.stdin = open("input_namespaces.txt", "r")


def my_namespaces():
    dict_namespaces = {
        'global': {
            'variables': [],
            'parent': None
        }
    }

    n = int(sys.stdin.readline())
    for i in range(n):
        line = sys.stdin.readline().split()

        if line[0] == 'add':
            add(dict_namespaces, line[1], line[2])
        elif line[0] == 'create':
            # pass
            create(dict_namespaces, line[1], line[2])
        elif line[0] == 'get':
            # pass
            print(get(dict_namespaces, line[1], line[2]))

    print(dict_namespaces)


# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
def add(dict_namespaces, namespace, var):
    dict_namespaces.get(namespace).get('variables').append(var)


# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
def create(dict_namespaces, namespace, parent):
    dict_namespaces.update({namespace: {'variables': [], 'parent': parent}})


# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует
def get(dict_namespaces, namespace, need_var):
    try:
        if need_var in dict_namespaces.get(namespace).get('variables'):
            return namespace
        else:
            res = get(dict_namespaces, dict_namespaces.get(namespace).get('parent'), need_var)
            if res is not None:
                return res
    except:
        pass


my_namespaces()
