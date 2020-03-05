#                              Frog random year
# def number_of_frogs(year):
#     numb_frog = 120
#     i = 1
#     while i < year:
#         numb_frog = 2 * (numb_frog - 50)
#         i+=1
#     return numb_frog
#
# print(number_of_frogs(int(input())))

#                               Fib
# def fib (n):
#     if n == 0:return 0
#     if n == 1:return 1
#     res = fib(n-1) + fib(n-2)
#     return res
# print(fib(3))

#                                        Error and exception (classes)
# import math
# def foo(y):
#     x = y
#     assert y != 1, "AssertionError"
#     x = x / y
#     x = math.exp(y) # inf
#     return x
#
#
# for i in [2000000, 1, 0]:
#     try:
#         foo(i)
#     except ZeroDivisionError as e:
#         print(type(ZeroDivisionError()).__name__)
#     except ArithmeticError as e:
#         print(type(ArithmeticError()).__name__)
#     except AssertionError as e:
#         print(e)
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