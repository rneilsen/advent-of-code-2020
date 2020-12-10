from os.path import abspath, join, dirname
from itertools import combinations

(inputfile, len_pream) = ('test_input1', 5)
(inputfile, len_pream) = ('input', 25)

with open(abspath(join(dirname(__file__), inputfile))) as f:
    code = [int(l.strip()) for l in f.readlines()]

# find number that is not sum of 2 elems in previous len_pream elems
valid_sums = [a+b for (a,b) in combinations(code[:len_pream], 2)]
cur_pos = len_pream
while code[cur_pos] in valid_sums:
    valid_sums = [a+b for (a,b) in 
            combinations(code[cur_pos - len_pream + 1:cur_pos+1], 2)]
    cur_pos += 1
else:
    target = code[cur_pos]

print("9-1:", target)

# find block of numbers that sums to the target
start_pos = 0
end_pos = 2
block_sum = sum(code[start_pos:end_pos])
while block_sum != target:
    if block_sum > target:
        start_pos += 1
        end_pos = start_pos + 2
        block_sum = sum(code[start_pos:end_pos])
    else:
        block_sum += code[end_pos]
        end_pos += 1
else:
    print("9-2:", min(code[start_pos:end_pos]) + max(code[start_pos:end_pos]))