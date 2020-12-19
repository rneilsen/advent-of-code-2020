from os.path import abspath, dirname, join
from typing import Dict, List

with open(abspath(join(dirname(__file__), 'input'))) as f:
    sections = [l.strip() for l in f.read().split(sep='\n\n')]

target_prefix = 'departure'

# parse identified fields into dict:
# key = name of field
# value = set of allowable values
# also create master list of all allowed values for finding invalid tickets
fields = {}
raw_fields = sections[0].split(sep='\n')
allowed_values = set()
for raw_field in raw_fields:
    (field_name, raw_ranges) = raw_field.split(sep=': ')
    ranges = raw_ranges.split(' or ')
    fields[field_name] = set()
    for r in ranges:
        (lb, ub) = r.split('-')
        this_range = range(int(lb), int(ub) + 1)
        fields[field_name].update(set(this_range))
        allowed_values.update(set(this_range))


# parse your ticket into a list of ints
your_ticket = [int(n) for n in sections[1].split(sep='\n')[1].split(sep=',')]

# parse nearby tickets into a list of lists of ints
nearby_tickets = []
for line in sections[2].split(sep='\n')[1:]:
    nearby_tickets.append([int(n) for n in line.split(sep=',')])


def is_valid(ticket):
    for value in ticket:
        if value not in allowed_values:
            return False
    else:
        return True


def part1():
    error_rate = 0
    for ticket in nearby_tickets:
        error_rate += sum([value for value in ticket if value not in allowed_values])
    
    return error_rate


def part2():
    num_values = len(your_ticket)
    potential_locations = [set(fields.keys()) for n in range(num_values)]
    num_pls = {}    # number of potential locs for each field
    for field in fields:
        num_pls[field] = num_values
    
    valid_tickets = list(filter(is_valid, nearby_tickets))
    for ticket in valid_tickets:
        for i in range(num_values):
            for field in fields:
                if ticket[i] not in fields[field]:
                    potential_locations[i].discard(field)
                    num_pls[field] -= 1
                    if len(potential_locations[i]) == 1:
                        isolated_field = next(iter(potential_locations[i]))
                        for p in potential_locations[:i] + potential_locations[i+1:]:
                            p.discard(isolated_field)
        for field in fields:
            if num_pls[field] == 1:
                potential_locations = {field}
                for other_field in fields:
                    if other_field == field:
                        continue
                    else:
                        potential_locations[other_field].discard(field)
    
    locations = {}
    for i in range(num_values):
        locations[potential_locations[i].pop()] = i
    
    product = 1
    for field in locations:
        if field.find(target_prefix) == 0:
            product *= your_ticket[locations[field]]
    
    return product


print(part1())
print(part2())

