from os.path import abspath, dirname, join
from collections import deque
from itertools import islice
from typing import List, Tuple

with open(abspath(join(dirname(__file__), 'input'))) as f:
    lines = [l.strip() for l in f.readlines()]

def evaluate(line: List[str]) -> Tuple[int, List[str]]:
    while '(' in line:
        start_paren = end_paren = line.index('(')
        paren_depth = 1
        while paren_depth > 0:
            end_paren += 1
            if line[end_paren] == '(':
                paren_depth += 1
            elif line[end_paren] == ')':
                paren_depth -= 1
        line =  line[:start_paren] + \
                [evaluate(line[start_paren+1:end_paren])] + \
                line[end_paren+1:]
    
    val = int(line[0])
    i = 1
    while i < len(line):
        if line[i] == '+':
            val += int(line[i+1])
        elif line[i] == '*':
            val *= int(line[i+1])
        i += 2
    return val


def part1():
    return sum([evaluate(list(line.replace(' ', ''))) for line in lines])

print("Part 1:", part1())