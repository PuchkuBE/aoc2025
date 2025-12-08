with open('input/day7.txt', 'r') as f:
    lines = f.read().splitlines()

def nr_splits(input):
    oldstate = input[0]
    ans1 = 0
    for actions in input[1:]:
        newstate = oldstate[:]
        for idx, action in enumerate(actions):
            if action == '^' and oldstate[idx] == '|':
                newstate = newstate[:idx-1] + '|.|'+newstate[idx+2:] 
                ans1 += 1
        oldstate = newstate
    return ans1

with open('input/day7.txt', 'r') as f:
    lines = f.read().splitlines()

lines[0] = lines[0].replace('S','|')

print(f'Solution for day7/part1: {nr_splits(lines)}')