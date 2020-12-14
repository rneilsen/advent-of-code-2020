from os.path import abspath, join, dirname
from collections import deque
from math import cos, sin

cardinal = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}
rotations_R = deque([(1,0), (0,1), (-1,0), (0,-1)])

with open(abspath(join(dirname(__file__), 'input'))) as f:
    instructions = [l.strip() for l in f.readlines()]

(x, y) = (0, 0)
facing = cardinal['E']

for instr in instructions:
    (cmd, val) = (instr[0], int(instr[1:]))
    if cmd in cardinal:
        (x, y) = (x + val*cardinal[cmd][0], y + val*cardinal[cmd][1])
    elif cmd == 'F':
        (x, y) = (x + val*facing[0], y + val*facing[1])
    elif cmd == 'R':
        rotations_R.rotate(val // 90)
        facing = rotations_R[0]
    elif cmd == 'L':
        rotations_R.rotate(-val // 90)
        facing = rotations_R[0]

print(x, y, abs(x) + abs(y))
    