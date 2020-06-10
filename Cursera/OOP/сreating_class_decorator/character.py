from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_positive_effects(self):
        pass


class AbstractPositive(AbstractEffect):
    def __init__(self, obj_hero):
        super().__init__()
        self.hero_with_effects = obj_hero
        self.stats = obj_hero.stats
        self.positive_effects = [effect for effect in obj_hero.positive_effects]


class AbstractNegative(AbstractEffect):
    def __init__(self, obj_hero):
        super().__init__()
        self.hero_with_effects = obj_hero
        self.stats = obj_hero.stats
        self.negative_effects = [effect for effect in obj_hero.negative_effects]


class Curse(AbstractPositive):
    def get_stats(self):
        for stat in self.stats.keys():
            self.stats[stat] = self.stats[stat] - 2 \
                if stat != 'HP' and stat != 'MP' and stat != 'SP' else self.stats[stat]

        return self.stats

    def get_positive_effects(self):
        self.hero_with_effects.get_positive_effects()
        return self.hero_with_effects.positive_effects

    def get_negative_effects(self):
        self.negative_effects.append(type(self).__name__)
        return self.negative_effects


class Blessing(AbstractPositive):
    def get_stats(self):
        for stat in self.stats.keys():
            self.stats[stat] += 2

        return self.stats

    def get_positive_effects(self):
        self.positive_effects.append(type(self).__name__)
        return self.positive_effects

    def get_negative_effects(self):
        return self.negative_effects


class Berserk(AbstractPositive):
    def get_stats(self):
        for stat in self.stats.keys():
            self.stats[stat] = self.stats[stat] + 7 if stat == 'Strength' or stat == 'Endurance'\
                                                       or stat == 'Agility' or stat == 'Luck' else self.stats[stat]
            self.stats[stat] = self.stats[stat] - 3 if stat == 'Perception' or stat == 'Charisma' \
                                                       or stat == 'Intelligence' else self.stats[stat]
            self.stats[stat] = self.stats[stat] + 50 if stat == 'HP' else self.stats[stat]

        return self.stats

    def get_positive_effects(self):
        self.positive_effects.append(type(self).__name__)
        return self.positive_effects

    def get_negative_effects(self):
        return self.negative_effects