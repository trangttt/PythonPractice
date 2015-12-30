#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

sz, *lines = open(sys.argv[1]).read().splitlines()
col, row = map(int, sz.split())

name_to_coord = lambda name: (int(name[1])-1, "ABCDEFGHIJ".index(name[0]))
rules = [ (int(val), [name_to_coord(coord) for coord in coords])
            for val, *coords in map(str.split, lines)]

rules_map = defaultdict(list)
for rule in rules:
    for coord in rule[1]:
        rules_map[coord].append(rule)

board = { (x,y): None for x in range(row) for y in range(col) }
cell_list = list(sorted(board))

def check(cell, i):
    rules = rules_map.get(cell, None)
    if not rules:
        return True
    result= []
    for rule in rules:
        val, coords = rule
        vals = [ board[coord] for coord in coords ]
        if not all(vals):
            result.append(True)
        else :
            result.append(sum(vals) == val)
    return all(result)

def recurse(depth=0):
    if depth == len(cell_list):
        return True

    cell = cell_list[depth]
    X, Y = cell
    used = { board[(X,y)] for y in range(col) } | { board[(x,Y)] for x in range(row) }
    for i in set(range(1, 9+1)) - used:
        board[cell] = i
        if not check(cell, i):
            continue
        if recurse(depth+1):
            return True
    board[cell] = None

recurse()

print(" ".join(" ABCDEFGHIJ"[:col+1]))
for i in range(row):
    print(i+1, " ".join([ str(board[(i,y)]) for y in range(col) ]))
