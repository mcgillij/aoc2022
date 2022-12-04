# Day 4 AOC 2022

# test_input = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# """

# my_list = test_input.splitlines()


with open("input") as f:
    my_list = f.read().splitlines()

overlap = 0
encapsulated = 0
for elf_pair in my_list:
    first_elf, second_elf = elf_pair.split(",")

    first_elf_start, first_elf_end = [int(i) for i in first_elf.split("-")]
    second_elf_start, second_elf_end = [int(i) for i in second_elf.split("-")]

    first_elf_range = set([i for i in range(first_elf_start, first_elf_end+1)])
    second_elf_range = set([i for i in range(second_elf_start, second_elf_end+1)])

    if len(first_elf_range & second_elf_range) in [len(first_elf_range), len(second_elf_range)]:
        encapsulated += 1
    if first_elf_range & second_elf_range:
        overlap += 1

# part1
print(encapsulated)
# part2
print(overlap)
