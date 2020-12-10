from os.path import abspath, join, dirname

with open(abspath(join(dirname(__file__), 'input'))) as f:
    code = [l.strip() for l in f.readlines()]

acc = 0
cur_inst = 0
times_run = [0 for inst in code]

while max(times_run) < 2:
    if times_run[cur_inst] == 1:
        print(acc)
        break
    times_run[cur_inst] += 1

    (cmd, val) = code[cur_inst].split(sep=' ')
    val = int(val)
    
    if cmd == 'acc':
        acc += val
        cur_inst += 1
    elif cmd == 'jmp':
        cur_inst += val
    elif cmd == 'nop':
        cur_inst += 1
