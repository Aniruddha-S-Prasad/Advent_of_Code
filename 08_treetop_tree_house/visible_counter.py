import numpy as np

with open('input.txt', 'r') as height_map_file:
    height_map =[]
    for line in height_map_file:
        line = line.strip()
        row = []
        for height in line:
            row.append(int(height))
        height_map.append(row)

height_map = np.array(height_map)
visible_map = np.full(height_map.shape, 0)

for n_row, row in enumerate(height_map):
    for n_col, tree_height in enumerate(row):
        if n_col == 0 or n_col == (row.shape[0]-1):
            visible_map[n_row, n_col] = 1
        elif tree_height > row[:n_col].max() or tree_height > row[n_col+1:].max():
            visible_map[n_row, n_col] = 1

for n_col, col in enumerate(height_map.T):
    for n_row, tree_height in enumerate(col):
        if n_row == 0 or n_row == (col.shape[0]-1):
            visible_map[n_row, n_col] = 1
        elif tree_height > col[:n_row].max() or tree_height > col[n_row+1:].max():
            visible_map[n_row, n_col] = 1

print(visible_map.sum())

