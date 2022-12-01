# Day 1 AOC 2022

# test_input = """1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000"""

#my_list = test_input.splitlines()

with open("input") as f:
    my_list = f.read().splitlines()

# on each blank line we need to add the number of elves
# and append the values to a new list
elf_list = []
new_aggregate_list = []
for line in my_list:
    if line == "":
        new_aggregate_list.append(elf_list)
        elf_list = []
    else:
        elf_list.append(line)

totals = [sum(int(x) for x in l) for l in new_aggregate_list]

# part 1
print(f"part1: {max(totals)}")
# part 2
sorted_totals = sorted(totals, reverse=True)[:3]
print(f"part2: {sum(sorted_totals)}")
