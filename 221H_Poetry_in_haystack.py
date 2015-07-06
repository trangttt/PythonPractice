#!/bin/python3
import re

word_list = set(open("wordlist.txt").read().splitlines())

haystack = open("221H_challenge.txt").read().splitlines()

for line in haystack:
    count = 0
    for word in line.split():
        if re.sub(r'\W+','',word) not in word_list: count += 1
        if count > 3 :
            break
    if count < 4 : print(line)


###################################################
##LEARNED LESSON: line 11: check whether an element in set is much faster than an element in list
