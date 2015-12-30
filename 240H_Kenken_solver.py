from functools import reduce
import operator
import sys

sz, *rules = open(sys.argv[1]).read().splitlines()
sz = int(sz)

name_to_coord = lambda name: ("ABCDEFGHIJK".index(name[0]), int(name[1])-1)
rules = [ (int(val), op, [name_to_coord(coord) for coord in coords])
         for val, op, *coords in map(str.split, rules)]

rules_map = {
    coord: rule
    for rule in rules
    for coord in rule[2]
}

board = { (x,y): None for x in range(sz) for y in range(sz) }
cell_list = list(sorted(board.keys()))

def check(cell, i):
    val, op, coords = rules_map[cell]
    vals = [ board[coord] for coord in coords ]
    if not all(vals):
        return True
    elif op == "=":
        return val == i
    elif op == "+":
        return sum(vals) == val
    elif op == "*":
        return reduce(operator.mul, vals) == val
    elif op == "-":
        return abs(vals[1] - vals[0]) == val
    elif op == "/":
        bigger, smaller = max(vals), min(vals)
        return bigger // smaller == val and bigger % smaller == 0

def recurse(depth=0):
    if depth == len(cell_list):
        return True
    cell = cell_list[depth]
    X, Y = cell
    used = { board[(X,y)] for y in range(sz) } | { board[(x,Y)] for x in range(sz) }
    for i in set(range(1, sz+1)) - used:
        board[cell] = i
        if not check(cell, i):
            continue
        if recurse(depth+1):
            return True
    board[cell] = None

recurse()

for y in range(sz):
    print( " ".join( [ str(board[x,y]) for x in range(sz) ] ) )
