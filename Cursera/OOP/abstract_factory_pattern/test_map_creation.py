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

    def test_yaml(self):
        # демонстрация загрузки yaml по первый вариант
        import yaml

        # класс определяющий пользовательский тип данных
        class ExampleClass:
            def __init__(self, value):
                self.value = value

            def __str__(self):
                return f'ExampleClass, value - {self.value}'

        # функция конструктор для типа данных ExampleClass
        def constuctor_example_class(loader, node):
            # получаем данные из yaml
            value = loader.construct_mapping(node)
            print(loader, '\n', node, '\n', value, '\n', ExampleClass(*value).value)
            # необходимо выбрать из полученные данных необходимые
            # для создания экземпляра класса ExampleClass
            return ExampleClass(*value)

        # регистрируем конструктор
        yaml.add_constructor('!example_class', constuctor_example_class)
        # yaml строка
        document = """!example_class {5}"""
        # выполняем загрузку
        obj = yaml.load(document)
        # выведем полученный объект, ожидаем строку
        # ExampleClass, value - 5
        print('result:', obj)

    def test_yaml_EasyLevel(self):
        import yaml
        from Cursera.OOP.abstract_factory_pattern.map_creation \
            import AbstractLevel, EasyLevel, MediumLevel, HardLevel

        with open('settings_maps.yaml') as F:
            Levels_yaml = yaml.load(F)

            Levels = {'levels': []}
            _map = EasyLevel.Map()
            _obj = EasyLevel.Objects()
            Levels['levels'].append({'map': _map, 'obj': _obj})

            _map = MediumLevel.Map()
            _obj = MediumLevel.Objects()
            _obj.config = {'enemy':['rat']}
            Levels['levels'].append({'map': _map, 'obj': _obj})

            _map = HardLevel.Map()
            _obj = HardLevel.Objects()
            _obj.config = {'enemy': ['rat', 'snake', 'dragon'], 'enemy_count': 10}
            Levels['levels'].append({'map': _map, 'obj': _obj})

            for lvl in Levels['levels']:
                print(lvl)

            print('\nLike above:')
            for lvl in Levels_yaml['levels']:
                print(lvl)

            self.assertEqual(Levels_yaml['levels'][2]['obj'].config['enemy'], ['rat', 'snake', 'dragon'])