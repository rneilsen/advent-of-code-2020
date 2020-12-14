from os.path import abspath, join, dirname
from collections import deque
from typing import Tuple

cardinal = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}
rotations_R = deque([(1,0), (0,1), (-1,0), (0,-1)])

def rotate_right(wayp_x: int, wayp_y: int, angle: int) -> Tuple[int, int]:
    (new_wayp_x, new_wayp_y) = (wayp_x, wayp_y)
    for i in range(angle // 90):
        (new_wayp_x, new_wayp_y) = (new_wayp_y, -new_wayp_x)
    return (new_wayp_x, new_wayp_y)

with open(abspath(join(dirname(__file__), 'input'))) as f:
    instructions = [l.strip() for l in f.readlines()]

(ship_x, ship_y) = (0, 0)   # position vector of ship
(wayp_x, wayp_y) = (10, 1)  # direction vector of waypoint

for instr in instructions:
    (cmd, val) = (instr[0], int(instr[1:]))
    if cmd in cardinal:
        (wayp_x, wayp_y) = (wayp_x + val*cardinal[cmd][0], 
                            wayp_y + val*cardinal[cmd][1])
    elif cmd == 'F':
        (ship_x, ship_y) = (ship_x + val*wayp_x, ship_y + val*wayp_y)
    elif cmd == 'R':
        (wayp_x, wayp_y) = rotate_right(wayp_x, wayp_y, val)
    elif cmd == 'L':
        (wayp_x, wayp_y) = rotate_right(wayp_x, wayp_y, 360 - val)

print(ship_x, ship_y, abs(ship_x) + abs(ship_y))
    