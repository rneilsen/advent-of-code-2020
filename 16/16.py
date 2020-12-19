from os.path import abspath, dirname, join
from typing import Dict, List, Set

with open(abspath(join(dirname(__file__), 'input'))) as f:
    sections = [l.strip() for l in f.read().split(sep='\n\n')]

target_prefix = 'departure'


class Field:
    def __init__(self, name: str, allowed_values: Set[int], num_possible_slots: int):
        self.name = name                                        # 'class'
        self.allowed_values = allowed_values                    # {25, 26, 27, 31, 32, 33, 34}
        self.possible_slots = set(range(num_possible_slots))    # {1, 2, 3, 4, 5, 6, 7}
        self.known_loc = None                                   # None / 3
    
    def is_allowed(self, value: int) -> bool:
        return value in self.allowed_values

    def remove_slot(self, slot: int) -> bool:
        # return True if slot was actually removed
        if slot in self.possible_slots:
            self.possible_slots.remove(slot)
            if len(self.possible_slots) == 1:
                self.known_loc = self.possible_slots.pop()
            return True
        else:
            return False

    
    def is_possible_slot(self, slot: int) -> bool:
        return slot in self.possible_slots
    
    def __repr__(self):
        if self.known_loc is not None:
            return f"<{self.name}: {self.known_loc}>"
        else:
            return f"<{self.name}: {self.possible_slots}>"


# parse first section into a set of Field objects
fields = set()
raw_fields = sections[0].split(sep='\n')
num_fields = len(raw_fields)
for raw_field in raw_fields:
    (field_name, raw_ranges) = raw_field.split(sep=': ')
    ranges = raw_ranges.split(' or ')
    allowed_values = set()
    for r in ranges:
        (lb, ub) = r.split('-')
        this_range = range(int(lb), int(ub) + 1)
        allowed_values.update(set(this_range))
    fields.add(Field(field_name, allowed_values, num_fields))


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
    valid_tickets = [t for t in nearby_tickets if is_valid_ticket(t)]

    potential_fields = [fields.copy() for i in range(num_fields)]    # [{Field1, Field2}, {Field1, Field3}, {Field2}, ...]
    
    # first pass: identify which slots can't be valid based on nearby valid tickets    
    for ticket in valid_tickets:
        for i in range(num_fields):
            cur_value = ticket[i]
            for field in fields:
                if not field.is_allowed(cur_value):
                    field.remove_slot(i)    # this field can't correspond to this slot
                    potential_fields[i].discard(field)   # this slot can't contain this field
    
    # second pass: inferences based on slots with only one field 
    # and fields with only one slot
    update_needed = True
    while update_needed:
        update_needed = False
        for field in fields:
            if field.known_loc is not None:
                for other_field in fields:
                    if other_field != field:
                        update_needed = update_needed or other_field.remove_slot(field.known_loc)
        
        for slot in range(num_fields):
            if len(potential_fields[slot]) == 1:
                for other_slot in range(num_fields):
                    if other_slot != slot:
                        if slot in potential_fields[other_slot]:
                            potential_fields[other_slot].remove(slot)
                            update_needed = True
    
    product = 1
    for field in fields:
        if field.name[:len(target_prefix)] == target_prefix:
            product *= your_ticket[field.known_loc]

    return product    
    

print("Part 1:", part1())
print("Part 2:", part2())

pass
