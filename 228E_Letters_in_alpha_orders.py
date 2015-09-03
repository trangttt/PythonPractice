import sys

def is_in_order(word):
    prev = 0
    for i, w in enumerate(word[1:]):
        if ord(word[prev]) > ord(w): return word + " NOT IN ORDER"
        prev = i
    return word + " IN ORDER"

if __name__ == "__main__":
    file = open(sys.argv[1])
    for line in file.readlines():
        print(is_in_order(line.rstrip('\n')))
