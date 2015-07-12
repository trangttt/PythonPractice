#!/bin/python3
import sys

messages = open(sys.argv[1]).read().splitlines()

planets = ["Omicron", "Hoth", "Ryza", "Htrae"]

rate_text = lambda text: sum(c.isalpha() or c.isspace() for c in text)

for mes in messages:
    chars = mes.strip('\"').split()
    results = [
        "".join(chr(int(c) ^ 0b10000) for c in chars),
        "".join(chr(int(c) - 10) for c in chars),
        "".join(chr(int(c) + 1) for c in chars),
        "".join(chr(int(c)) for c in reversed(chars))
        ]
    best = max(results, key = rate_text)
    planet = planets[results.index(best)]
    print("{:>7} | {}".format(planet, best))
