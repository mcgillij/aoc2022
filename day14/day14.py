# Day 14 AOC 2022

lines = []
#with open("test_input") as f:
with open("input") as f:
    for data in f:
        line = data.strip().split(" -> ")
        for n, l in enumerate(line):
            x, y = [int(i) for i in l.split(",")]
            line[n] = (x, y)
        lines.append(tuple(line))

rocks = set()
lowest_y = 10
for l in lines:
    x, y = l[0]
    rocks.add((x, y))
    for k in range(1, len(l)):
        tx, ty = l[k]
        while tx > x:
            x += 1
            rocks.add((x,y))
        while tx < x:
            x -= 1
            rocks.add((x,y))
        while ty > y:
            y += 1
            rocks.add((x,y))
            if y > lowest_y:
                lowest_y = y
        while ty < y:
            y -= 1
            rocks.add((x,y))

sand = set()
not_void = True
part1_finished = False
part1 = 0
while not_void:
    x, y = 500,0
    falling = True
    while falling:
        if y > lowest_y:
            if not(part1_finished):
                part1 = len(sand)
                part1_finished = True
            sand.add((x,y))
            break
        nx, ny = x, y+1
        if (nx,ny) not in rocks and (nx,ny) not in sand:
            x, y = nx, ny
            continue
        nx, ny = x-1, y+1
        if (nx,ny) not in rocks and (nx,ny) not in sand:
            x, y = nx, ny
            continue
        nx, ny = x+1, y+1
        if (nx,ny) not in rocks and (nx,ny) not in sand:
            x, y = nx, ny
            continue
        sand.add((x,y))
        if (x,y) == (500,0):
            not_void = False
            break
        falling = False
        break

part2 = len(sand)

# part1
print(f"{part1=}")
# part2
print(f"{part2=}")
