#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from z3 import *
from functools import reduce
import operator
import sys


name_to_coord = lambda name: ( "ABCDEFGHIJ".index(name[0]), int(name[1])-1 )

def process_rule(rules):
    result = []
    for val, op, coords in rules:
        vals = [ X[i][j] for i, j in coords ]
        if op == "=":
            result.append( vals[0] == val )
        if op == "+" :
            result.append(Sum(vals) == val)
        if op == "*" :
            result.append( reduce(operator.mul, vals) == val )
        if op == "-" :
            result.append(Or(vals[0] - vals[1] == val, vals[1] - vals[0] == val))
        if op == "/" :
            result.append(Or(vals[0]/vals[1] == val, vals[1]/vals[0] == val))
    return result


if __name__ == "__main__":
    lines = open(sys.argv[1]).read().splitlines()
    sz, rules = int(lines[0]), lines[1:]

    X = [ [ Int("x_%s_%s" % (i,j)) for j in range(sz) ] for i in range(sz) ]
    rules_raw = []
    for rule in rules:
        items = rule.split()
        val, op, coords = int(items[0]), items[1], items[2:]
        rules_raw.append((val, op, [name_to_coord(coord) for coord in coords]))

    cells_r = [ And(X[i][j] >=1, X[i][j] <= sz)  for i in range(sz)
               for j in range(sz)]

    rows_r = [ Distinct([ X[i][j] for i in range(sz) ]) for j in range(sz)]
    cols_r = [ Distinct([ X[i][j] for j in range(sz) ]) for i in range(sz)]

    rules_r = process_rule(rules_raw)
    # rules_r = []

    s = Solver()
    rules = cells_r + rows_r + cols_r + rules_r
    s.add(rules)
    # print s
    if s.check() == sat :
        ans = s.model()
        for j in range(sz):
            print " ".join([ str(ans[X[i][j]]) for i in range(sz)])
    else :
        print "Not satisfiable"
