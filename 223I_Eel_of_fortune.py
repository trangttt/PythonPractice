#!/bin/python3
import sys


for word in open(sys.argv[1]).read().splitlines():
    slang = "snond"
    if slang == "".join(c for c in word if c in slang):
        print(word)
