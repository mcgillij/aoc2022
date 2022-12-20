# Day 20 AOC 2022

from collections import deque

def decrypt(nums: deque[tuple[int, int]]) -> None:
    for idx in range(len(nums)):
        while idx != nums[0][0]:
            nums.rotate(-1)

        i, n = nums.popleft()
        nums.rotate(-n)
        nums.appendleft((i, n))
        nums.rotate(n)

def sum_coords(nums: deque[tuple[int, int]]) -> int:
    while nums[0][1] != 0:
        nums.rotate(-1)

    total = 0
    for _ in range(1, 4):
        nums.rotate(-1000)
        total += nums[0][1]

    return total

def part1_decrypt(nums: deque[tuple[int, int]]) -> int:
    decrypt(nums)
    return sum_coords(nums)

def part2_decrypt(nums: deque[tuple[int, int]]) -> int:
    for _ in range(10):
        decrypt(nums)
    return sum_coords(nums)

DECRYPTION_KEY = 811589153

#with open("test_input") as f:
with open("input") as f:
    part1 = deque([(i, int(x.rstrip())) for i, x in enumerate(f.readlines())])
    part2 = deque([(i, n * DECRYPTION_KEY) for i, n in part1])

part1 = part1_decrypt(part1)
print(f"{part1=}")

part2 = part2_decrypt(part2)
print(f"{part2=}")
