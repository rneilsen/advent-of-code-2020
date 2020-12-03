from os.path import abspath, join, dirname

tree = '#'
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

# Read input from file
with open(abspath(join(dirname(__file__), 'input'))) as f:
    rows = f.read().splitlines()
num_rows = len(rows)
num_cols = len(rows[0])

slope_tree_product = 1
for slope in slopes: # iterate through list of prescribed slopes
    (right_step, down_step) = slope
    (cur_row, cur_col) = (0, 0)
    num_trees = 0

    # follow slope through map and count trees
    while cur_row < num_rows:
        if rows[cur_row][cur_col] == tree:
            num_trees += 1
        
        cur_row += down_step
        # wrap around to left side again (simulates repeated blocks)
        cur_col = (cur_col + right_step) % num_cols
    
    slope_tree_product *= num_trees
    
print(slope_tree_product)