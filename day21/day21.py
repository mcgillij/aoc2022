# Day 21 AOC 2022

import operator
from typing import Callable

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}

REVOPS = {
    operator.add: operator.sub,
    operator.sub: operator.add,
    operator.mul: operator.floordiv,
    operator.floordiv: operator.mul,
}

REVOPS2 = {
    operator.add: operator.sub,
    operator.sub: (lambda q, a: a - q),
    operator.mul: operator.floordiv,
    operator.floordiv: (lambda q, a: a // q),
}


def get_monkeys(data: list[str]) -> dict[str, int | tuple[Callable, str, str]]:
    monkeys = {}
    for line in data:
        if not line:
            continue
        monkey, _, value = line.partition(": ")
        if value.isdigit():
            monkeys[monkey] = int(value)
        else:
            ma, op, mb = tuple(value.split())
            monkeys[monkey] = (OPERATORS[op], ma, mb)
    return monkeys


def part1(data: list[str]) -> int:
    monkeys = get_monkeys(data)
    done = {m: v for m, v in monkeys.items() if isinstance(v, int)}
    queue = {m: v for m, v in monkeys.items() if not isinstance(v, int)}

    while "root" not in done and queue:
        for q in list(queue):
            op, a, b = queue[q]
            if a in done and b in done:
                done[q] = op(done[a], done[b])
                del queue[q]

    return done["root"]


def part2(data: list[str]) -> int:
    monkeys = get_monkeys(data)
    del monkeys["humn"]
    done = {m: v for m, v in monkeys.items() if isinstance(v, int)}
    queue = {m: v for m, v in monkeys.items() if not isinstance(v, int)}
    computed = done.keys()
    _, roota, rootb = queue.pop("root")

    while roota not in done and rootb not in done:
        for q in list(queue):
            op, a, b = queue[q]
            if {a, b} < computed:
                done[q] = op(done[a], done[b])
                del queue[q]

    if roota in done:
        done["root"] = done[rootb] = done[roota]
    else:
        done["root"] = done[roota] = done[rootb]

    while "humn" not in done:
        for q in list(queue):
            op, a, b = queue[q]
            if {a, b} <= computed:
                done[q] = op(done[a], done[b])
                del queue[q]
            elif {q, b} <= computed:
                done[a] = REVOPS[op](done[q], done[b])
                del queue[q]
            elif {q, a} <= computed:
                done[b] = REVOPS2[op](done[q], done[a])
                del queue[q]

    return done["humn"]

#with open("test_input") as f:
with open("input") as f:
    data = f.read().splitlines()

# part1
print(f"part1: {part1(data)}")
# part2
print(f"part2: {part2(data)}")
