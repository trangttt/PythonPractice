import sys

data_file = 'reverse_words_data.txt'


def reverse(string):
    return string[::-1]

def load_file(file):
    lines = []
    with open(file) as f:
        for line in f:
            words = line.strip().split()
            lines.append(words)
    return lines

@profile
def reverse_words(data):
    for line in data:
        result = []
        for words in reversed(line) :
            result.append(words)
        print(" ".join(result))

if __name__ == "__main__" :
    reverse_words(load_file(sys.argv[1]))


