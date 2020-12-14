from os.path import abspath, join, dirname
from itertools import product

with open(abspath(join(dirname(__file__), 'input'))) as f:
    rows = [l.strip() for l in f.readlines()]

def count_adj_occ(seats: list, row: int, col: int) -> int:
    (num_rows, num_cols) = (len(seats), len(seats[0]))
    if row not in range(num_rows) or col not in range(num_cols):
        raise ValueError

    rows_to_check = set([row])
    if row > 0:
        rows_to_check.add(row - 1)
    if row < num_rows - 1:
        rows_to_check.add(row + 1)
    
    cols_to_check = set([col])
    if col > 0:
        cols_to_check.add(col - 1)
    if col < num_cols - 1:
        cols_to_check.add(col + 1)
    
    seats_to_check = set(product(rows_to_check, cols_to_check))
    seats_to_check.remove((row, col))

    num_adj_occ = 0
    for (i,j) in seats_to_check:
        if seats[i][j] == '#':
            num_adj_occ += 1
    
    return num_adj_occ

while True:
    next_layout = []
    for i in range(len(rows)):
        next_row = ''
        for j in range(len(rows[0])):
            adj_occ = count_adj_occ(rows, i, j)
            if rows[i][j] == '.':
                next_row += '.'
            elif adj_occ == 0:
                next_row += '#'
            elif adj_occ >= 4:
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