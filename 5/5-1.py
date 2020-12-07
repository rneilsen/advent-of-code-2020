from os.path import abspath, join, dirname

def binary_split(lb, ub):
    return (lb + ub) // 2

def convert(seat_code):
    (lb, ub) = (0, 127)
    for c in seat_code[:7]:
        mid = binary_split(lb, ub)
        if c == 'F':
            (lb, ub) = (lb, mid)
        elif c == 'B':
            (lb, ub) = (mid + 1, ub)
        else:
            raise ValueError
    row = lb

    (lb, ub) = (0, 7)
    for c in seat_code[7:]:
        mid = binary_split(lb, ub)
        if c == 'L':
            (lb, ub) = (lb, mid)
        elif c == 'R':
            (lb, ub) = (mid + 1, ub)
        else:
            raise ValueError
    col = lb
    return (row, col)

with open(abspath(join(dirname(__file__), 'input'))) as f:
    passes = [l.strip() for l in f.readlines()]

highest_id = -1
for p in passes:
    (row, col) = convert(p)
    seat_id = row*8 + col
    highest_id = max(highest_id, seat_id)

print(highest_id)