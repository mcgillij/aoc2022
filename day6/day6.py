# Day 6 AOC 2022

# test_input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
# bvwbjplbgvbhsrlpgdmjqwftvncz
# nppdvjthqldpwncqszvftbrmjlhg
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
# """

#data = test_input.splitlines()

with open("input") as f:
    data = f.read()

def detect_message(data, size):
    for (i, _) in enumerate(data):
        if len(set(data[i:(i+size)])) == size:
            return i + size

# test data
#for d in data:
#    print(f"{d=}: {detect_message(d, 4)}")
#    print(f"{d=}: {detect_message(d, 14)}")

# part1
print(f"part1: {detect_message(data, 4)}")
# part2
print(f"part2: {detect_message(data, 14)}")
