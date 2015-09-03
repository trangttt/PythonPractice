import sys
import math



def square_spiral_p(size, pos):
    center = (int(size/2) + 1, int(size/2) + 1)

    lb     = int(math.sqrt(pos))
    if lb %2  == 0: lb = lb -1
    id        = int((lb+3)/2)

    val       = (2*id - 3)**2
    dirs      = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    start     = (center[0] + id -1, center[1] + id -1)
    max_steps = 2 * (id - 1)

    for index, dir in enumerate(dirs, start=1):
        if val + (index -1)*max_steps < pos <= val + (index)*max_steps:
            diff = pos - val - (index-1)*max_steps
            return (start[0] + diff * dir[0], start[1] + diff * dir[1])
        else:
            start = (start[0] + max_steps * dir[0], start[1] + max_steps * dir[1])


def square_spiral_c(size, coor):
    center    = (int(size/2) + 1, int(size/2) + 1)
    id        = max(abs(coor[0] - center[0]), abs(coor[1] - center[1])) + 1
    dirs      = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    start     = (center[0] + id - 1, center[1] + id - 1 )
    max_steps = 2 * (id - 1)
    val       = (2*id -3)**2

    dir_x = int((coor[0] - center[0])/abs(coor[0] - center[0])) \
        if abs(coor[0] - center[0]) == id -1  else 0
    dir_y = int((coor[1] - center[1])/abs(coor[1] - center[1])) \
        if abs(coor[1] - center[1]) == id -1  else 0
    dir = (dir_x, dir_y)

    if dir   == (1  , 1  ) or dir == (1,  0): dir = (0  , -1 )
    elif dir == (1  , -1 ) or dir == (0, -1): dir = (-1 , 0  )
    elif dir == (-1 , -1 ) or dir == (-1, 0): dir = (0  , 1  )
    elif dir == (-1 , 1  ) or dir == (0,  1): dir = (1  , 0  )

    for index, d in enumerate(dirs, start=1):
        if dir == d :
            diff = max(abs(coor[0] - start[0]), abs(coor[1] - start[1]))
            return val + (index-1)*max_steps + diff
        else :
            start = (start[0] + max_steps * d[0], start[1] + max_steps * d[1])


if __name__ == "__main__":
    file = open(sys.argv[1])
    while True:
        try:
            size = int( file.readline() )
            pos = file.readline()
            if len(pos.split()) == 1:
                print(square_spiral_p(int(size), int(pos)))
            else :
                print(square_spiral_c(int(size), list(map(int, pos.split()))))
        except ValueError:
            sys.exit()
