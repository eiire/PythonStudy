from unittest import TestCase


class TestAbstractLvl(TestCase):
    def test_factory(self):
        from Cursera.OOP.abstract_factory_pattern.map_creation import AbstractLevel, EasyLevel, MediumLevel, HardLevel

        #  Use of a common interface from factories
        def create_lvl(FactoryLevel):
            lvl = FactoryLevel()
            lvl.get_map()
            lvl.get_objects()

            return lvl

        #  Example using a common interface from factories
        self.assertEqual(create_lvl(HardLevel).get_objects().objects, [('next_lvl', (5, 5))])
        self.assertEqual(create_lvl(MediumLevel).get_objects().objects, [('next_lvl', (4, 4))])
        self.assertEqual(create_lvl(EasyLevel).get_objects().objects, [('next_lvl', (2, 2))])