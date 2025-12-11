import ast
from functools import reduce
from itertools import combinations, combinations_with_replacement

lines = open('input/day10.txt','r').read().splitlines()

#Format:
#[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}

# Data structures
##################
# lights: a tuple of booleans, True indicates which lights need to be on the start the machine
# e.g. (False, True, True, False)
#
# Buttons: list of button
# Each button is represented as a boolean tuple, indicating which lights will be toggled by the button
# e.g. (False, False, True, False)

def minimum_switches(lights: tuple[bool], buttons:list[tuple]) -> int:
    for i in range(1,len(buttons)):
        for btns in combinations(buttons, i):
            red = reduce(lambda a, b: tuple(x ^ y for x, y in zip(a, b)), btns)
            if red == lights:
                return i
    return 999

def minimum_joltages(joltages: tuple[int], buttons:list[tuple]) -> int:
    for i in range(1,999):
        for btns in combinations_with_replacement(buttons, i):
            if joltages == reduce(lambda a, b: tuple(x + y for x, y in zip(a, b)), btns):
                print(f'Solution found for {joltages} in {i} toggles')
                return i
    return 999

ans1 = ans2 = 0
for line in lines:
    lights, *list_buttons, joltage = line.split(" ")
    # Turn the lights string into a list of booleans (on/off)
    lights = tuple(c=='#' for c in lights if c not in ['[',']'])

    bool_buttons = []
    int_buttons = [] # For part 2
    for buttons in list_buttons:
        # Each button is like (1,3,4) or 3
        b = ast.literal_eval(buttons)
        if isinstance(b, int):
            b = (b,)
        bool_buttons.append(tuple(i in b for i in range(len(lights))))
        int_buttons.append(tuple(1 if i in b else 0 for i in range(len(lights))))
  
    # Store the joltages as a tuple
    joltage = tuple(map(int,joltage[1:-1].split(",")))
    ans1 += minimum_switches(lights, bool_buttons)
    ans2 += minimum_joltages(joltage, int_buttons)


print(f'Solution for day10/part1: {ans1}')
print(f'Solution for day10/part2: {ans2}')
