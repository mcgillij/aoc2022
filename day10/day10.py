# Day 10 AOC 2022

#with open("test_input") as f:
with open("input") as f:
    data = f.read().strip()

part1 = []
cycles = []
for line in data.split("\n"):
    cycles.extend([0] if line == "noop" else [0, int(line.split()[1])])

for i in range(20, 221, 40):
    part1.append(i * (sum(cycles[:i-1]) + 1))

print(f"Part 1: {sum(part1)}")

print("Part 2:")
screen = [["."] * 40 for _ in range(6)]
for c in range(len(cycles)):
    x = sum(cycles[:c]) + 1
    if c % 40 in range(x - 1, x + 2):
        screen[c//40][c%40] = "#"

for line in screen:
    print("".join([p if p == "#" else " " for p in line]))
