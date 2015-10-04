#!/usr/bin/env python3
import sys

def binary_permutation_generator(nw):
    for i in range(2**(nw)):
        ret = map(int, list('{number:0{width}b}'.format(width=nw, number=i)))
        yield list(ret)

def is_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]: return False
    return True

def sort(network, array):
    for i in range(len(network)):
        w1, w2 = network[i]
        if array[w1] > array[w2]:
            array[w1], array[w2] = array[w2], array[w1]

def validate(network, nw):
    for array in binary_permutation_generator(nw):
        sort(network, array)

        if not is_sorted(array):
            print('Invalid network')
            return

    print('Valid network')

if __name__ == "__main__":
    file = open(sys.argv[1])
    network = []
    nw, nc = map(int, file.readline().rstrip('\n').split())
    for _ in range(nc):
        s = file.readline()
        network.append(tuple(map(int, s.rstrip('/n').split())))
    validate(network, nw)
