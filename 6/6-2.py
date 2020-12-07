from os.path import abspath, join, dirname

with open(abspath(join(dirname(__file__), 'input'))) as f:
    raw_input = f.read()

# process raw input into list of groups (each group is a list)
groups = [g.split() for g in raw_input.split(sep='\n\n')]

# iterate through each group
count_sum = 0
for group in groups:
    # use first person's responses as starting point
    questions = set(group[0])
    
    # intersection-update with questions by all other members of group
    # (note if group has only 1 person, this will not do anything)
    for p in group[1:]:
        questions &= set(p)
    
    count_sum += len(questions)

print(count_sum)