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


x = MoneyBox(15)
print(x.add(9))
print(x.can_add(6))
