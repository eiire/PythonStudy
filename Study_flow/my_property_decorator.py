class property(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, type = None):
        return self.fget(obj)


class Person:
    first_name = 'First'
    last_name = 'Last'

    # @property
    def full_name_1(self):
        return ' '.join([self.first_name, self.last_name])

    full_name_1 = property(full_name_1)

    def full_name_2(self):
        return ' '.join([self.first_name, self.last_name])


if __name__=='__main__':
    obj = Person()
    obj.full_name_2()

    print(Person.__dict__['full_name_2'](obj))

    print(obj.full_name_1)
    print(Person.__dict__['full_name_1'].__get__(obj))