import sys
from PIL import Image

im = Image.open(sys.argv[1])

width, height = im.size
pixels = im.tobytes()

coor = set([(x, y) for x in range(width) for y in range(height)])


def get_color(p, px, w, h):
    cb = int(len(px)/(w*h))
    rc = lambda p: (p[1] * w + p[0]) * cb
    return px[rc(p):rc(p) + cb]

_BLACK = b'\x00\x00\x00'


def detect_circle(point, pixels, w, h):
    in_prog = {point}
    done = set()
    ci = set([(x, y) for x in range(width) for y in range(height)])
    while len(in_prog) > 0:
        p = in_prog.pop()
        if p in ci: ci.remove(p)
        else:
            continue
        if get_color(p, pixels, w, h) == _BLACK:
            done.add(p)
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_p = (p[0] + dir[0], p[1] + dir[1])
                if new_p[0] >= 0 and new_p[0] < w and new_p[1] >= 0 and new_p[1] < h:
                    in_prog.add(new_p)
    return done

cirs = []
while len(coor) > 0:
    p = coor.pop()
    if get_color(p, pixels, width, height) == _BLACK:
        cir = detect_circle(p, pixels, width, height)
        coor = coor - cir
        if len(cir) > 0:
            cirs.append(cir)
pis = []
for i, cir in enumerate(cirs):
    area = len(cir)
    dia = max(p[0] for p in cir) - min(p[0] for p in cir) + 1
    pi = area*4/(dia**2)
    print('Circle {:>2d} Area {:>10d} Dia {:>5d}'.format(i, area, dia))
    pis.append(pi)

print('Number of Circles : {:0>2d}'.format(len(cirs)))
print('Estimated pi      : {:>.9f}'.format(sum(pis)/len(pis)))
