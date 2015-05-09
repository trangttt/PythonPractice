keyboard = """\
qwertyuiop
asdfghjkl
^zxcvbnm ^
   #####\
""".splitlines()

text = input()

hands = [[], []]
total = 0



keys = [(key if key != '#' else ' ', x, y) for y, row in enumerate(keyboard) for x, key in enumerate(row) if key != ' ']
get_xy = lambda c: [(x, y) for key, x, y in keys if key == c]

dist = lambda hand, x, y: abs(hand[-1][0]-x) + abs(hand[-1][1]-y) if hand else 0

#def dist(hand, x, y):
#    return abs(hand[-1][0] - x ) + abs(hand[-1][1] - y ) if hand else 0

best_for_hands = lambda locations, hands: [min([(dist(hand, *loc), loc) for loc in locations], key=lambda x: x[0]) for hand in hands]

output = lambda c, hand, d: print('{:<6}: {:<5}, distance: {}'.format(c, ['left', 'right'][hand], d))

for c in text:
    if c.isupper():
        shifts = best_for_hands(get_xy('^'), hands)
        bests = best_for_hands(get_xy(c.lower()), hands)
        #print("SHIFT")
        #print(shifts)
        #print("CHARACTER")
        #print(bests)
        a, b = (0, 1) if shifts[0][0] + bests[1][0] <= shifts[1][0] + bests[0][0] else (1, 0)
        hands[a].append(shifts[a][1])
        hands[b].append(bests[b][1])
        total += shifts[a][0] + bests[b][0]
        output('Shift', a, shifts[a][0])
        output(c, b, bests[b][0])
    else:
        bests = best_for_hands(get_xy(c), hands)
        #print("CHARACTER")
        #print(bests)
        a = 0 if bests[0] <= bests[1] else 1
        hands[a].append(bests[a][1])
        total += bests[a][0]
        output(c if not c.isspace() else 'Space', a, bests[a][0])
    print(hands)
print('Total: ', total)