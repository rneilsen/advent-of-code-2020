from os.path import abspath, dirname, join
from re import split as resplit

# Read in input file
with open(abspath(join(dirname(__file__), 'input'))) as f:
    rows = f.read().splitlines()

valid_count = 0
for row in rows:
    # Splits e.g. '2-5 a: abcde' into 
    # lowerbound: lb='2'
    # upperbound: ub='5'
    # match char: c='a'
    # password:   pw='abcde'
    (lb, ub, ch, pw) = resplit('[\- :]+', row)
    if int(lb) <= pw.count(ch) <= int(ub):
        # this password is valid
        valid_count += 1

print(valid_count)