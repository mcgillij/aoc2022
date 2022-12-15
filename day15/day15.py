# Day 15 AOC 2022

data = [[sum(a*b for a, b in zip((int(p.split('=')[1])
                                 for p in s.split(',')), (1, 1j)))
       for s in line.split(':')]
       #for line in open("test_input").read().splitlines()]
       for line in open("input").read().splitlines()]

def distance(lh, rh):
    return int(abs((rh - lh).real) + abs((rh - lh).imag))

def scan(y):
    return sorted([(int(sensor.real-extra), int(sensor.real+extra))
                   for sensor, beacon in data
                   for extra in [(distance(sensor, beacon) - distance(sensor, sensor.real + y*1j))]
                   if extra >= 0])

def merge(E, act, v):
    if not E:
        return v
    left, right = E[0]
    result = act(left, right, v)
    for left, x in E[1:]:
        left = max(left, right+1)
        right = max(right, x)
        if (right >= left):
            result = act(left, right, result)
    return result

def part1():
    Y=2000000
    B = len(set(beacon.real for _, beacon in data if beacon.imag == Y))
    return int(merge(scan(Y), lambda left,right,v: v+right-left+1, 0) - B)

def part2():
    MINX,MINY,MAXX,MAXY=0,0,4000000,4000000
    for y in range (MINY, MAXY+1):
        act = lambda left, right, z: [right,
                                      z[1]+min(MAXX,right)-max(MINX, left)+1,
                                      z[2] if z[0]+2 != left else z[2] + [left-1]]
        z = merge(scan(y), act, [0, 0, []])
        if len(z[2]) == 1:
            return y + 4000000*z[2][0]

# part1
print (f"part1: {part1()}")
# part2
print (f"part2: {part2()}")
