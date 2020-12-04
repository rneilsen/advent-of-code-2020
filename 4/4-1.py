from os.path import abspath, join, dirname

REQD_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open(abspath(join(dirname(__file__), 'input'))) as f:
    raw_input = f.read()

# process raw input into a list of dicts (each dict is one passport)
raw_passports = [p.split() for p in raw_input.split(sep='\n\n')]
passports = []
for raw_passport in raw_passports:
    passport = {}
    for entry in raw_passport:
        (key, val) = entry.split(sep=':')
        passport[key] = val
    passports.append(passport)

# count valid passports
num_valid = 0
for passport in passports:
    valid = True
    for field in REQD_FIELDS:
        if field not in passport:
            valid = False
            break
    if valid:
        num_valid += 1

print(num_valid)