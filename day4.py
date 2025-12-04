lines = open('input/day4.txt','r').read().splitlines()

def isReachable(row, col, grid):
    rolls_around = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                if grid[r][c] in {'@', 'x'}:
                    rolls_around += 1
    return rolls_around < 5

ans1 = 0
ans2 = 0
first_loop = True
while True:
    prev_ans2 = ans2
    # Cleanup removed roles
    lines = [l.replace('x', '.') for l in lines]
    for idx_row, row in enumerate(lines):
        for idx_col, val in enumerate(row):
            # If we are on a roll, check if reachable
            if val == '@' and isReachable(idx_row, idx_col, lines):
                lines[idx_row] = lines[idx_row][:idx_col] + 'x' + lines[idx_row][idx_col+1:]
                ans2 += 1
                if first_loop: # In the first loop, determine the initial reachability
                    ans1 += 1
    first_loop = False
    if ans2 == prev_ans2:
        break

print(f'Solution for day4/part1: {ans1}')
print(f'Solution for day4/part2: {ans2}')