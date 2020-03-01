# Frog random year
# def number_of_frogs(year):
#     numb_frog = 120
#     i = 1
#     while i < year:
#         numb_frog = 2 * (numb_frog - 50)
#         i+=1
#     return numb_frog
#
# print(number_of_frogs(int(input())))

# Fib
# def fib (n):
#     if n == 0:return 0
#     if n == 1:return 1
#     res = fib(n-1) + fib(n-2)
#     return res
# print(fib(3))

# Matrix transpose
# import sys
#
# x, y = sys.stdin.readline().split()
# arr = [[] for i in range(int(x))]
#
# for i in range(int(x)):
#     arr[i] = sys.stdin.readline().split()
#
# arr_transpose = [[0 for i in range(int(x))] for j in range(int(y))]
#
# i_mirror = [i for i in reversed(range(int(x)))]
# for i in reversed(range(int(x))):
#     for j in reversed(range(int(y))):
#         arr_transpose[j][i_mirror[i]] = arr[i][j]
#
# for i in range(int(y)):
#     print(' '.join(arr_transpose[i]))


