str = input()
complement = lambda c: 'ATCG'['TAGC'.find(c)]

print("".join(list(complement(t) for t in str)))
##print( (lambda c: 'ATCG'[TAGC.find(c)])(t) for t in str )
