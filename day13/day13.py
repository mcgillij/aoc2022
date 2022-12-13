# Day 13 AOC 2022

from itertools import zip_longest
from functools import cmp_to_key


def compare(a, b):
    if a is None:
        return -1
    elif b is None:
        return 1
    elif isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else 1 if b < a else 0
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        for x, y in zip_longest(a, b):
            if (result := compare(x, y)) == 0:
                continue
            return result
        return 0


#with open("test_input") as f:
with open("input") as f:
    pairs = [list(map(eval, x.split())) for x in f.read().strip().split("\n\n")]

# part1
print(f"part1: {sum(i + 1 for i, (a, b) in enumerate(pairs) if compare(a, b) < 0)}")
# part2
packets = [x for y in pairs for x in y] + [[[2]], [[6]]]
sorted_packets = sorted(packets, key=cmp_to_key(compare))
print(f"part2: {(sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)}")
