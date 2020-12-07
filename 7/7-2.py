from os.path import abspath, join, dirname
from collections import Counter

goal = 'shiny gold'

with open(abspath(join(dirname(__file__), 'input'))) as f:
    raw_rules = f.readlines()

rules = {}

# parse the horrible input file into a 'rules' dict
for raw in raw_rules:
    raw = raw.rstrip('.\n')
    raw = raw.replace(' bags', '')
    raw = raw.replace(' bag', '')
    (container_type, contained_raw) = raw.split(sep = ' contain ')
    if contained_raw == 'no other':
        rules[container_type] = Counter()
        continue
    contained_list = contained_raw.split(sep = ', ')
    contained_set = Counter()
    for contained in contained_list:
        (num_contained, contained_type) = contained.split(sep=' ', maxsplit=1)
        contained_set[contained_type] = int(num_contained)
    rules[container_type] = contained_set


total_bags = 0
to_process = Counter({goal: 1})

# take a class of bags from 'to_process', add however many of them we have so far,
# then add everything in them to 'to_process'
while len(to_process) > 0:
    (current, num_current) = to_process.popitem()
    total_bags += num_current
    for contained_bag in rules[current]:
        to_process[contained_bag] += num_current * rules[current][contained_bag]

print(total_bags - 1)   # -1 to not count goal itself
            