class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())


object_stack = ExtendedStack()
object_stack.append(1)
object_stack.append(2)
object_stack.sum()
print(object_stack)

object_stack.append(1)
object_stack.append(2)
object_stack.sub()
print(object_stack)

object_stack.append(1)
object_stack.append(2)
object_stack.mul()
print(object_stack)

object_stack.append(1)
object_stack.append(2)
object_stack.div()
print(object_stack)