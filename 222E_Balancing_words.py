#!/bin/python3

#words = input().splitlines()

words= ['CONSUBSTANTIATION','WRONGHEADED','UNINTELLIGIBILITY']

ALPHABET_INDEX = dict((c, i) for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ',1))

def balancing_word(word):
    #for pivot in range(len(word)):
    for pivot, cp in enumerate(word):
        lw = rw = 0
        for i, c in enumerate(word):
            if i < pivot : lw += (pivot-i) * ALPHABET_INDEX.get(c)
            if i > pivot : rw += (i-pivot) * ALPHABET_INDEX.get(c)
        if lw == rw : return print(word[:pivot], word[pivot], word[pivot+1:], '-', lw)
    return print(word, 'DOES NOT BALANCE')


for word in words: balancing_word(word)
