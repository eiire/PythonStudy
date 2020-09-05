import sys

x, y = sys.stdin.readline().split()
arr = [[] for i in range(int(x))]

for i in range(int(x)):
    arr[i] = sys.stdin.readline().split()

arr_transpose = [[0 for i in range(int(x))] for j in range(int(y))]

i_mirror = [i for i in reversed(range(int(x)))]
for i in reversed(range(int(x))):
    for j in reversed(range(int(y))):
        arr_transpose[j][i_mirror[i]] = arr[i][j]

for i in range(int(y)):
    print(' '.join(arr_transpose[i]))