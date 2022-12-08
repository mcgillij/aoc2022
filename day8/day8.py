# Day 8 AOC 2022

# test_input = """30373
# 25512
# 65332
# 33549
# 35390
# """

from typing import List, Tuple

with open("input") as f:
    grid = [[int(x) for x in lines[:-1]] for lines in f.readlines()]

MAX = len(grid)

def is_visible(row: List , column: List, tree_height: int) -> Tuple:
    visible = [1,1,1,1]
    visible_trees = [0,0,0,0]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    for i in range(4):
        rr, cc = row + dr[i], column + dc[i]
        while 0 <= rr < MAX and 0 <= cc < MAX:
            visible_trees[i] += 1
            if grid[rr][cc] >= tree_height:
                visible[i] = 0
                break
            rr, cc = rr + dr[i], cc + dc[i]
    if 1 in visible:
        return True, visible_trees
    else:
        return False, visible_trees

count, score = 0, []
for row, R in  enumerate(grid):
    for column, tree_height in enumerate(R):
        v, visible_trees = is_visible(row, column, tree_height)
        if v:
            count += 1
            score.append(visible_trees[0] * visible_trees[1] * visible_trees[2] * visible_trees[3])

# part1
print(f"part1: {count}")
# part2
print(f"part2: {max(score)}")
