from os.path import abspath, join, dirname

with open(abspath(join(dirname(__file__), 'input'))) as f:
    raw_input = f.read()

# process raw input into list of groups (each group is a list)
groups = [g.split() for g in raw_input.split(sep='\n\n')]

# iterate through each group
count_sum = 0
for group in groups:
    questions = set()
    
    # gather all questions asked by each person in group
    for p in group:
        for q in p:
            questions.add(q)
    
    count_sum += len(questions)

print(count_sum)