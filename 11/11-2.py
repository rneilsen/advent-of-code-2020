from os.path import abspath, join, dirname
from itertools import product

with open(abspath(join(dirname(__file__), 'input'))) as f:
    rows = [l.strip() for l in f.readlines()]

def count_card_occ(seats: list, row: int, col: int) -> int:
    (num_rows, num_cols) = (len(seats), len(seats[0]))
    if row not in range(num_rows) or col not in range(num_cols):
        raise ValueError

    num_occ = 0
    directions = set(product((-1, 0, 1), repeat=2)) - {(0,0)}
    for direction in directions:
        (i, j) = (row + direction[0], col + direction[1])
        while 0 <= i <= num_rows - 1 and 0 <= j <= num_cols - 1:
            if seats[i][j] == '#':
                num_occ += 1
                break
            elif seats[i][j] == 'L':
                break
            (i, j) = (i + direction[0], j + direction[1])
    
    return num_occ

while True:
    next_layout = []
    for i in range(len(rows)):
        next_row = ''
        for j in range(len(rows[0])):
            if rows[i][j] == '.':
                next_row += '.'
                continue
            adj_occ = count_card_occ(rows, i, j)
            if adj_occ == 0:
                next_row += '#'
            elif adj_occ >= 5:
                next_row += 'L'
            else:
                next_row += rows[i][j]
        next_layout.append(next_row)
    if next_layout == rows:
        break
    else:
        rows = next_layout.copy()

total_occ = 0
for row in rows:
    total_occ += row.count('#')

print(total_occ)