from unittest import TestCase


class TestShortNotificationPrinter(TestCase):
    def test_update(self):
        from Cursera.OOP.observer_pattern_implementation.achievement_systems import ShortNotificationPrinter, FullNotificationPrinter
        shotr_mes = ShortNotificationPrinter()
        shotr_mes.update({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
        shotr_mes.update({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
        # shotr_mes.update({'ff': 'F'})
        self.assertEqual(shotr_mes.achievements, {'Покоритель'})

        full_mess = FullNotificationPrinter()
        full_mess.update({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
        full_mess.update({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
        full_mess.update({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
        self.assertEqual(full_mess.achievements, [{"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}])

    def test_archievement_systme(self):
        from Cursera.OOP.observer_pattern_implementation.achievement_systems \
            import ShortNotificationPrinter, FullNotificationPrinter, Engine, ObservableEngine

        engine = Engine()
        obs_engine = ObservableEngine()
        subcriber_1 = FullNotificationPrinter()
        subcriber_2 = ShortNotificationPrinter()

        obs_engine.subscribe(subcriber_1)
        obs_engine.notify(engine.generate_message())
        self.assertNotEqual(subcriber_1.achievements,
                            [{"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"} for _ in range(3)])
        print(subcriber_1.achievements)

        obs_engine.subscribe(subcriber_2)
        obs_engine.notify(engine.generate_message())
        self.assertNotEqual(subcriber_1.achievements,
                            ('Покоритель' for _ in range(3)))
        print(subcriber_2.achievements)


