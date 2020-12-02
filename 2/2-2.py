from os.path import abspath, dirname, join
from re import split as resplit

# Read in input file
with open(abspath(join(dirname(__file__), 'input'))) as f:
    rows = f.read().splitlines()

valid_count = 0
for row in rows:
    # Splits e.g. '2-5 a: abcde' into 
    # left pos:   lp='2'
    # right pos:  rp='5'
    # match char: ch='a'
    # password:   pw='abcde'
    (lp, rp, ch, pw) = resplit('[\- :]+', row)
    if (pw[int(lp) - 1] + pw[int(rp) - 1]).count(ch) == 1:
        # this password is valid
        valid_count += 1

print(valid_count)