import operator

with open('input/day6.txt', 'r') as f:
    lines = f.read().splitlines()

#Solution 1

# Generate a list of operators based on the last line of the input
ops = lines[-1].strip().split()
ops_func = [operator.add if op=='+' else operator.mul for op in ops]

# Generate a list of integers, where the operators need to be applied on
numbers = [list(map(int, line.strip().split())) for line in lines[:-1]]

sum_lines = numbers[0]
for row in numbers[1:]:
    for c, (op, num) in enumerate(zip(ops_func,row)):
        sum_lines[c] = op(sum_lines[c], num)

print(f'Solution for day6/part1: {sum(sum_lines)}')

#Solution 2
cols = [list(c) for c in zip(*lines)]
ans2 = 0

for *nrs, op in cols:
    digits = ''.join(n for n in nrs if n.isdigit())
    if op in ('+', '*'):
        oper = operator.add if op == '+' else operator.mul
        interm = int(digits)
    elif digits:
        interm = oper(interm, int(digits))
    else: # Blank column
        ans2 += interm

ans2 += interm # last one does not have blank column behind it

print(f'Solution for day6/part2: {ans2}')