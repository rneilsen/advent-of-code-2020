from os.path import abspath, dirname, join

mask_length = 36

with open(abspath(join(dirname(__file__), 'input'))) as f:
    lines = [line.strip().split(sep=' = ') for line in f.readlines()]

memory = {}
mask = 'X' * mask_length
for line in lines:
    if line[0] == 'mask':
        mask = line[1]
    else:
        addr = int(''.join([c for c in line[0] if c.isnumeric()]))
        raw_value = bin(int(line[1]))[2:].zfill(mask_length)
        masked_value = ''
        for i in range(mask_length):
            if mask[i] == 'X':
                masked_value += raw_value[i]
            else:
                masked_value += mask[i]
        memory[addr] = masked_value

value_sum = 0
for bin_value in memory.values():
    value_sum += int(bin_value, 2)

print(value_sum)