#!/bin/python3

base = int(input())
number = int(input())


def find_sad_cycles(b, n):
    results = []
    next = n
    while True:
        next = sum(int(c)**base for c in str(next))
        if next in results:
            return results[results.index(next):]
        else :
            results.append(next)


ret = find_sad_cycles(base, number)
print(", ".join(str(i) for i in ret))
