import sys


def load_file(fn):
    data = []
    with open(fn) as f:
        for line in f:
            data.append(line)
    return data


def rollercoaster(data):
    for line in data:
        result = []
        flag = 0
        for l in line.strip():
            if l in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                l = l.upper() if flag == 0 else l
                flag = 1 if flag == 0 else 0
            result.append(l)
        print "".join(result)


if __name__ == "__main__":
    rollercoaster(load_file(sys.argv[1]))
__author__ = 'dantoccatu'
