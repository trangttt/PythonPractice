import sys
import math


def square_spiral_c(s, x, y):
    center = int(s/2) + 1, int(s/2) + 1
    id = max(abs(x - center[0]), abs(y - center[1]))
    val = get_square(s, 2*(id-1)+1)
    return val.get((x,y))

def square_spiral_p(s, p):
    lb = int(math.sqrt(p))
    if lb%2 == 0: lb -= 1
    val = get_square(s, lb)
    new_val = {v :k for k, v in val.items()}
    return new_val.get(p)

def get_square(size, id):
    center = int(size/2)+1, int(size/2)+1
    rank =  int((id-1)/2)
    pos = (center[0] + rank + 1, center[1] + rank +1 )
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    result = {}
    value = (id)**2
    for dir in dirs:
        while True:
            next = (pos[0] + dir[0], pos[1] + dir[1])
            if max(abs(next[0] - center[0]), \
                   abs(next[1] - center[1])) != rank + 1:
                break
            else:
                pos = next
                value += 1
                result[pos] = value
    return result

if __name__ == "__main__":
    file = open(sys.argv[1])
    try :
        while True:
            size = int(file.readline().strip())
            p = file.readline().strip()
            if len(p.split()) > 1:
                x, y  = p.split()
                print(square_spiral_c(size, int(x), int(y)))
            else:
                pos = int(p)
                print(square_spiral_p(size, int(p)))
    except IOError:
        print("end of file")

