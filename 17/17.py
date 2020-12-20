from os.path import abspath, dirname, join
from itertools import product
from functools import reduce
from typing import List

with open(abspath(join(dirname(__file__), 'input'))) as f:
    raw_rows = [l.strip() for l in f.readlines()]

target_num_cycles = 6

# CONVENTION: coord[0] (x) = row number, coord[1] (y) = position in row

class Cube:
    def __init__(self, coords: List[int]):
        self.coords = coords
    
    def get_neighbour_cubes(self):
        neighbour_cubes = set()
        for coords in product(*[range(x-1, x+2) for x in self.coords]):
            neighbour_cubes.add(Cube(coords))
        neighbour_cubes.remove(Cube(self.coords))
        return neighbour_cubes

    def __repr__(self):
        return f"({','.join([str(n) for n in self.coords])})"

    def __eq__(self, other):
        for (a, b) in zip(self.coords, other.coords):
            if a != b:
                return False
        else:
            return True

    def __hash__(self):
        return hash(tuple(self.coords))


class CubeSpace:
    def __init__(self, dim: int, raw_input: List[str]):
        self.active_cubes = set()
        self.dim = dim

        self.space_bounds = []
        for d in range(dim):
            self.space_bounds.append((0,0))
        
        for (x, row) in enumerate(raw_input):
            for (y, char) in enumerate(row):
                if char == '#':
                    self.activate([x, y] + ([0] * (dim-2)))
    
    def activate(self, coords):
        self.active_cubes.add(Cube(coords))
        for n in range(self.dim):
            (cur_lbound, cur_ubound) = self.space_bounds[n]
            self.space_bounds[n] = (min(coords[n], cur_lbound), max(coords[n], cur_ubound))
                
    def deactivate(self, cube: Cube):
        self.active_cubes.remove(cube)

    def display(self):
        for slice_coords in product(*[range(lb,ub+1) for (lb, ub) in self.space_bounds[2:]]):
            print(', '.join([f"x_{d+2}={slice_coords[d]}" for d in range(self.dim - 2)]))
            for x in range(self.space_bounds[0][0], self.space_bounds[0][1] + 1):
                row_string = ''
                for y in range(self.space_bounds[1][0], self.space_bounds[1][1] + 1):
                    row_string += ('#' if Cube([x,y] + list(slice_coords)) in self.active_cubes else '.')
                print(row_string)
            print('')
    
    def __repr__(self):
        return str([cube for cube in self.active_cubes])
    
    def is_active(self, coords):
        return Cube(coords) in self.active_cubes

    def cycle(self):
        # returns a new CubeSpace corresponding to one cycle after this one
        new_space = CubeSpace(self.dim, [])
        for coords in product(*[range(lb-1,ub+2) for (lb, ub) in self.space_bounds]):
            spaces_to_check = Cube(coords).get_neighbour_cubes()
            active_neighbours = spaces_to_check.intersection(self.active_cubes)
            if len(active_neighbours) == 3:
                new_space.activate(coords)
            elif len(active_neighbours) == 2 and self.is_active(coords):
                new_space.activate(coords)
        return new_space

      
def part1(disp=False):
    cubes = CubeSpace(3, raw_rows)
    if disp:
        print("After", n, "cycles:")
        cubes.display()
    for n in range(target_num_cycles):
        cubes = cubes.cycle()
        if disp:
            print("After", n, "cycles:")
            cubes.display()
    return len(cubes.active_cubes)

def part2(disp=False):
    cubes = CubeSpace(4, raw_rows)
    if disp:
        print("After", n, "cycles:")
        cubes.display()
    for n in range(target_num_cycles):
        cubes = cubes.cycle()
        if disp:
            print("After", n, "cycles:")
            cubes.display()
    return len(cubes.active_cubes)

print("Part 1:", part1())
print("Part 2:", part2())
