from os.path import abspath, dirname, join
from typing import List

mask_length = 36

with open(abspath(join(dirname(__file__), 'input'))) as f:
    lines = [line.strip().split(sep=' = ') for line in f.readlines()]

def expand_masked(masked_addr: str) -> List[int]:
    x_loc = masked_addr.find('X')
    if x_loc == -1:
        return [int(masked_addr, 2)]
    else:
        left = masked_addr[:x_loc]
        right = masked_addr[x_loc + 1:]
        return expand_masked(left + '0' + right) + expand_masked(left + '1' + right)

memory = {}
mask = 'X' * mask_length
for line in lines:
    if line[0] == 'mask':
        mask = line[1]
    else:
        raw_addr = bin(int(''.join([c for c in line[0] if c.isnumeric()])))[2:].zfill(mask_length)
        raw_value = bin(int(line[1]))[2:].zfill(mask_length)
        masked_addr = ''
        for i in range(mask_length):
            if mask[i] == '0':
                masked_addr += raw_addr[i]
            elif mask[i] == '1':
                masked_addr += '1'
            else:
                masked_addr += 'X'
        
        for addr in expand_masked(masked_addr):
            memory[addr] = raw_value


value_sum = 0
for bin_value in memory.values():
    value_sum += int(bin_value, 2)

print(value_sum)