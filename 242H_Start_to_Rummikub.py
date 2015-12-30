import sys
import itertools
import operator
import random

from collections import namedtuple

Tile = namedtuple("Tile", ["col", "num"])

def find_groups(tiles):
    tiles = sorted(tiles, key=lambda x: x.num)
    result = [ list(g) for k,g in itertools.groupby(tiles, key=lambda x: x.num)]
    result = itertools.filterfalse(lambda x: len(x)<3, result)
    return list(result)


def find_runs(tiles):
    tiles = sorted(tiles, key=lambda x: x.col)
    cols = [ sorted(g, key=lambda x: x.num) for k, g in itertools.groupby( tiles, lambda x: x.col )]
    runs = [ list(map(operator.itemgetter(1), g))
                 for col in cols
                 for k, g in itertools.groupby(enumerate(col), lambda x: x[0]-x[1].num)]
    runs = itertools.filterfalse(lambda x: len(x)<3, runs)
    return list(runs)

def is_overlapped(l1, l2):
    return len(set(l1) & set(l2)) > 0

def sum_num(l1, l2):
    return sum(map(operator.itemgetter(1), l1+l2))

def find_start(mixed):
    for l1, l2 in itertools.combinations(mixed, 2):
        if not is_overlapped(l1, l2) and sum_num(l1, l2) > 30:
            return (l1, l2)
    return None

if __name__ == "__main__":
    tiles = sys.argv[1:]
    tiles = [ Tile(tile[0], int(tile[1:])) for tile in tiles ]
    groups = find_groups(tiles)
    runs = find_runs(tiles)
    mixed = groups + runs
    start = find_start(mixed)
    if start:
        l1, l2 = start
        print(" ".join(list(map(lambda x: x.col+str(x.num), l1))))
        print(" ".join(list(map(lambda x: x.col+str(x.num), l2))))
    else :
        BAGS = [ Tile(name, num) for name in "BYRP" for num in range(1,13) ]
        used = set(tiles)

        print("Grabbed:")
        while not start:
            left = set(BAGS) - used
            picked = random.choice(list(left))
            print("\t", picked.col + str(picked.num))
            used.add(picked)
            tiles = list(used)
            mixed = find_groups(tiles) + find_runs(tiles)
            start = find_start(mixed)
            if start:
                l1, l2 = start
                print("\n\nFound set:")
                print("\t", " ".join(list(map(lambda x: x.col+str(x.num), l1))))
                print("\t", " ".join(list(map(lambda x: x.col+str(x.num), l2))))
            else :
                continue
