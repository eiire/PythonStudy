# Version 2(passed) task 1
def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


class multifilter:
    def judge_half(self):
        fl = 0
        for check in self.check_lst:
            if check == '1':
                fl += 1
        if len(self.check_lst) / 2 <= fl:
            return True
        else:
            return False

    def judge_any(self):
        fl = 0
        for check in self.check_lst:
            if check == '1':
                fl = 1
        if fl == 0:
            return False
        else:
            return True

    def judge_all(self):
        # print(check_lst)
        fl = 0
        for check in self.check_lst:
            if check == '0':
                fl = 1
        if fl == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.funcs = funcs
        self.judge = judge
        self.iterable = iterable
        self.check_lst = []

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            for foo in self.funcs:
                self.check_lst += str(int(foo(i)))
            if self.judge(self):
                yield i
            self.check_lst.clear()


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))

#  Task 2
import itertools


def primes():
    i = 0
    while True:
        if my_simple(i) and i != 0 and i != 1:
            yield i
        i += 1

def my_simple(var):
    lst = range(var)
    fl = 0
    for e in lst:
        try:
            if var % e == 0 and e != 1:
                fl = 1
        except:
            pass
    if fl == 1:
        return False
    else:
        return True

print("Task_2: ", list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

#  Version 1
# def my_generator(myfilter):
#     for element in myfilter:
#         yield element
#
#
# def my_costyl(elements):
#     for el in elements:
#         yield int(el)
#     elements.clear()
#
#
# class MultiFilter:
#     # test is new string judged elements
#     test = []
#
#     def judge_half(pos, neg):
#         # print(neg)
#         fl = 0
#         for check in neg:
#             if check == '1':
#                 fl += 1
#         if len(neg) / 2 < fl:
#             return pos
#
#     def judge_any(pos, neg):
#         return pos
#
#     def judge_all(pos, neg):
#         # print(neg)
#         fl = 0
#         for check in neg:
#             if check == '0':
#                 fl = 1
#         if fl == 0:
#             return pos
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         elements = my_generator(iterable)
#         check_lst = []
#         for element in elements:
#             for foo in funcs:
#                 check_lst += str(int(foo(element)))
#             # print(check_lst)
#             if judge(element, check_lst) is not None:
#                 self.test.append(judge(element, check_lst))
#             # print(self.test)
#             check_lst.clear()
#
#     def __iter__(self):
#         return my_costyl(self.test)
#
#
# def mul2(x):
#     return x % 2 == 0
#
#
# def mul3(x):
#     return x % 3 == 0
#
#
# def mul5(x):
#     return x % 5 == 0
#
#
# a = [i for i in range(31)]  # [0, 1, 2, ... , 30]
#
# print(list(MultiFilter(a, mul2, mul3, mul5)))
# # # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
#
# print(list(MultiFilter(a, mul2, mul3, mul5, judge=MultiFilter.judge_half)))
# # # [0, 6, 10, 12, 15, 18, 20, 24, 30]
#
# print(list(MultiFilter(a, mul2, mul3, mul5, judge=MultiFilter.judge_all)))
# # [0, 30]
