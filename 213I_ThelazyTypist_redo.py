keyboard = """\
qwertyuiop
asdfghjkl
^zxcvbnm ^
   #####\
""".splitlines()


text = input()

hands = [[],[]]

keys = [ (key if key != '#' else ' ', x, y) for y, row in enumerate(keyboard) for x, key in enumerate(row) if key != " "]


dist = lambda hand, x, y: abs(hand[0] - x) + abs( hand[1] - y) if hand else 0
get_xy = lambda c: [(x,y) for key, x, y in keys if key == c]
min_dist = lambda locations, hands: [min([(dist(hand, *loc), loc) for loc in locations], key=lambda x: x[0]) for hand in hands]


output = lambda key, hand, effort, pc: print("{:<6}: {} {:<5} hand from {} (effort: {})".format( \
    key, ["Use","Move"][1 if pc else 0],["left","right"][hand], pc, effort ))

total = 0
prev_char = None
for c in text:
    if c.isupper():
        shifts = min_dist(get_xy('^'), hands)
        chars = min_dist(get_xy(c.lower()), hands)
        (a,b) = (0,1) if shifts[0][0] + chars[1][0] <= shifts[1][0] + chars[0][0] else (1,0)
        hands[a] = list(shifts[a][1])
        hands[b] = list(chars[b][1])
        output("SHIFT", a, shifts[a][0], prev_char)
        output(c, b, chars[b][0], prev_char)
        total += shifts[a][0] + chars[b][0]
    else :
        chars = min_dist(get_xy(c), hands)
        pos = 0 if chars[0][0] <= chars[1][0] else 1
        hands[pos] = list(chars[pos][1])
        total += chars[pos][0]
        output("Space" if c is " " else c, pos, chars[pos][0], prev_char)
    prev_char = "Space" if c is " " else c

print("Total : %d" % total )
