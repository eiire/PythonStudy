from abc import ABC, abstractmethod


class Engine():
    """ Engine, which can create notifications of achievements.
    An example of the achievement that the engine generates """
    def generate_message(self):
        for i in range(3):
            return {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribes = set()

    def subscribe(self, subscriber):
        self.__subscribes.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribes.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribes:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achievement):
        if achievement['title'] not in [achievement['title'] for achievement in self.achievements]:
            self.achievements.append(achievement)


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        self.achievements.add(achievement['title'])