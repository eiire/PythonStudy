class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(self.dim)

        for x, index_x in zip(grid, range(self.dim[1])):
            for y, index_y in zip(x, range(self.dim[0])):
                if y == 1:
                    self.adaptee.lights.append((index_y, index_x))
                if y == -1:
                    self.adaptee.obstacles.append((index_y, index_x))

        self.adaptee.set_lights(self.adaptee.lights)
        self.adaptee.set_obstacles(self.adaptee.obstacles)

        return self.adaptee.generate_lights()


class Light:
    """
        The Light class creates a field of the specified size in the __init__ method.
        The parameter, which is a tuple of 2 numbers, is responsible for the size of the field.
        The element dim [1] is responsible for the height of the map, dim [0] for its width.
        The set_lights method sets an array of light sources with the given coordinates and calculates the lighting.
        The set_obstacles method sets obstacles in the same way.
        The position of the elements is determined by the list of tuples.
        Each tuple value contains 2 values:
        elem [0] - coordinate along the width of the map and
        elem [1] - coordinate along the height, respectively.
        The generate_lights method calculates lighting based on sources and obstacles.
        (This class is an example)
    """
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # light
        self.map[5][2] = -1  # obstacle

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)

