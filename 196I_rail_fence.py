import sys
from collections import deque
# from itertools import repeat
from itertools import cycle
from itertools import chain

def index_generator(noLines, length):
    index = cycle( chain(range(0, noLines-1), range(noLines-1, 0, -1)))
    for i in range(length):
        yield next(index)

def encrypt(noLines, text):
    zigzag = [ "" for i in range(noLines) ]
    queue = deque(text)
    for index in index_generator(noLines, len(text)):
        zigzag[index] += queue.popleft()
    print(''.join(zigzag))

def decrypt(noLines, text):
    zigzag = [ deque() for i in range(noLines) ]
    length = len(text)
    for index in index_generator(noLines, length):
        zigzag[index].append('?')
    for i in range(noLines):
        zigzag[i] = deque(text[:len(zigzag[i])])
        text = text[len(zigzag[i]):]
    print(''.join([ zigzag[index].popleft() for index in index_generator(noLines, length) ]))

if __name__ == "__main__":
    if sys.argv[1] == 'enc':
        encrypt(int(sys.argv[2]), sys.argv[3])
    elif sys.argv[1] == 'dec':
        decrypt(int(sys.argv[2]), sys.argv[3])
