# Day 3 AOC 2022

from string import ascii_letters
from itertools import count

# test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# """

# my_list = test_input.splitlines()

CHAR_VALUES = dict(zip(ascii_letters, count(1)))

with open("input") as f:
    my_list = f.read().splitlines()

def part1(sacks):
    priorities = 0
    for bag in sacks:
        middle = len(bag) // 2
        left_sack = bag[:middle]
        right_sack = bag[middle:]
        in_both = list(set(left_sack) & set(right_sack))[0]
        priorities += CHAR_VALUES[in_both]
    return priorities

def part2(sacks):
    priorities = 0
    for i in range(0, len(sacks) -2, 3): # iterate over groups
        elf_packs = map(set, sacks[i:i+3]) # group of elves
        in_all = set.intersection(*elf_packs).pop()
        priorities += CHAR_VALUES[in_all]

    return priorities

# part1
print(f"part1: {part1(my_list)}")
# part2
print(f"part2: {part2(my_list)}")
