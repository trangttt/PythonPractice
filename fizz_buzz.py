
import sys

def load_file(fn):
    data = []
    with open(fn) as f:
        for line in f:
            (a, b, n) = line.strip().split()
            data.append((int(a), int(b), int(n)))
    return data

def fizz_buzz(data):
    for a, b, n in data :
        result = []
        for i in range(1, n + 1 ) :
            if (i % a) == 0 and (i %b == 0) :
                result.append('FB')
            elif i % a == 0:
                result.append('F')
            elif i % b == 0:
                result.append('B')
            else : result.append(str(i))
        print " ".join(result)


if __name__ == "__main__" :
    fizz_buzz(load_file(sys.argv[1]))
