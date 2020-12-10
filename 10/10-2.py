from os.path import abspath, join, dirname
from itertools import groupby
from operator import mul
import functools

with open(abspath(join(dirname(__file__), 'input'))) as f:
    adaps = [0] + [int(l.strip()) for l in f.readlines()]

@functools.lru_cache(None)
def tribonacci(n: int) -> int:
    if n in (0,1):
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

adaps.sort()
adaps.append(adaps[-1] + 3)

diffs = [adaps[i+1] - adaps[i] for i in range(len(adaps) - 1)]
block_sizes = [len(list(y)) for (x, y) in groupby(diffs) if x == 1]

# by observation all 'blocks' between 3-diffs consist of 1-diffs only.
# the number of ways to select adapters in a row of n 1-diffs
# is given by tribonacci(n+2)
print(functools.reduce(lambda x, y: x*y, [tribonacci(n+2) for n in block_sizes]))
