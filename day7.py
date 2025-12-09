with open('input/day7.txt', 'r') as f:
    lines = f.read().splitlines()

def nr_splits(input):
    oldstate = input[0]
    ans1 = 0
    for actions in input[1:]:
        newstate = oldstate[:]
        for idx, action in enumerate(actions):
            if action == '^' and type(oldstate[idx]) is int and oldstate[idx] > 0: 
                newstate[idx-1] += oldstate[idx]
                newstate[idx] = 0
                newstate[idx+1] += oldstate[idx]
                ans1 += 1
        oldstate = newstate
    ans2 = sum(oldstate)
    return ans1, ans2

with open('input/day7.txt', 'r') as f:
    lines = f.read().splitlines()

lines = [
    [1 if c == 'S' else 0 if c == '.' else c for c in line]
    for line in lines
]
ans1, ans2 = nr_splits(lines)
print(f'Solution for day7/part1: {ans1}')
print(f'Solution for day7/part2: {ans2}')