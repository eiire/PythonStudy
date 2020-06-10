from unittest import TestCase


class TestHero(TestCase):
    def test_check_base_hero(self):
        from Cursera.OOP.сreating_class_decorator.character import Hero
        hero = Hero()
        print(
            hero.stats, "- stats;\n",
            hero.negative_effects, "- neg_eff;\n",
            hero.positive_effects, "- pos_eff;\n\n",
            hero.get_negative_effects(), "- get neg_eff;\n",
            hero.get_positive_effects(), "- get pos_eff;\n",
            hero.get_stats(), "- get stats\n",
        )

    def test_AbstractEffect(self):
        from Cursera.OOP.сreating_class_decorator.character import Hero, AbstractEffect
        stats_char = {
            'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4,
            'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1
        }
        hero = Hero()

        hero_with_effect = AbstractEffect(hero)

        self.assertEqual(hero.stats, stats_char)
        print(hero_with_effect.stats)
        hero_with_effect.stats['HP'] = 0
        print(hero_with_effect.stats)
        print(hero.stats)

    def test_AbstractPositive(self):
        from Cursera.OOP.сreating_class_decorator.character import Hero, AbstractEffect, AbstractPositive, Blessing, Berserk
        hero = Hero()

        hero_positive = Blessing(hero)
        hero_positive.get_positive_effects()
        print(hero_positive.positive_effects, 'base - ', hero.positive_effects)

        hero_positive_2 = Blessing(hero_positive)
        hero_positive_2.get_positive_effects()
        print(hero_positive_2.positive_effects)

        hero_positive_2.hero_with_effects = hero_positive_2
        print(hero_positive_2.positive_effects)

        g = Hero()
        j = Berserk(g)
        j.get_stats()
        j.get_positive_effects()
        k = Blessing(j)
        k.get_positive_effects()
        print(j.stats, j.positive_effects, '\n----', k.stats, k.positive_effects)

    def test_base_system(self):
        from Cursera.OOP.сreating_class_decorator.character import Hero, AbstractPositive, Berserk, Curse
        # создадим героя
        hero = Hero()

        brs1 = Berserk(hero)

        # 2 правильность изменения характеристик
        print(brs1.get_stats(), '\n', {'HP': 178,
                                       'MP': 42,
                                       'SP': 100,
                                       'Strength': 22,
                                       'Perception': 1,
                                       'Endurance': 15,
                                       'Charisma': -1,
                                       'Intelligence': 0,
                                       'Agility': 15,
                                       'Luck': 8}, '2')
        print('\n')
        # 3 неизменность списка отрицательных эффектов
        print(brs1.get_negative_effects(), '\n', [], '3')
        print('\n')

        # 4 проверим, что в список положительных эффектов был добавлен Berserk
        print(brs1.get_positive_effects(), '\n', ['Berserk'], '4')
        print('\n')
        # повторное наложение эффекта Berserk
        brs2 = Berserk(brs1)
        print(brs2.get_stats(), "CHECK")
        # наложение эффекта Curse
        cur1 = Curse(brs2)

        # 5 правильность изменения характеристик
        print(cur1.get_stats(), '\n', {'HP': 228,
                                       'MP': 42,
                                       'SP': 100,
                                       'Strength': 27,
                                       'Perception': -4,
                                       'Endurance': 20,
                                       'Charisma': -6,
                                       'Intelligence': -5,
                                       'Agility': 20,
                                       'Luck': 13}, '5')
        print('\n')

        # 6 правильность добавления эффектов в список положительных эффектов
        print(cur1.get_positive_effects(), '\n', ['Berserk', 'Berserk'], '6')
        print('\n')

        # 7 правильность добавления эффектов в список отрицательных эффектов
        print(cur1.get_negative_effects(), '\n', ['Curse'], '7')
        print('\n')
        # снятие эффекта Berserk
        cur1.base = brs1

        # 8 правильность изменения характеристик
        print(cur1.get_stats(), '\n', {'HP': 178,
                                       'MP': 42,
                                       'SP': 100,
                                       'Strength': 20,
                                       'Perception': -1,
                                       'Endurance': 13,
                                       'Charisma': -3,
                                       'Intelligence': -2,
                                       'Agility': 13,
                                       'Luck': 6}, '8')
        print('\n')

        # 9 правильность удаления эффектов из списка положительных эффектов
        print(cur1.get_positive_effects(), '\n', ['Berserk'], '9')
        print('\n')

        # 10 правильность эффектов в списке отрицательных эффектов
        print(cur1.get_negative_effects(), '\n', ['Curse'], '10')
        print('\n')

        # 11 незменность характеристик у объекта hero
        print(hero.get_stats(), '\n', {'HP': 128,
                                       'MP': 42,
                                       'SP': 100,
                                       'Strength': 15,
                                       'Perception': 4,
                                       'Endurance': 8,
                                       'Charisma': 2,
                                       'Intelligence': 3,
                                       'Agility': 8,
                                       'Luck': 1}, '11')
        print('\n')


