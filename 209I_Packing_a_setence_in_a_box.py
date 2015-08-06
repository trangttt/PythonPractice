#!/bin/python3

sentence = input()


def find_box_size(n):
    for i in range(int(n**0.5), n):
        if n % i == 0:
            yield i


def snake_packing(sentence):
    new_sen = sentence.translate({ord(" "): None})
    l = len(new_sen)
    he = next(find_box_size(l))
    wi = int(l/he)
    for r in range(0, l, wi):
        if r % 2 == 0:
            print(new_sen[r:r+wi])
        else:
            print(new_sen[r+wi-1:r-1:-1])


def spiral_packing(sentence):
    new_sen = sentence.translate({ord(" "): None})
    l = len(new_sen)
    he = next(find_box_size(l))
    wi = int(l/he)

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    x, y, dir = 0, 0, 0

    ret = [[" " for r in range(wi)] for c in range(he)]
    for c in new_sen:
        ret[x][y] = c
        next_x, next_y = x + dirs[dir][0], y + dirs[dir][1]
        if next_x < 0 or next_x > wi-1 or next_y < 0 or next_y > he-1 \
                or ret[next_x][next_y] != " ":
            dir = (dir+1) % 4
            next_x, next_y = x + dirs[dir][0], y + dirs[dir][1]
        x, y = next_x, next_y

    print("\n".join("".join(ret[x][y] for x in range(wi)) for y in range(he)))

snake_packing(sentence)
print('\n')
spiral_packing(sentence)
