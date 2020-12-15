from os.path import abspath, join, dirname
from sympy.ntheory.modular import crt

with open(abspath(join(dirname(__file__), 'input'))) as f:
    start_time = int(f.readline().strip())
    buses = f.readline().strip().split(sep=',')

mod = 0
rems = []
mods = []
for bus in buses:
    if bus != 'x':
        rems.append(int(bus))
        mods.append(mod)
    mod -= 1

print(crt(rems, mods))