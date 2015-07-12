#!/bin/python3

from collections import defaultdict
import sys

wh, player, *board = open(sys.argv[1]).read().splitlines()
w, h = map(int, wh.split())

enemy = "b" if player == "w" else "w"

visited = set()

def fill(start_x, start_y):
    group, liberties = set(), set()
    to_visit = {(start_x, start_y)}
    while to_visit:
        x, y = to_visit.pop()
        group.add((x, y))
        visited.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if board[ny][nx] == enemy and (nx, ny) not in group:
                to_visit.add((nx, ny))
            elif board[ny][nx] == ' ':
                liberties.add((nx, ny))
    return group, liberties

all_liberties = defaultdict(int)

for y, row in enumerate(board):
    for x, cell in enumerate(row):
        if cell == enemy and (x, y) not in visited:
            group, liberties = fill(x, y)
            if len(liberties) == 1:
                all_liberties[liberties.pop()] += len(group)

if not all_liberties:
    print("No move resulting in immediate removal")
else:
    best_liberty, max_size = max(all_liberties.items(), key=lambda kv: kv[1])
    print("Placing stone in {} will result in removing {} stones".format(best_liberty, max_size))
