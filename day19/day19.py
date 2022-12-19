# Day 19 AOC 2022

import sys
import functools
from typing import List

sys.setrecursionlimit(100000)


def calculate(blueprint: List, time: int) -> int:
    ore_cost = blueprint[0]
    clay_cost = blueprint[1]
    obs_cost = blueprint[2]
    geo_cost = blueprint[3]

    max_ore_cost = max(ore_cost, clay_cost, obs_cost[0], geo_cost[0])

    @functools.cache
    def calculate_geodes(
            time_left: int,
            ores: int,
            clay: int,
            obsidian: int,
            o_bot: int,
            c_bot: int,
            ob_bot:int,
            ) -> int:
        if time_left <= 0:
            return 0

        new_ores = ores + o_bot
        new_clay = clay + c_bot
        new_obs = obsidian + ob_bot

        best = 0

        # build robot
        if ores >= geo_cost[0] and obsidian >= geo_cost[1]:
            best = max(
                    best,
                    (time_left - 1)
                    + calculate_geodes(
                        time_left - 1,
                        new_ores - geo_cost[0],
                        new_clay,
                        new_obs - geo_cost[1],
                        o_bot,
                        c_bot,
                        ob_bot,
                        ),
                    )
        else:
            if ores >= ore_cost:
                best = max(
                        best,
                        calculate_geodes(
                            time_left - 1,
                            new_ores - ore_cost,
                            new_clay,
                            new_obs,
                            o_bot + 1,
                            c_bot,
                            ob_bot,
                            ),
                        )

            if ores >= clay_cost:
                best = max(
                        best,
                        calculate_geodes(
                            time_left - 1,
                            new_ores - clay_cost,
                            new_clay,
                            new_obs,
                            o_bot,
                            c_bot + 1,
                            ob_bot,
                            ),
                        )

            if ores >= obs_cost[0] and clay >= obs_cost[1]:
                best = max(
                        best,
                        calculate_geodes(
                            time_left - 1,
                            new_ores - obs_cost[0],
                            new_clay - obs_cost[1],
                            new_obs,
                            o_bot,
                            c_bot,
                            ob_bot + 1,
                            ),
                        )

        if ores < max_ore_cost:
            best = max(
                    best,
                    calculate_geodes(
                        time_left - 1, new_ores, new_clay, new_obs, o_bot, c_bot, ob_bot
                        ),
                    )

        return best

    return calculate_geodes(time, 0, 0, 0, 1, 0, 0)


def part1(blueprints: List) -> int:
    levels = 0
    for (itx, blueprint) in enumerate(blueprints):
        geodes = calculate(blueprint, 24)
        levels += (itx + 1) * geodes
    return levels


def part2(blueprints: List) -> int:
    levels = 1
    for (_, blueprint) in enumerate(blueprints[0:3]):
        geodes = calculate(blueprint, 32)
        levels *= geodes
    return levels


#with open("test_input") as f:
with open("input") as f:
    blueprints = []
    for line in f:
        stub = line.split(":")[1].split(".")
        ore_cost = int(stub[0].strip().split(" ")[4])
        clay_cost = int(stub[1].strip().split(" ")[4])

        tmp = stub[2].strip().split(" ")
        obsidian_cost = (int(tmp[4]), int(tmp[7]))

        tmp = stub[3].strip().split(" ")
        geode_cost = (int(tmp[4]), int(tmp[7]))

        blueprints.append((ore_cost, clay_cost, obsidian_cost, geode_cost))

# part1
print(f"part1: {part1(blueprints)}")
# part2
print(f"part2: {part2(blueprints)}")
