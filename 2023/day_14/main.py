################################################################################
#PART 1
################################################################################
with open("input.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]

rows = len(grid)
cols = len(grid[0])


for c in range(cols):
    for r in range(1, rows):
        if grid[r][c] == 'O':
            nr = r
            while nr > 0 and grid[nr-1][c] == '.':
                grid[nr-1][c], grid[nr][c] = grid[nr][c], grid[nr-1][c]
                nr -= 1


total_load = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'O':
            total_load += rows - r 

print(total_load)

################################################################################
#PART 2
################################################################################
from copy import deepcopy


def tilt_north(g):
    new_g = deepcopy(g)
    for c in range(cols):
        for r in range(1, rows):
            if new_g[r][c] == 'O':
                nr = r
                while nr > 0 and new_g[nr-1][c] == '.':
                    new_g[nr-1][c], new_g[nr][c] = new_g[nr][c], new_g[nr-1][c]
                    nr -= 1
    return new_g

def tilt_south(g):
    new_g = deepcopy(g)
    for c in range(cols):
        for r in range(rows-2, -1, -1):
            if new_g[r][c] == 'O':
                nr = r
                while nr < rows-1 and new_g[nr+1][c] == '.':
                    new_g[nr+1][c], new_g[nr][c] = new_g[nr][c], new_g[nr+1][c]
                    nr += 1
    return new_g

def tilt_west(g):
    new_g = deepcopy(g)
    for r in range(rows):
        for c in range(1, cols):
            if new_g[r][c] == 'O':
                nc = c
                while nc > 0 and new_g[r][nc-1] == '.':
                    new_g[r][nc-1], new_g[r][nc] = new_g[r][nc], new_g[r][nc-1]
                    nc -= 1
    return new_g

def tilt_east(g):
    new_g = deepcopy(g)
    for r in range(rows):
        for c in range(cols-2, -1, -1):
            if new_g[r][c] == 'O':
                nc = c
                while nc < cols-1 and new_g[r][nc+1] == '.':
                    new_g[r][nc+1], new_g[r][nc] = new_g[r][nc], new_g[r][nc+1]
                    nc += 1
    return new_g

def spin_cycle(g):
    g1 = tilt_north(g)
    g2 = tilt_west(g1)
    g3 = tilt_south(g2)
    g4 = tilt_east(g3)
    return g4

seen = {}
current_grid = deepcopy(grid)
total_cycles = 1_000_000_000
cycle_num = 0

while cycle_num < total_cycles:
    grid_tuple = tuple(tuple(row) for row in current_grid)
    if grid_tuple in seen:
        first_seen = seen[grid_tuple]
        cycle_length = cycle_num - first_seen
        remaining = (total_cycles - cycle_num) % cycle_length
        for _ in range(remaining):
            current_grid = spin_cycle(current_grid)
        break
    seen[grid_tuple] = cycle_num
    current_grid = spin_cycle(current_grid)
    cycle_num += 1
    
final_load = sum(rows - r for r in range(rows) for c in range(cols) if current_grid[r][c] == 'O')
print(final_load)