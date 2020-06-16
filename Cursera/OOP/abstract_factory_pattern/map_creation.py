import random
from yaml import YAMLObject
from abc import ABC


#  Abstract factory
class AbstractLevel(YAMLObject):
    @classmethod
    def get_map(cls):
        return cls.Map()

    @classmethod
    def get_objects(cls):
        return cls.Objects()

    @classmethod  # special for yaml
    def from_yaml(cls, loader, node):
        _map = cls.Map()

        _objects = cls.Objects()
        _objects.config['enemy'] = loader.construct_mapping(node, deep=True).get('enemy', [])
        _objects.config['enemy_count'] = loader.construct_mapping(node, deep=True).get('enemy_count', 5)

        return {'map': _map, 'obj': _objects}

    class Map(ABC):
        pass

    class Objects(ABC):
        pass


#  Implementation 1
class EasyLevel(AbstractLevel):
    # yaml
    yaml_tag = '!easy_level'

    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(5)] for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    if i == 0 or j == 0 or i == 4 or j == 4:
                        self.Map[j][i] = -1  # граница карты
                    else:
                        self.Map[j][i] = random.randint(0, 2)  # случайная характеристика области

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            self.objects = [('next_lvl', (2, 2))]
            self.config = {}

        def get_objects(self, _map):
            for obj_name in ['rat']:
                coord = (random.randint(1, 3), random.randint(1, 3))
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 3), random.randint(1, 3))

                self.objects.append((obj_name, coord))

            return self.objects


#  Implementation 2
class MediumLevel(AbstractLevel):
    yaml_tag = '!medium_level'

    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(8)] for _ in range(8)]
            for i in range(8):
                for j in range(8):
                    if i == 0 or j == 0 or i == 7 or j == 7:
                        self.Map[j][i] = -1  # граница карты
                    else:
                        self.Map[j][i] = random.randint(0, 2)  # случайная характеристика области

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            self.objects = [('next_lvl', (4, 4))]
            self.config = {'enemy': []}

        def get_objects(self, _map):
            for obj_name in self.config['enemy']:
                coord = (random.randint(1, 6), random.randint(1, 6))
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 6), random.randint(1, 6))

                self.objects.append((obj_name, coord))

            return self.objects


#  Implementation 3
class HardLevel(AbstractLevel):
    yaml_tag = '!hard_level'

    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(10)] for _ in range(10)]
            for i in range(10):
                for j in range(10):
                    if i == 0 or j == 0 or i == 9 or j == 9:
                        # map border
                        self.Map[j][i] = -1
                    else:
                        # characteristic of the area (-1 for impassable region)
                        self.Map[j][i] = random.randint(-1, 8)

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            # place the transition to the next level
            self.objects = [('next_lvl', (5, 5))]
            self.config = {'enemy_count': 5, 'enemy': []}

        def get_objects(self, map_obj):
            # place enemies
            for obj_name in self.config['enemy']:
                for tmp_int in range(self.config['enemy_count']):
                    coord = (random.randint(1, 8), random.randint(1, 8))
                    # looking for a random free location
                    intersect = True
                    while intersect:
                        intersect = False
                        if map_obj[coord[0]][coord[1]] == -1:
                            intersect = True
                            coord = (random.randint(1, 8), random.randint(1, 8))
                            continue
                        for obj in self.objects:
                            if coord == obj[1]:
                                intersect = True
                                coord = (random.randint(1, 8), random.randint(1, 8))

                    self.objects.append((obj_name, coord))

            return self.objects