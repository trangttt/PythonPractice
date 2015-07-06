
import sys

input_prob = open(sys.argv[1]).read()




rows = 'ABCDEFGHI'
cols = '123456789'


cross = lambda A, B: [ a + b for a in A for b in B]

cells = cross(rows, cols)

unitlist = [ cross([ x for x in rows], [i]) for i in cols ] + [ cross([x],[ i for i in cols] ) for x in rows ] + \
            [cross(x,y) for x in ['ABC', 'DEF', 'GHI'] for y in ['123', '456', '789']]

units = dict( [(c, [ u for u in unitlist if c in u]) for c in cells] )

peers = dict( (c1, list(set([ c2 for unit in units[c1] for c2 in unit ]) - set([c1]) )) for c1 in cells)



def test_data():
    print("{:<6}".format("Testing..........."))
    assert len(cells) == 81
    assert len(unitlist) == 27
    assert all( len(units[c]) == 3 for c in cells )
    assert all( len(peers[c]) == 20 for c in cells )


    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert set(peers['C2']) == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])

    print("%6s" % "All tests pass.")






parse_prob = lambda ls: dict( ('ABCDEFGHI'[r]+ str(c), cell) for r, l in enumerate(ls) for c, cell in enumerate(l,1))

display_prob = lambda pr: "\n".join( [  "".join( [ ( pr[r + c].center(1+max(len(pr[c]) for c in pr)) + ('|' if c in '36' else '') ) for c in cols ]) + ( '\n------+------+------' if r in 'CF' else '' )  for r in rows])

sum_unit = lambda u, prob: sum( prob[c] for c in u )


def update_pos_vals(pos_vals, val, cell):
    if not pos_vals: return False
    if val not in pos_vals[cell]: return False

    new_pos_vals = dict(pos_vals)
    new_pos_vals[cell] = val
    new_pos_vals = propagate_values(new_pos_vals, val, cell)
    return new_pos_vals



def propagate_values(pos_vals, val, cell):
    if not pos_vals: return False

    new_pos_vals = dict(pos_vals)
    for i in peers[cell] :
        new_pos_vals[i] = new_pos_vals[i].replace(val, '')

    for i in peers[cell]:
        if len(new_pos_vals[i]) == 0:
            return False
        elif (new_pos_vals[i] != pos_vals[i]) and len(new_pos_vals[i]) == 1:
            new_pos_vals = propagate_values(new_pos_vals, new_pos_vals[i], i)
            if not new_pos_vals: return False

    for u in unitlist:
        filled = [ new_pos_vals[c][0] for c in u if len(new_pos_vals[c]) == 1  ]
        if len(filled) == 8 :
            not_fill_digit = list(set('12345678') - set(filled))
            if len(not_fill_digit) != 1 : return False
            else :
                not_fill_cell = [c for c in u if not_fill_digit[0] in new_pos_vals[c]]
                if len(not_fill_cell) != 1 : return False
                else :
                    new_pos_vals = update_pos_vals(new_pos_vals, not_fill_digit[0], not_fill_cell[0])
                    if not new_pos_vals: return False

    return new_pos_vals


def check_unit(pos_vals):
    print('Checking possible answer......'.ljust(30,'.'))
    for u in unitlist:
        if set([ pos_vals[c] for c in u]) != set('123456789') :
            print('Answer is INCORRECT')
            print(u)
            print([pos_vals[c] for c in u])
            return False
    print ('Answer is CORRECT')
    return True

def parse_pos_vals(prob):
    pos_vals = dict((c, '123456789') for c in cells)
    for i in prob:
        if prob[i] not in '0.' :
            pos_vals = update_pos_vals(pos_vals, prob[i], i)
    return pos_vals

def solve(pos_vals) :
    result = search(pos_vals)
    if result and check_unit(result):
        print('Result is :')
        print(display_prob(result))
    else :
        print('No possible answer.')


def search(pos_vals):
    if not pos_vals : return False
    elif all(len(pos_vals[c]) == 1 for c in cells) : return pos_vals
    else :
        min_pos =  min([(c, len(pos_vals[c])) for c in cells if len(pos_vals[c]) > 1], key=lambda x: x[1])[0]
        for i in pos_vals[min_pos] :
            new_pos_vals = dict(pos_vals)
            new_pos_vals = update_pos_vals(new_pos_vals, i, min_pos)
            if not new_pos_vals : continue
            else :
                new_pos_vals = search(new_pos_vals)
                if not new_pos_vals : continue
                else : return new_pos_vals

    return False

hard1 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
hard2  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'

hard_coded = hard1

test_data()
NUM_CHAR=9
#from file
#lines = input_prob.splitlines()
#hard coded
lines=[hard_coded[i*NUM_CHAR:(i+1)*NUM_CHAR] for i in range(int(81/NUM_CHAR))]



print("\n".join(lines),'\n')
print('Problem :')
print(display_prob(parse_prob(lines)),'\n')
print('Solving.......'.ljust(30,'.'))
pos_vals = parse_pos_vals(parse_prob(lines))
solve(pos_vals)



