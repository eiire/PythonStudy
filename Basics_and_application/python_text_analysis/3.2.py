s = input()
a = input()
b = input("For task_1(counter): ")


def counter(s, a, b):
    count_in = 0
    if s.find(a) != -1 and b.find(a) != -1:
        return print('Impossible')

    while s.find(a) != -1:
        s = s.replace(a, b)
        count_in += 1

    print(count_in)


def task_2(s, a):
    cnt = 0
    c = 0
    while c < len(s):
        if s.startswith(a, c, len(s)):
            cnt += 1
        c += 1
    print(cnt)


# counter(s, a, b)
# task_2(s, a)
