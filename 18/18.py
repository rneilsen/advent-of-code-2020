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


def part1() -> int:
    return sum([evaluate(list(line.replace(' ', ''))) for line in lines])

def part2() -> int:
    # parse input to insert parens around all addition expressions
    new_lines = []
    for line in lines:
        line = line.replace(' ', '')
        next_plus = line.find('+')
        while next_plus != -1:
            left_edge = next_plus - 1
            paren_depth = (1 if line[left_edge] == ')' else 0)
            while paren_depth > 0:
                left_edge -= 1
                if line[left_edge] == ')':
                    paren_depth += 1
                elif line[left_edge] == '(':
                    paren_depth -= 1
            right_edge = next_plus + 1
            paren_depth = (1 if line[right_edge] == '(' else 0)
            while paren_depth > 0:
                right_edge += 1
                if line[right_edge] == '(':
                    paren_depth += 1
                elif line[right_edge] == ')':
                    paren_depth -= 1
            if left_edge != 0 or right_edge != len(line) - 1:
                line = line[:left_edge] + '(' + line[left_edge:right_edge + 1] + ')' + line[right_edge + 1:]
            next_plus = line.find('+', next_plus + 2)
        new_lines.append(line)

    return sum([evaluate(list(line.replace(' ', ''))) for line in new_lines])

print("Part 1:", part1())
print("Part 2:", part2())