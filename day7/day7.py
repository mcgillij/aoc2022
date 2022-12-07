# Day 7 AOC 2022

# test_input = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# """

# lines = [x.strip().split() for x in test_input.splitlines()]

with open("input") as f:
    lines = [x.strip().split() for x in f]

root = {".name": "/", ".type": "d"}
cwd = None
path = []

max_size = 100_000
available_space = 70_000_000
minimum_space = 30_000_000

for chunk in lines:
    if chunk[0] == "$":
        if chunk[1] == "cd":
            if   chunk[2] == "/":  cwd = root
            elif chunk[2] == "..": cwd = path.pop() 
            else:
                path.append(cwd); cwd = cwd[chunk[2]]
    elif chunk[0] == "dir":
        cwd[chunk[1]] = {".name": chunk[1], ".type": "d"}
    else:
        cwd[chunk[1]] = {".name": chunk[1], ".type": "f", ".size": int(chunk[0])}

def get_size(n):
    if n[".type"] == "f":
        return n[".size"]
    return sum(get_size(v) for k, v in n.items() if not k.startswith("."))

def get_file_sizes(cwd, file_sizes):
    file_sizes.append(get_size(cwd))
    for k, v in cwd.items():
        if not k.startswith(".") and v[".type"] == "d":
            get_file_sizes(v, file_sizes)

file_sizes = []
get_file_sizes(root, file_sizes)
# part1
print(sum([s for s in file_sizes if s < max_size]))

# part2
size_free = available_space - file_sizes[0]
for d in sorted(file_sizes):
    if size_free + d >= minimum_space:
        print(d)
        break
