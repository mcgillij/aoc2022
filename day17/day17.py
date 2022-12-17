# Day 17 AOC 2022

jets = [1 if l == '>' else -1 for l in open("input").read().strip()]
#jets = [1 if l == '>' else -1 for l in open("test_input").read().strip()]
CHAMBER = set([-1j,1-1j,2-1j,3-1j,4-1j,5-1j,6-1j])
highest = -1
piece_index = 4
jet_index = len(jets)-1
part1, part2 = 0, 0
history = dict()
LIMIT = 1_000_000_000_000

TETRIS_PIECES = [[2+0j,3+0j,4+0j,5+0j], # |
          [3+0j,2+1j,3+1j,4+1j,3+2j], # +
          [2+0j,3+0j,4+0j,4+1j,4+2j], # L
          [2+0j,2+1j,2+2j,2+3j], # -
          [2+0j,3+0j,2+1j,3+1j]] # block

for n in range(LIMIT):

    seen = (piece_index, jet_index)
    if seen in history:
        period = n - history[seen][0]
        if n % period == LIMIT % period:
            part2 = history[seen][1] + (highest + 1 - history[seen][1]) * (((LIMIT - n)//period) + 1)
            break
    else:
        history[seen] = n, highest + 1

    if n == 2022:
        part1 = highest + 1

    piece_index = 0 if piece_index == 4 else piece_index + 1
    piece = [x + (highest+4)*1j for x in TETRIS_PIECES[piece_index]]

    while True:
        jet_index = 0 if jet_index == len(jets)-1 else jet_index + 1
        jet = jets[jet_index]
        piece = [x+jet for x in piece]
        if any([(x.real < 0) or (x in CHAMBER) or (x.real > 6) for x in piece]):
            piece = [x-jet for x in piece]
        piece = [x-1j for x in piece]
        if any([x in CHAMBER for x in piece]):
            CHAMBER |= set([x+1j for x in piece])
            highest = max(highest, int(piece[-1].imag)+1)
            break

# part1
print(f"{part1=}")
# part2
print(f"{part2=}")
