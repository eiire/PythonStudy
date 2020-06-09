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
        hero_effect = AbstractEffect(hero)
        hero_effect.change_stats_hero_with_dec()
        print(hero_effect.stats)
        self.assertEqual(hero.stats, stats_char)