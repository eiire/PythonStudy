class SomeObject(object):
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet(object):
    def __init__(self, data_type):
        self.data_type = data_type


class EventSet(object):
    def __init__(self, data):
        self.data = data


class NullHandler(object):
    """ It will simply pass the event to the next handler for processing. """

    def __init__(self, successor=None):
        self.next = successor
        # print(self.next.__class__.__name__)

    """ Call all handlers """
    def handle(self, data_entity, event):
        if self.next is not None:
            return self.next.handle(data_entity, event)  # return (!)


class IntHandler(NullHandler):
    def handle(self, data_entity, event):
        if event.__class__.__name__ == 'EventGet':
            if event.data_type == int:
                return data_entity.integer_field
            else:
                return super().handle(data_entity, event)
        elif event.__class__.__name__ == 'EventSet':
            if type(event.data) == int:
                data_entity.integer_field = event.data
            else:
                super().handle(data_entity, event)


class FloatHandler(NullHandler):
    def handle(self, data_entity, event):
        if event.__class__.__name__ == 'EventGet':
            if event.data_type == float:
                return data_entity.float_field
            else:
                return super().handle(data_entity, event)
        elif event.__class__.__name__ == 'EventSet':
            if type(event.data) == float:
                data_entity.float_field = event.data
            else:
                super().handle(data_entity, event)


class StrHandler(NullHandler):
    def handle(self, data_entity, event):
        if event.__class__.__name__ == 'EventGet':
            if event.data_type == str:
                return data_entity.string_field
            else:
                return super().handle(data_entity, event)
        elif event.__class__.__name__ == 'EventSet':
            if type(event.data) == str:
                data_entity.string_field = event.data
            else:
                super().handle(data_entity, event)