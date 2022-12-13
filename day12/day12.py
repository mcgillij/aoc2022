# Day 12 AOC 2022

from collections import deque

def breadth_first_search(start, end):
    queue = deque([start])
    distance = {start:0}
    while queue:
        position = queue.popleft()
        if position == end:
            return distance[end]
        queue.extend(unseen := [n for n in neighbs[position] if n not in distance])
        distance.update({n:distance[position] + 1 for n in unseen})

def neighbors(position):
    return {
        position + delta
        for delta in [1, 1j, -1, -1j]
        if position + delta in heatmap
        and ((heatmap[position + delta] - heatmap[position] <= 1)
        or heatmap[position + delta] < heatmap[position])
        }

with open('input') as f:
#with open('test_input') as f:
    data = f.read().splitlines()

heatmap = { complex(x, y): ord(h) for y, row in enumerate(data) for x, h in enumerate(row)}
start   = next(k for k,v in heatmap.items() if v == ord('S'))
end     = next(k for k,v in heatmap.items() if v == ord('E'))
heatmap.update({start:ord('a'), end:ord('z')})
neighbs = { position:neighbors(position) for position in heatmap }

# part1
print(f"part1: {breadth_first_search(start,end)}")
# part2
print(f"part2: {min(filter(None,(breadth_first_search(start,end) for start in heatmap if heatmap[start]==ord('a'))))}")
