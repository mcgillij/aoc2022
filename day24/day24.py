# Day 24 AOC 2022

from collections import defaultdict
import heapq

def get_input() -> tuple:
    dir_dict = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    #with open("test_input") as f:
    with open("input") as f:
        lines = f.read().splitlines()
        board_height = len(lines) - 2
        board_width = len(lines[1]) - 2
        elf_start = (lines[0].index(".") - 1, -1)
        elf_end = (lines[-1].index(".") - 1, board_height)
        blizzards = [((x-1, y-1), dir_dict[lines[y][x]]) \
            for y in range(1, board_height+1) for x in range(1, board_width+1) if lines[y][x] in dir_dict]
        return elf_start, elf_end, blizzards, board_width, board_height

def move_blizzards(blizzards: dict, time: int) -> defaultdict:
    if time in blizzard_dict: return blizzard_dict[time]
    result = defaultdict(list)
    for blizzard in blizzards:
        x, y = (blizzard[0][0] + blizzard[1][0] * time) % board_width, \
            (blizzard[0][1] + blizzard[1][1] * time) % board_height
        result[(x, y)].append(blizzard)
    blizzard_dict[time] = result
    return result

def calc_moves(pos: tuple, blizzards: dict, time: int) -> list:
    delta_force = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    stuff = move_blizzards(blizzards, time+1)
    moves = []
    for delta in delta_force:
        x, y = pos[0] + delta[0], pos[1] + delta[1]
        if (x, y) not in stuff and ((x, y) == elf_end or (x, y) == elf_start or  x >= 0 and x < board_width and y >= 0 and y < board_height):
            moves.append((x, y))

    return moves

def find_path(blizzards: dict, start_pos: tuple, end_pos: tuple, time: int) -> int:
    heap = []
    heapq.heappush(heap, (0, start_pos, time))
    visited = set()

    while heap:
        _, pos, time = heapq.heappop(heap)
        if pos == end_pos:
            return time
        if (pos, time) not in visited:
            visited.add((pos, time))
            for move in calc_moves(pos, blizzards, time):
                heapq.heappush(heap, (abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1]) + time, move, time+1))

elf_start, elf_end, blizzards, board_width, board_height = get_input()
blizzard_dict = {}

part1 = find_path(blizzards, elf_start, elf_end, 0)
# part1
print(f"part1: {part1}")
# part2
print(f"part2: {find_path(blizzards, elf_start, elf_end, find_path(blizzards, elf_end, elf_start, part1))}")
