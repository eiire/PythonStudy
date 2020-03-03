import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, str):
        super(LoggableList, self).append(str)
        self.log(str)


x = LoggableList()
x.append("msg1")
x.append("msg2")
print(x)