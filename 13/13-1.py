from os.path import abspath, join, dirname

with open(abspath(join(dirname(__file__), 'input'))) as f:
    start_time = int(f.readline().strip())
    buses = [int(id) for id in f.readline().strip().split(sep=',') if id != 'x']

t = start_time
cont = True
while cont:
    for bus in buses:
        if t % bus == 0:
            print(bus, t, bus * (t - start_time))
            cont = False
            break
    t += 1
    