#!/usr/bin/env python3

HW, *data = open('237I_input2.txt').read().splitlines()
H, W = [int(i) for i in HW.split(' ')]
data = { (x,y): c for y, line in enumerate(data) for x, c in enumerate(list(line)) }

depth_fill = { 0: '#', 1: '=', 2: '-', 3: '.' , 4 : ' '}

def fill(start=(0,0), depth=0):
    to_visit = [(start[0]+1, start[1]+1)]
    visited = set()
    while to_visit:
        cur = to_visit.pop()
        if cur in data and cur not in visited and data[cur] not in '+|-':
            data[cur] = depth_fill[depth]
            visited.add(cur)
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                to_visit.append((cur[0] + x, cur[1] + y))
        elif cur not in data :
            continue
        elif data[cur] == '+' and data[(cur[0]+1, cur[1])] == '-' and \
                        data[(cur[0], cur[1]+1)] == '|' :
            fill(cur, depth=depth+1)

fill()
print("\n".join(["".join([data[(x,y)] for x in range(W)]) for y in range(H)]))
