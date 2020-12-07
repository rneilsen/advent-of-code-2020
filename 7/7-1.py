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


to_process = set([goal])    # bag types we haven't yet found containers of
processed = set()           # bag types we've already found containers of
while len(to_process) > 0:
    current = to_process.pop()
    if current in processed:
        continue            # skip if we've already done this one

    # find everything that can contain 'current', and add them to to_process
    for container in rules:
        if current in rules[container]:
            to_process.add(container)
    
    # finally, mark 'current' as processed
    processed.add(current)

print(len(processed) - 1)   # - 1 to not count the goal itself
            