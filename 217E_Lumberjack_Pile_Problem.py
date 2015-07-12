#!/bin/python3
import sys

size, logs, *piles = [int(i) for i in open(sys.argv[1]).read().split()]


logs = int(logs)
min_pile = min(piles)
while logs > 0 :
    for index, pile in enumerate(piles):
        if pile == min_pile :
            piles[index] +=  1
            logs -= 1
        if logs == 0: break
    min_pile += 1

size = int(size)
for i in range(0, size * size, size):
    print(*piles[i:i+size])
