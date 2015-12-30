from functools import reduce
import operator

sz, *cages = open("240H_input.txt").read().splitlines()
sz = int(sz)

name_to_coord = lambda name: ('ABCDEFGHI'.index(name[0]), int(name[1])-1)
cages = [
    (int(val), operator, [name_to_coord(coord) for coord in coords])
    for val, operator, *coords in map(str.split, cages)
]
cage_map = {
    coord: cage
    for cage in cages
    for coord in cage[2]
}

board = {
    coord: None for coord in cage_map
}
cell_list = list(sorted(board))

def check(cell, i):
    val, op, coords = cage_map[cell]
    vals = [board[coord] for coord in coords]
    if not all(vals):
        return True
    if op == "=":
        return i == val
    elif op == "+":
        return sum(vals) == val
    elif op == "*":
        return reduce(operator.mul, vals) == val
    elif op == "-":
        return abs(vals[0] - vals[1]) == val
    elif op == "/":
        bigger, smaller = max(vals), min(vals)
        return bigger % smaller == 0 and bigger // smaller == val

def recurse(depth=0):
    if depth == len(cell_list):
        return True
    cell = cell_list[depth]
    X, Y = cell
    used = {board[(x, Y)] for x in range(sz)} | {board[(X, y)] for y in range(sz)}
    for i in set(range(1, sz+1)) - used:
        board[cell] = i
        if not check(cell, i):
            continue
        if recurse(depth+1):
            return True
    board[cell] = None

print(cell_list)
recurse()

for y in range(sz):
    line = " ".join(str(board[(x, y)]) for x in range(sz))
    print(line)
