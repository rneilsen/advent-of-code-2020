from os.path import abspath, join, dirname

with open(abspath(join(dirname(__file__), 'input'))) as f:
    code = [l.strip() for l in f.readlines()]

for test_pos in range(len(code)):
    newcode = code.copy()
    if code[test_pos][:3] == 'jmp':
        newcode[test_pos] = 'nop' + code[test_pos][3:]
    elif code[test_pos][:3] == 'nop':
        newcode[test_pos] = 'jmp' + code[test_pos][3:]
    else:
        continue    # skip this attempt if not substituting jmp/nop
    
    acc = 0
    cur_inst = 0
    times_run = [0 for inst in code]

    while cur_inst < len(newcode):
        if times_run[cur_inst] == 1:
            # print('Terminated: loop, acc =', acc)
            break
        times_run[cur_inst] += 1

        (cmd, val) = newcode[cur_inst].split(sep=' ')
        val = int(val)
        
        if cmd == 'acc':
            acc += val
            cur_inst += 1
        elif cmd == 'jmp':
            cur_inst += val
        elif cmd == 'nop':
            cur_inst += 1
    else:
        print('Terminated: end of code, acc =', acc)
