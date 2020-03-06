# Task 1
class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        if (self.capacity - self.count) >= v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.count += v

        return self.capacity - self.count


# x = MoneyBox(15)
# print(x.add(9))
# print(x.can_add(6))

# Task 2
class Buffer:
    def __init__(self):
        self.lst = []
    def add(self, *a):
        self.lst += a
        divisor = 0
        for i in range(len(self.lst)):
            if i % 5 == 0 and i != 0:
                sum = self.lst[divisor] + self.lst[divisor - 1] + self.lst[divisor - 2] + self.lst[divisor - 3] + self.lst[divisor - 4]
                self.lst = self.lst[divisor:]
                divisor = 0
                print(sum)
            divisor += 1
            if len(self.lst) == 5:
                sum = self.lst[divisor] + self.lst[divisor - 1] + self.lst[divisor - 2] + self.lst[divisor - 3] + self.lst[divisor - 4]
                print(sum)
                self.lst = self.lst[5:]

    def get_current_part(self):
        return print(self.lst)

# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]
