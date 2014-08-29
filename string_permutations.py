import sys
import string


def load_file(fn):
    data = []
    with open(fn) as f:
        for line in f:
            data.append(line.strip())
    return data

def string_permutation(word):
    if len(word) == 1 : return [word]

    result = []
    l = list(word)
    for i in sorted(l):
        prev_permutation =  string_permutation(string.replace(word, i, ''))
        for j in prev_permutation :
            result.append(string.join([i, j], ""))
    return result

def string_permutations(data):
    for line in data:
        print ",".join(string_permutation(line))

if __name__ == "__main__":
    string_permutations(load_file(sys.argv[1]))
