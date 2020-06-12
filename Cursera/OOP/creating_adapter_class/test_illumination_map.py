from unittest import TestCase


class TestIlluminationMap(TestCase):
    def test_light_class(self):
        from Cursera.OOP.creating_adapter_class.illumination_map import Light
        light = Light((3, 3))
        print(light.dim, '\n',
              light.lights, '\n',
              light.obstacles, '\n',
              light.generate_lights(), '\n',

              light.set_lights((1, 1)), light.lights, light.generate_lights(),
              light.set_obstacles((2, 2)), 'obstacle was create: ',
              light.obstacles, 'new_lights_map: ', light.generate_lights(),  '\n',

              light.set_lights((1, 1)))

    def test_my_adapter(self):
        from Cursera.OOP.creating_adapter_class.illumination_map import Light, System, MappingAdapter
        light = Light((3, 3))  # base_obj
        light_for_system = MappingAdapter(light)
        system = System()
        system.get_lightening(light_for_system)
        self.assertEqual((len(system.lightmap), len(system.lightmap[0])), (20, 30))
        self.assertEqual((light.obstacles, light_for_system.adaptee.obstacles), ([(2, 5)], [(2, 5)]),
                         "Base object was change")