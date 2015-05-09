



digits = 'ABCDEFGHI'
rows = '123456789'

cross = lambda A, B: [ a + b for a in A for b in B]

squares = cross(digits, rows)

unitlist = [ cross([ x for x in digits], [i]) for i in rows ] + [ cross([x],[ i for i in rows] ) for x in digits ] + \
            [ cross(x,y) for x in ['ABC', 'DEF', 'GHI'] for y in [ '123', '456', '789'] ]


for i in unitlist :
    print(i)
