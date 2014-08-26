import sys

data_file = "multiples_of_a_number_data.txt"


def load_data(fn):
    data = []
    with open(fn) as f:
        for line in f:
            (x,n) = line.strip().split(',')
            data.append((x,n))
    return data

def find_mul_of_a_number(data):
    for x, n in data:
        m = int(n)
        while m < int(x) :
            m += int(n)
        print m




if __name__ == "__main__" :
    find_mul_of_a_number(load_data(sys.argv[1]))
    __author__ = 'dantoccatu'
