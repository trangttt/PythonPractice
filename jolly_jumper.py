import sys

def load_file(fn):
    data = []
    with open(fn) as f:
        for line in f:
            data.append(line.strip().split())
    return data

def jolly_jumper(data):
    for line in data:
        n = int(line[0])
        seq = line[1:]
        tok = range(1, n)
        for i, j in zip(seq[:n-1], seq[1:]):
            try :
                t = abs(int(i) - int(j))
                tok.remove(t)
            except ValueError:
                break
        if not tok : print 'Jolly'
        else : print 'Not jolly'


if __name__ == "__main__" :
    jolly_jumper(load_file(sys.argv[1]))
