import sys


def spliList(l,n):
    '''Split list *l* of length *n*
    '''
    f = lambda l,n: [l[i:i+n] for i in range(0,len(l),n)]


def main(w,h,x,y) :
    w = int(w)
    h = int(h)
    x = int(x)-1
    y = int(y)-1
    matrix = [[i for i in range(j,j+w)] for j in range(1, h*w, w)]
    up = lambda (x,y): (x-1,y)
    down = lambda (x,y): (x+1,y)
    left =  lambda (x,y): (x-1,y-1)
    right = lambda (x,y): (x+1,y+1)

TURN_LEFT = {(-1,0): (-1,-1), (-1,-1):(1,0), (1,0):(0,-1), (0,-1):(-1,0)}

def tranverse(matrix, step):
    list = [(0,0)]
    dir = (-1,0)
    pos = (0,0)
    for i in range(step): 
        list.append(pos)
        if 




if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])



