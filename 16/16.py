from os.path import abspath, dirname, join
from typing import Dict, List, Set

with open(abspath(join(dirname(__file__), 'input'))) as f:
    sections = [l.strip() for l in f.read().split(sep='\n\n')]

target_prefix = 'departure'


class field:
    def __init__(self, name: str, allowed_values: Set[int], num_possible_slots: int):
        self.name = name                                        # 'class'
        self.allowed_values = allowed_values                    # {25, 26, 27, 31, 32, 33, 34}
        self.possible_slots = set(range(num_possible_slots))    # {1, 2, 3, 4, 5, 6, 7}
        self.known_loc = None                                   # None / 3
    
    def is_allowed(self, value):
        return value in self.allowed_values

    def remove_slot(self, slot: int):
        self.possible_slots.discard(slot)
        if len(self.possible_slots) == 1:
            self.known_loc = self.possible_slots.pop()


# parse first section into a set of field objects
fields = set()
raw_fields = sections[0].split(sep='\n')
for raw_field in raw_fields:
    (field_name, raw_ranges) = raw_field.split(sep=': ')
    ranges = raw_ranges.split(' or ')
    allowed_values = set()
    for r in ranges:
        (lb, ub) = r.split('-')
        this_range = range(int(lb), int(ub) + 1)
        allowed_values.update(set(this_range))
    fields.add(field(field_name, allowed_values, len(raw_fields)))


# parse your ticket into a list of ints
your_ticket = [int(n) for n in sections[1].split(sep='\n')[1].split(sep=',')]

# parse nearby tickets into a list of lists of ints
nearby_tickets = []
for line in sections[2].split(sep='\n')[1:]:
    nearby_tickets.append([int(n) for n in line.split(sep=',')])


def is_valid_value(value: int) -> bool:
    for f in fields:
        if f.is_allowed(value):
            return True
    else:
        return False


def is_valid_ticket(ticket: List[int]) -> bool:
    for value in ticket:
        if not is_valid_value(value):
            return False
    else:
        return True


def part1():
    error_rate = 0
    for ticket in nearby_tickets:
        error_rate += sum([value for value in ticket if not is_valid_value(value)])
    
    return error_rate


def part2():
    pass


print(part1())
print(part2())

