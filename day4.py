with open('input/day4.txt', 'r') as f:
    lines = f.read().splitlines()

grid = [list(row) for row in lines]
rows = len(grid)
cols = len(grid[0])

area = ((-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1))

def isReachable(row, col, grid):
    res = [1 if grid[row+dr][col+dc] in {'@', 'x'} else 0 for dr, dc in area if 0 <= row+dr < rows and 0 <= col+dc < cols]
    return sum(res) < 4

ans1 = 0
ans2 = 0
first_loop = True
while True:
    # Clean up the x's in grid first
    grid = [['.' if c == 'x' else c for c in r] for r in grid]
    # Mark reachable with x
    grid = [['x' if c=='@' and isReachable(ir, ic, grid) else c for ic, c in enumerate(r)] for ir, r in enumerate(grid)]
    nr_x = sum(row.count('x') for row in grid)
    ans2 += nr_x
    if first_loop:
        ans1 = nr_x
        first_loop = False
    if nr_x == 0:
        break

print(f'Solution for day4/part1: {ans1}')
print(f'Solution for day4/part2: {ans2}')