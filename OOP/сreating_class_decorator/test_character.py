from unittest import TestCase


class TestHero(TestCase):
    def test_decorator_removal(self):
        from OOP.сreating_class_decorator.character import Hero, Berserk, Curse
        hero = Hero()
        brs1 = Berserk(hero)
        brs2 = Berserk(brs1)
        brs2.get_positive_effects()
        # print(id(brs2), id(brs1))
        cur1 = Curse(brs2)
        # cur1.get_positive_effects()
        print(cur1.positive_effects)
        cur1.base = brs1  # remove second effect Berserk
        # print(id(cur1.base))
        self.assertEqual(id(brs1), id(cur1.base))
        print(cur1.positive_effects)

    def test_pos_eff(self):
        from OOP.сreating_class_decorator.character import Hero, Berserk
        # создадим героя
        hero = Hero()

        brs1 = Berserk(hero)
        brs1.get_positive_effects()
        self.assertEqual(brs1.positive_effects, ['Berserk'], 'brs1')
        brs2 = Berserk(brs1)
        brs2.get_positive_effects()
        self.assertEqual(brs2.positive_effects, ['Berserk', 'Berserk'], 'bsr2')
        brs2.base = hero
        brs2.get_positive_effects()
        self.assertEqual(brs2.positive_effects, ['Berserk'], brs2.base.__class__)

        # cur1 = Curse(brs2)
        #
        # # 6 правильность добавления эффектов в список положительных эффектов
        # print(cur1.get_positive_effects(), ['Berserk', 'Berserk'], '6')
        # print('\n')
        #
        # # 7 правильность добавления эффектов в список отрицательных эффектов
        # print(cur1.get_negative_effects(), '\n', ['Curse'], '7')
        # print('\n')
        # # снятие эффекта Berserk
        # cur1.base = brs1
        #
        # # 9 правильность удаления эффектов из списка положительных эффектов
        # print(cur1.get_positive_effects(), '\n', ['Berserk'], '9')
        # print('\n')

    def test_stats_with_remove_effect(self):
        from OOP.сreating_class_decorator.character import Hero, Berserk
        # создадим героя
        hero = Hero()

        brs1 = Berserk(hero)

        # 2 правильность изменения характеристик
        # print(brs1.get_stats(), '\n', {'HP': 178,
        #                                'MP': 42,
        #                                'SP': 100,
        #                                'Strength': 22,
        #                                'Perception': 1,
        #                                'Endurance': 15,
        #                                'Charisma': -1,
        #                                'Intelligence': 0,
        #                                'Agility': 15,
        #                                'Luck': 8}, '2')
        print('\n')
        brs1.get_stats()
        brs1.get_positive_effects()
        print('\n')
        # повторное наложение эффекта Berserk
        brs2 = Berserk(brs1)
        brs2.base = hero
        # print(brs1.stats, 'brs1')
        self.assertEqual(brs2.get_stats(), {'HP': 178,
                                            'MP': 42,
                                            'SP': 100,
                                            'Strength': 22,
                                            'Perception': 1,
                                            'Endurance': 15,
                                            'Charisma': -1,
                                            'Intelligence': 0,
                                            'Agility': 15,
                                            'Luck': 8}, "brs2 with remove one berserk")
        # print(brs1.stats, 'brs1')

    def test_base_system(self):
        from OOP.сreating_class_decorator.character import Hero, Berserk, Curse
        # создадим героя
        hero = Hero()

        brs1 = Berserk(hero)

        # 2 правильность изменения характеристик
        self.assertEqual(brs1.get_stats(), {'HP': 178,
                                            'MP': 42,
                                            'SP': 100,
                                            'Strength': 22,
                                            'Perception': 1,
                                            'Endurance': 15,
                                            'Charisma': -1,
                                            'Intelligence': 0,
                                            'Agility': 15,
                                            'Luck': 8}, '2')
        # 3 неизменность списка отрицательных эффектов
        self.assertEqual(brs1.get_negative_effects(), [], '3')

        # 4 проверим, что в список положительных эффектов был добавлен Berserk
        self.assertEqual(brs1.get_positive_effects(), ['Berserk'], '4')

        # повторное наложение эффекта Berserk
        brs2 = Berserk(brs1)

        brs2.get_stats()
        # наложение эффекта Curse
        cur1 = Curse(brs2)

        # 5 правильность изменения характеристик
        self.assertEqual(cur1.get_stats(), {'HP': 228,
                                            'MP': 42,
                                            'SP': 100,
                                            'Strength': 27,
                                            'Perception': -4,
                                            'Endurance': 20,
                                            'Charisma': -6,
                                            'Intelligence': -5,
                                            'Agility': 20,
                                            'Luck': 13}, '5')

        # 6 правильность добавления эффектов в список положительных эффектов
        self.assertEqual(cur1.get_positive_effects(), ['Berserk', 'Berserk'], '6')

        # 7 правильность добавления эффектов в список отрицательных эффектов
        self.assertEqual(cur1.get_negative_effects(), ['Curse'], '7')

        # снятие эффекта Berserk
        cur1.base = brs1

        # 8 правильность изменения характеристик
        self.assertEqual(cur1.get_stats(), {'HP': 178,
                                            'MP': 42,
                                            'SP': 100,
                                            'Strength': 20,
                                            'Perception': -1,
                                            'Endurance': 13,
                                            'Charisma': -3,
                                            'Intelligence': -2,
                                            'Agility': 13,
                                            'Luck': 6}, '8')

        # 9 правильность удаления эффектов из списка положительных эффектов
        self.assertEqual(cur1.get_positive_effects(), ['Berserk'], '9')

        # 10 правильность эффектов в списке отрицательных эффектов
        self.assertEqual(cur1.get_negative_effects(), ['Curse'], '10')

        # 11 незменность характеристик у объекта hero
        self.assertEqual(hero.get_stats(), {'HP': 128,
                                            'MP': 42,
                                            'SP': 100,
                                            'Strength': 15,
                                            'Perception': 4,
                                            'Endurance': 8,
                                            'Charisma': 2,
                                            'Intelligence': 3,
                                            'Agility': 8,
                                            'Luck': 1}, '11')

    def test_multiple_effects(self):
        from OOP.сreating_class_decorator.character import Hero, Curse, Berserk
        hero = Hero()
        print(hero.get_stats(), '<-- main', '\n')

        b = Curse(Curse(Berserk(Berserk(hero))))
        self.assertEqual(b.get_positive_effects(), ['Berserk', 'Berserk'])

        ber = Berserk(Berserk(Berserk(hero)))
        self.assertEqual(ber.get_stats()['HP'], 278)
        self.assertEqual(ber.get_positive_effects(), ['Berserk', 'Berserk', 'Berserk'])

    def test_killme(self):
        from OOP.сreating_class_decorator.character import Hero, Berserk, Curse
        hero = Hero()
        brs1 = Berserk(hero)
        self.assertEqual(brs1.get_negative_effects(), [], '3')  # <-- был вызван
        print(brs1.negative_effects)
        brs2 = Berserk(brs1)
        brs2.get_stats()
        cur1 = Curse(brs2)
        # self.assertEqual(cur1.get_negative_effects(), ['Curse'], '7')
        cur1.base = brs1
        print(cur1.negative_effects)
        self.assertEqual(cur1.get_negative_effects(), ['Curse'], '10')

    def test_3xCurs(self):
        from OOP.сreating_class_decorator.character import Hero, Curse, Berserk
        hero = Hero()
        curl = Curse(Curse(Curse(hero)))
        ber = Berserk(Berserk(Berserk(hero)))

        print(curl.get_negative_effects(), ber.get_positive_effects())
