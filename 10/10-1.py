from os.path import abspath, join, dirname

with open(abspath(join(dirname(__file__), 'input'))) as f:
    adaps = [0] + [int(l.strip()) for l in f.readlines()]

adaps.sort()
adaps.append(adaps[-1] + 3)

diffs = [adaps[i+1] - adaps[i] for i in range(len(adaps) - 1)]
print(diffs.count(3) * diffs.count(1))