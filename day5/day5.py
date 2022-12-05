# Day 5 AOC 2022

# test_input = """    [D]    
# [N] [C]    
# [Z] [M] [P]
 # 1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# """

#data = test_input.splitlines()

import re

with open("input") as f:
   data = f.readlines()

stacks = []
moves = []
for line in data:
    if '[' in line:
        for index, c in enumerate(line):
            if index >= len(stacks):
                stacks.append([])
            if c.isalpha():
                stacks[index].append(c)
    if 'move' in line:
        moves.append(list(map(int, (re.findall(r'\d+', line)))))
stacks = [s[::-1] for s in filter(lambda l: len(l), stacks)]


def part1(stacks, moves):
    for times, source, destination in moves:
        for _ in range(times):
            stacks[destination - 1].append(stacks[source - 1].pop())
    return ''.join(s[-1] for s in stacks)


def part2(stacks, moves):
    for times, source, destination in moves:
        stacks[destination - 1] += stacks[source - 1][-times:]
        stacks[source - 1] = stacks[source - 1][:-times]
    return ''.join(s[-1] for s in stacks)

# part1
print("Part 1:", part1([s.copy() for s in stacks], moves))
# part2
print("Part 2:", part2(stacks, moves))
