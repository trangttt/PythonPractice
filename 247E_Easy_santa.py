import random
import sys

if __name__ == "__main__":
    file = open(sys.argv[1])
    families = {}
    for index, line in enumerate(file.readlines()):
        families.update({name:index for name in line.strip().split()})

    names = list(families.keys())

    while True:
        random.shuffle(names)
        assigned = [ (a1, a2) for a1,a2 in zip(names[0:-1], names[1:]) ]
        if all( families[a1] != families[a2] for a1, a2 in assigned):
            break

    for a1, a2 in assigned:
        print(a1, '(', families[a1], ')',  '->', a2, '(', families[a2], ')')
