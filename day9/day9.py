# Day 9 AOC 2022

test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

from typing import List, Tuple, Set

def sign(x: int) -> int:
    return (x > 0) - (x < 0) # True = 1, False = 0

def move_tail(e1: List, e2: List):
    xdelta = e1[0] - e2[0]
    ydelta = e1[1] - e2[1]
    if abs(xdelta) > 1 or abs(ydelta) > 1:
        e2[0] += sign(xdelta)
        e2[1] += sign(ydelta)

def move_head(head: List, direction: str):
    head[0] += 1 if direction == 'R' else -1 if direction == 'L' else 0
    head[1] += 1 if direction == 'D' else -1 if direction == 'U' else 0

def move(rope: List, direction: str) -> Tuple:
    move_head(rope[0], direction)

    for i in range(1, len(rope)): # move tail
        move_tail(rope[i-1], rope[i])

    return tuple(rope[-1]) # return position of rope end

def simulate(rope: List) -> Set[Tuple]:
    #return { move(rope, direction) for direction, num in (line.split() for line in test_input.splitlines()) # test with the test_input
    return { move(rope, direction) for direction, num in (line.split() for line in open("input").read().splitlines())
                                   for _ in range(int(num)) }

# part1
print(f"part1: {len(simulate([[0, 0] for _ in range(2)]))}")
# part2
print(f"part2: {len(simulate([[0, 0] for _ in range(10)]))}")
