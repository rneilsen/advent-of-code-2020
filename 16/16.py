from os.path import abspath, dirname, join
from typing import Dict, List

with open(abspath(join(dirname(__file__), 'input'))) as f:
    sections = [l.strip() for l in f.read().split(sep='\n\n')]

# parse identified fields into dict:
# key = name of field
# value = list of range objects
fields = {}
raw_fields = sections[0].split(sep='\n')
for raw_field in raw_fields:
    (field_name, raw_ranges) = raw_field.split(sep=': ')
    ranges = raw_ranges.split(' or ')
    fields[field_name] = []
    for r in ranges:
        (lb, ub) = r.split('-')
        fields[field_name].append(range(int(lb), int(ub) + 1))
    
# parse your ticket into a list of ints
your_ticket = [int(n) for n in sections[1].split(sep='\n')[1].split(sep=',')]

# parse nearby tickets into a list of lists of ints
nearby_tickets = []
for line in sections[2].split(sep='\n')[1:]:
    nearby_tickets.append([int(n) for n in line.split(sep=',')])

def part1(fields, nearby_tickets):
    # gather all allowable field ranges into a large set of allowed values
    allowed_values = set()
    for ranges in fields.values():
        for r in ranges:
            allowed_values.update(set(r))

    error_rate = 0
    for ticket in nearby_tickets:
        error_rate += sum([value for value in ticket if value not in allowed_values])
    
    return error_rate

print(part1(fields,nearby_tickets))

