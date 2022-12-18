# Day 18 AOC 2022

from itertools import combinations
from typing import List, Set, Tuple

def are_neighbors(a: tuple, b: tuple) -> int:
  return sum(abs(d1 - d2) for d1, d2 in zip(a, b)) == 1


def get_neighbors(point: tuple, minv: int, maxv: int) -> Set:
  candidates = set()
  for delta in [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]:
    new_point = tuple([d+offset for d,offset in zip(point,delta)])
    if not all([d >= minv and d <= maxv for d in new_point]):
        continue
    candidates.add(new_point)
  return candidates


def calculate(data: List) -> Tuple[int, int]:
  part1 = 6 * len(data)
  for a, b in combinations(data, 2):
    if not are_neighbors(a,b):
        continue
    part1 -= 2

  part2 = 0
  data_set = set(data)
  minv = min(min(point) for point in data_set) -1
  maxv = max(max(point) for point in data_set) +1
  nodes = [(minv, minv, minv)]
  visited = {nodes[0]}
  while nodes:
    node = nodes.pop()
    for neighbor in get_neighbors(node, minv, maxv):
      if neighbor in visited:
          continue
      if neighbor in data_set:
          part2 += 1
      else:
        visited.add(neighbor)
        nodes.append(neighbor)  

  return part1, part2


with open("input") as f:
#with open("test_input") as f:
    data = [tuple(map(int, line.split(','))) for line in f.readlines()]

part1, part2 = calculate(data)
# part1
print(f"{part1=}")
# part2
print(f"{part2=}")
