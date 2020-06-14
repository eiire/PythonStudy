from unittest import TestCase


class TestSomeObject(TestCase):
    def test_handler(self):
        from Cursera.OOP.chain_of_responsibility_pattern.data_type_handler \
            import SomeObject, EventGet, EventSet, IntHandler, FloatHandler, NullHandler
        obj = SomeObject()
        obj.integer_field = 4
        obj.float_field = 3.14
        obj.string_field = 'dor'

        chain = FloatHandler(IntHandler(NullHandler()))
        chain.handle(obj, EventSet(6.1))
        self.assertEqual(chain.handle(obj, EventGet(float)), 6.1)

        chain.handle(obj, EventSet(3))
        print(chain.handle(obj, EventGet(int)))
        self.assertEqual(chain.handle(obj, EventGet(int)), 3)
