# Day 22 AOC 2022

def firstcol_fromleft(r):
    for c in range(WIDTH):
        if grid[r][c] != ' ':
            return c

def firstcol_fromright(r):
    for c in range(WIDTH - 1, -1, -1):
        if grid[r][c] != ' ':
            return c

def firstrow_fromtop(c):
    for r in range(HEIGHT):
        if grid[r][c] != ' ':
            return r

def firstrow_frombottom(c):
    for r in range(HEIGHT - 1, -1, -1):
        if grid[r][c] != ' ':
            return r

def face(r, c):
    if r <= 50:
        if c <= 100:
            return 1, r, c - 50
        else:
            return 2, r, c - 100
    elif r <= 100:
        if c <= 100:
            return 3, r - 50, c - 50
    elif r <= 150:
        if c <= 50:
            return 4, r - 100, c
        elif c <= 100:
            return 5, r - 100, c - 50
    else:
        if c <= 50:
            return 6, r - 150, c

def wrap(r, c, direction):
    f, fr, fc = face(r, c)

    if f == 1:
        if direction == UP: # -> face 6 going right
            res = fc + 150, 1, RIGHT
        elif direction == LEFT: # -> face 4 going right
            res = (51 - fr) + 100, 1, RIGHT
    elif f == 2:
        if direction == UP: # -> face 6 up
            res = 200, fc, UP
        elif direction == DOWN: # -> face 3 left
            res = fc + 50, 100, LEFT
        elif direction == RIGHT: # -> face 5 left
            res = (51 - fr) + 100, 100, LEFT
    elif f == 3:
        if direction == LEFT: # -> face 4 down
            res = 101, fr, DOWN
        elif direction == RIGHT: # -> face 2 up
            res = 50, fr + 100, UP
    elif f == 4:
        if direction == UP: # -> face 3 right
            res = fc + 50, 51, RIGHT
        elif direction == LEFT: # -> face 1 right
            res = (51 - fr), 51, RIGHT
    elif f == 5:
        if direction == RIGHT: # -> face 2 left
            res = (51 - fr), 150, LEFT
        elif direction == DOWN: # -> face 6 left
            res = fc + 150, 50, LEFT
    else:
        if direction == LEFT: # -> face 1 down
            res = 1, fr + 50, DOWN
        elif direction == RIGHT: # -> face 5 up
            res = 150, fr + 50, UP
        elif direction == DOWN: # -> face 2 down
            res = 1, fc + 100, DOWN

    f, fr, fc = face(res[0], res[1])
    return res


with open("input") as f:
#with open("test_input") as f:
    grid = []

    for line in f:
        line = line.rstrip('\n')
        if not line:
            break

        grid.append(line)


    WIDTH = max(map(len, grid))
    HEIGHT = len(grid)

    for i in range(len(grid)):
        grid[i] = list(' ' + grid[i].ljust(WIDTH, ' ') + ' ')

    WIDTH += 2
    HEIGHT += 2
    grid = [list(' ' * WIDTH)] + grid + [list(' ' * WIDTH)]

    moves = f.readline().strip()
    moves = moves.replace('R', ' R ').replace('L', ' L ').split()
    R, C = 1, grid[1].index('.')
    direction = 0

    RIGHT, DOWN, LEFT, UP = range(4)
    DIRMAP = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            ]

    RDLU = 'RDLU'

    for i, move in enumerate(moves):
        if i % 2 == 0:
            n = int(move)
            dr, dc = DIRMAP[direction]

            for _ in range(n):
                newr = R + dr
                newc = C + dc

                if grid[newr][newc] == ' ':
                    if direction == RIGHT:
                        newc = firstcol_fromleft(newr)
                    elif direction == LEFT:
                        newc = firstcol_fromright(newr)
                    elif direction == DOWN:
                        newr = firstrow_fromtop(newc)
                    elif direction == UP:
                        newr = firstrow_frombottom(newc)

                if grid[newr][newc] == '#':
                    break

                R, C = newr, newc
        else:
            if move == 'R':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
    #part1
    print(f"part1: {1000 * R + 4 * C + direction}")


    R, C = 1, grid[1].index('.')
    direction = 0

    for i, move in enumerate(moves):
        if i % 2 == 0:
            n = int(move)

            for _ in range(n):
                dr, dc = DIRMAP[direction]
                newr = R + dr
                newc = C + dc
                newd = direction

                if grid[newr][newc] == ' ':
                    newr, newc, newd = wrap(R, C, direction)

                if grid[newr][newc] == '#':
                    break

                R, C, direction = newr, newc, newd

        else:
            if move == 'R':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
    # part2
    print(f"part2: {1000 * R + 4 * C + direction}")
