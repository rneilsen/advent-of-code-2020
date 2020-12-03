from os.path import abspath, join, dirname

tree = '#'
right_step = 3
down_step = 1

# Read input from file
with open(abspath(join(dirname(__file__), 'input'))) as f:
    rows = f.read().splitlines()
num_rows = len(rows)
num_cols = len(rows[0])

(cur_row, cur_col) = (0, 0)

num_trees = 0
while cur_row < num_rows:
    if rows[cur_row][cur_col] == tree:
        num_trees += 1
    
    cur_row += 1
    # wrap around to left side again (simulates repeated blocks)
    cur_col = (cur_col + right_step) % num_cols
    
print(num_trees)