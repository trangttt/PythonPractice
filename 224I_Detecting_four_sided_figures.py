#!/usr/bin/python3
import sys


data = open(sys.argv[1]).read().splitlines()
W, H = max(len(row) for row in data), len(data)
chart = [[c for c in row.ljust(W)] for row in data]

for i in range(H):
    for j in range(W):
        print(chart[i][j], end="")
    print("")

def is_connected(ls, l, r):
    for i in range(l+1, r):
        if ls[i] == " " : return False
    return True

def get_lr(ls):
    for l in range(len(ls)):
        for r in range(l+1, len(ls)):
            if ls[l] == ls[r] == '+' and is_connected(ls,l,r) :
                yield (l, r)

ret = 0
for t in range(H):
    for l, r in get_lr(chart[t]):
        for b in range(t+1, H):
            if chart[b][l] == chart[b][r] == '+' \
                    and is_connected([chart[i][l] for i in range(H)], t, b) \
                    and is_connected([chart[i][r] for i in range(H)], t, b) \
                    and is_connected(chart[b], l, r):
                ret += 1
                print(ret, t, b, l, r)



