#!/bin/python3
import re

sentence = input()

def mangle_word(w):
    sorted_w = sorted(re.sub(r'[^A-Za-z]', '', w.lower()))
    ret = []
    for c in w:
        if c.isalnum():
            if c.isupper(): ret.append(sorted_w.pop(0).upper())
            else: ret.append(sorted_w.pop(0))
        else: ret.append(c)
    return "".join(ret)



result = [mangle_word(w) for w in sentence.split()]
print(" ".join(result))
