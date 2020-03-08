



vec1 = (2, 3)
vec2 = (2, 3)

def vector_sum(v1, v2):
    new_vec = []
    index_v2 = 0
    for el in v1:
        new_vec.append(el + v2[index_v2])
        index_v2 += 1
    return tuple(new_vec)

print(vector_sum(vec1, vec2))

#                              Frog random year
def number_of_frogs(year):
    numb_frog = 120
    i = 1
    while i < year:
        numb_frog = 2 * (numb_frog - 50)
        i += 1
    return numb_frog


# print(number_of_frogs(int(input())))

#                               Fib
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    res = fib(n - 1) + fib(n - 2)
    return res


# print(fib(3))
#                                          Minicalc
# var_1 = float(input())
# var_2 = float(input())
# operation = input()
#
# try:
#     dict_operations = {
#         '+': var_1 + var_2,
#         '*': var_1 * var_2,
#         '-': var_1 - var_2,
#         'pow': var_1 ** var_2,
#         '/': var_1 / var_2,
#         'mod': var_1 % var_2,
#         'div': var_1 // var_2,
#     }
#
#     print(dict_operations[operation])
# except ZeroDivisionError:
#     dict_operations = {
#         '+': var_1 + var_2,
#         '*': var_1 * var_2,
#         '-': var_1 - var_2,
#         'pow': var_1 ** var_2
#     }
#     if operation in ('/', 'div', 'mod'):
#         print('Division by 0!')
#     else:
#         print(dict_operations[operation])
