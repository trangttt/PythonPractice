import sys
import z3

file = open(sys.argv[1])
col, row = map(int, file.readline().strip().split())

lines = file.read().splitlines()

rules = []
for line in lines:
    rule = line.split()
    val, coords = int(rule[0]), rule[1:]
    name_to_coord = lambda name: ("ABCDEFGHIJ".index(name[0]), int(name[1])-1)
    rules.append((val, [ name_to_coord(coord) for coord in coords ]))


X = { (c,r): z3.Int("x_%s_%s" % (c,r)) for c in range(col) for r in range(row)}

cells_r = [ z3.And(1<= X[x], X[x]<=9) for x in X ]

rows_r = [ z3.Distinct([X[(c,r)] for c in range(col)]) for r in range(row)  ]

cols_r = [ z3.Distinct([X[(c,r)] for r in range(row)]) for c in range(col) ]

rules_r = [ sum(X[coord] for coord in coords) == val for val, coords in rules ]

s = z3.Solver()
s.add(cells_r + rows_r + cols_r + rules_r)
if s.check() == z3.sat:
    ans = s.model()
    print " ".join(" ABCDEFGH"[:col+1])
    for r in range(row):
        print r+1, " ".join([ str(ans[X[(c,r)]]) for c in range(col) ])



