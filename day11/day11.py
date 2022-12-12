# Day 11 AOC 2022

from operator import add, mul, pow
from functools import reduce

def get_monkeys(f):
    for line in f:
        if line.startswith('  Starting items:'):
            items = tuple(map(int, line.split(':')[1].split(', ')))
            opstr, amount = next(f).replace('* old', '** 2').split()[-2:]
            op = {'+': add, '*': mul, '**': pow}[opstr], int(amount)
            throws = tuple(int(next(f).rsplit(' ', 1)[1]) for _ in range(3))
            yield items, op, throws

def business(monkeys, rounds, divisor):
    queues = [list(items) for items, _, _ in monkeys]
    inspects = [0] * len(monkeys)
    modulus = reduce(mul, (div for _, _, (div, _, _) in monkeys))
    for _ in range(rounds):
        for i, (_, (op, amount), (div, true, false)) in enumerate(monkeys):
            items = queues[i]
            for item in items:
                worry = op(item, amount) // divisor % modulus
                queues[false if worry % div else true].append(worry)
            inspects[i] += len(items)
            items.clear()
    return mul(*sorted(inspects)[-2:])

with open('input') as f:
#with open('test_input') as f:
    monkeys = list(get_monkeys(f))
    print(f"part1: {business(monkeys, 20, 3)}")
    print(f"part2: {business(monkeys, 10000, 1)}")
