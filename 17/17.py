from os.path import abspath, dirname, join
from itertools import product
from typing import List

with open(abspath(join(dirname(__file__), 'input'))) as f:
    raw_rows = [l.strip() for l in f.readlines()]

# CONVENTION: x = row number, y = position in row, z = layer number

class Cube:
    def __init__(self, x: int, y: int, z: int):
        (self.x, self.y, self.z) = (x, y, z)
    
    def get_neighbour_cubes(self):
        neighbour_cubes = set()
        for (x, y, z) in product(*[range(n-1, n+2) for n in [self.x, self.y, self.z]]):
            neighbour_cubes.add(Cube(x, y, z))
        neighbour_cubes.remove(Cube(self.x, self.y, self.z))
        return neighbour_cubes

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))


class CubeSpace:
    def __init__(self, raw_input: List[str]):
        self.active_cubes = set()
        self.xmin = self.xmax = 0
        self.ymin = self.ymax = 0
        self.zmin = self.zmax = 0
        for (x, row) in enumerate(raw_input):
            for (y, char) in enumerate(row):
                if char == '#':
                    self.activate(x, y, 0)
    
    def activate(self, x: int, y: int, z: int):
        self.active_cubes.add(Cube(x, y, z))
        self.xmin = min(x, self.xmin)
        self.xmax = max(x, self.xmax)
        self.ymin = min(y, self.ymin)
        self.ymax = max(y, self.ymax)
        self.zmin = min(z, self.zmin)
        self.zmax = max(z, self.zmax)
    
    def deactivate(self, cube: Cube):
        self.active_cubes.remove(cube)

    def display(self):
        for z in range(self.zmin, self.zmax + 1):
            print(f"z={z}")
            for x in range(self.xmin, self.xmax + 1):
                row_string = ''
                for y in range(self.ymin, self.ymax + 1):
                    row_string += ('#' if Cube(x,y,z) in self.active_cubes else '.')
                print(row_string)
            print('')
    
    def __repr__(self):
        return str([cube for cube in self.active_cubes])
    
    def is_active(self, x: int, y: int, z: int):
        return Cube(x, y, z) in self.active_cubes

    def cycle(self):
        # returns a new CubeSpace corresponding to one cycle after this one
        new_space = CubeSpace([])
        for x in range(self.xmin - 1, self.xmax + 2):
            for y in range(self.ymin - 1, self.ymax + 2):
                for z in range(self.zmin - 1, self.zmax + 2):
                    spaces_to_check = Cube(x,y,z).get_neighbour_cubes()
                    active_neighbours = spaces_to_check.intersection(self.active_cubes)
                    if len(active_neighbours) == 3:
                        new_space.activate(x, y, z)
                    elif len(active_neighbours) == 2 and self.is_active(x, y, z):
                        new_space.activate(x, y, z)
        return new_space
        
                    
def part1():
    cubes = CubeSpace(raw_rows)
    for n in range(6):
        cubes = cubes.cycle()
    return len(cubes.active_cubes)

print(part1())

