# Day 2 AOC 2022

# A = rock
# B = paper
# C = scissors

# X = rock
# Y = paper
# Z = scissors

#test_input = """A Y
# B X
# C Z
# """
# my_list = test_input.splitlines()

with open("input") as f:
    my_list = f.read().splitlines()

def bonus_for_choice(choice: str) -> int:
    if choice == "X":
        return 1
    elif choice == "Y":
        return 2
    elif choice == "Z":
        return 3
    return 0

def strategy_choice(player1: str, condition: str) -> str:
    if condition == "X": # lose
        if player1 == "A":
            return "Z"
        elif player1 == "B":
            return "X"
        elif player1 == "C":
            return "Y"
    elif condition == "Y": # draw
        if player1 == "A":
            return "X"
        elif player1 == "B":
            return "Y"
        elif player1 == "C":
            return "Z"
    elif condition == "Z": # win
        if player1 == "A":
            return "Y"
        elif player1 == "B":
            return "Z"
        elif player1 == "C":
            return "X"
    return "error"

def rps(player1: str, player2: str) -> int:
    total_points = 0
    if player1 == "A" and player2 == "X": # tie
        total_points += 3
    elif player1 == "A" and player2 == "Y":
        # win
        total_points += 6
    elif player1 == "A" and player2 == "Z":
        # lose no points
        pass
    if player1 == "B" and player2 == "Y": # tie
        total_points += 3
    elif player1 == "B" and player2 == "Z":
        # win
        total_points += 6
    elif player1 == "B" and player2 == "X":
        # lose no points
        pass
    if player1 == "C" and player2 == "Z": # tie
        total_points += 3
    elif player1 == "C" and player2 == "X":
        # win
        total_points += 6
    elif player1 == "C" and player2 == "Y":
        # lose no points
        pass
    total_points += bonus_for_choice(player2)
    return total_points

total_points_part1 = 0
total_points_part2 = 0
# we seem to be player2
for line in my_list:
    player1, player2 = line.split()
    total_points_part1 += rps(player1, player2)
    total_points_part2 += rps(player1, strategy_choice(player1, player2))

# part1
print(f"{total_points_part1=}")
# part2
print(f"{total_points_part2=}")
