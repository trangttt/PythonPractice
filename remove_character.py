import sys
import re

def load_file(fn):
    data = []
    with open(fn) as f:
        for line in f:
            data.append(line.strip().split(', '))
    return data


def remove_character(data):
    for line in data:
        # solution 1
        # print re.sub('[' + line[1] + ']', '', line[0])
        # solution 2
        print line[0].translate(None, line[1])

if __name__ == "__main__" :
    remove_character(load_file(sys.argv[1]))

__author__ = 'dantoccatu'
