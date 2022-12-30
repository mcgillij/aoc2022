# Day 25 AOC 2022

def s2i(sval) -> int:
    ival = 0
    power5 = 5**len(sval)
    for c in sval:
        power5 //= 5
        match c:
            case "1" | "2":
                ival += power5 * int(c)
            case "=":
                ival -= power5 * 2
            case "-":
                ival -= power5
    return ival

def i2s(ival: int) -> str:
    if ival == 0:
        return ""

    match ival % 5:
        case 0 | 1 | 2:
            return i2s(ival // 5) + str(ival % 5)
        case 3:
            return i2s( 1 + ival // 5) + "="
        case 4:
            return i2s( 1 + ival // 5) + "-"

requests = open("input").read().split()
#requests = open("test_input").read().split()
# part1
print(f"part1: {i2s(sum([s2i(r) for r in requests]))}")
