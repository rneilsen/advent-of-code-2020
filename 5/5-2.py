from os.path import abspath, join, dirname

def binary_split(lb, ub):
    return (lb + ub) // 2

def convert(seat_code):
    # returns (row, col) of a seat with given seat code
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

# find the highest id of any seat in the plane
highest_id = -1
ids = set()
for p in passes:
    (row, col) = convert(p)
    seat_id = row*8 + col
    ids.add(seat_id)
    highest_id = max(highest_id, seat_id)

# find the only missing seat id with both neighbours already boarded
for n in range(highest_id):
    if n not in ids and {n-1, n+1} <= ids:
        print(n)
        break