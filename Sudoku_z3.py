#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from z3 import *

X = [ [Int('x_%s_%s' % (x+1,y+1)) for y in range(9)] for x in range(9) ]

cells_r = [ And(X[x][y] >=1, X[x][y] <= 9) for y in range(9) for x in range(9) ]

rows_r = [ Distinct([ X[x][y] for y in range(9) ]) for x in range(9) ]

cols_r = [ Distinct([ X[x][y] for x in range(9) ]) for y in range(9) ]

squares_r = [ Distinct([ X[3*x+i][3*y+j] for i in range(3) for j in range(3)])
             for x in range(3) for y in range(3)]


sudoku_rules = cells_r + rows_r + cols_r + squares_r




if __name__ == "__main__":
    prob = open("Sudoku.txt").read().splitlines()
    for line in prob:
        print line
    prob = [ [ int(c) if c in "123456789" else 0 for c in line ] for line in prob ]
    prob_r = [ If( prob[x][y] == 0, True, X[x][y] == prob[x][y])
              for x in range(9) for y in range(9)]
    rules = sudoku_rules + prob_r
    s = Solver()
    s.add(rules)
    if s.check() == sat :
        m = s.model()
        r = [ [ m.evaluate(X[x][y]) for y in range(9) ]
              for x in range(9)]
        for x in range(9):
            print "".join([ str(r[x][y]) for y in range(9) ])
    else:
        print "Failed to solve"


