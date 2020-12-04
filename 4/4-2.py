from os.path import abspath, join, dirname
from re import fullmatch

REQD_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# with open(abspath(join(dirname(__file__), 'input'))) as f:
with open('input') as f:
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
    invalidations = []

    # Validate all fields as per specification:
    try:    # if any fields hit exceptions, reject as invalid passport
        
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not 1920 <= int(passport['byr']) <= 2002:
            valid = False
            invalidations.append('byr')
            # continue

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not 2010 <= int(passport['iyr']) <= 2020:
            valid = False
            invalidations.append('iyr')
            # continue

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not 2020 <= int(passport['eyr']) <= 2030:
            valid = False
            invalidations.append('eyr')
            # continue
        
        # hgt (Height) - a number followed by either cm or in:
        if fullmatch('[0-9]+cm', passport['hgt']):
            # If cm, the number must be at least 150 and at most 193.
            if not 150 <= int(passport['hgt'][:-2]) <= 193:
                valid = False
                invalidations.append('hgt')
                # continue
        elif fullmatch('[0-9]+in', passport['hgt']):
            # If in, the number must be at least 59 and at most 76.
            if not 59 <= int(passport['hgt'][:-2]) <= 76:
                valid = False
                invalidations.append('hgt')
                # continue
        else:
            # height was not in valid format
            valid = False
            invalidations.append('hgt')
            # continue

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not fullmatch('#[0-9a-f]{6}', passport['hcl']):
            valid = False
            invalidations.append('hcl')
            # continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if passport['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            valid = False
            invalidations.append('ecl')
            # continue
        
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not fullmatch('[0-9]{9}', passport['pid']):
            valid = False
            invalidations.append('pid')
            # continue
        
        # cid (Country ID) - ignored, missing or not.

    except:
        # invalid or missing fields
        valid = False
        invalidations.append('EXC')
    
    display = ', '.join([f"{key} = {passport[key]}" for key in sorted(passport) if key != 'cid'])
    if valid:
        num_valid += 1
        print("VALID:", display)
    else:
        pass
        # print("INVLD:", display, invalidations)


print(num_valid)