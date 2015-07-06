next_dir = lambda d: (0, -1) if d[1] == 0 else (-1, 0)
move = lambda x, y, d, n: (x + d[0] * n, y + d[1] * n)


def snake(text):
    print('\n{}\n'.format(text))
    words = text.split()

    res = build_grid(words)

    max_w = max(map(lambda k: k[0], res.keys())) + 1
    max_h = max(map(lambda k: k[1], res.keys())) + 1
    grid = [[' ' for y in range(max_w)] for x in range(max_h)]

    for key in res:
        grid[key[1]][key[0]] = res[key]

    for row in grid:
        print(''.join(row))


def build_grid(words, x=0, y=0, occupied=None, d=None):
    if len(words) == 0:
        return occupied

    occupied = dict() if occupied is None else occupied
    d = (1, 0) if d is None else d
    word = words[0]
    words = words[1:]

    for _ in range(2):
        if (x + d[0]) >= 0 and (y + d[1]) >= 0 \
                and all((move(x, y, d, n) not in occupied for n in range(1, len(word)))):

            _occupied = dict(occupied)

            for n in range(len(word)):
                _occupied[(move(x, y, d, n))] = word[n]

            pos = move(x, y, d, n)

            result = build_grid(words, pos[0], pos[1], _occupied, next_dir(d))

            if result is not None:
                return result

        d = (-d[0], -d[1])

    return None


if __name__ == "__main__":
    snake('SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE')
    snake('DELOREAN NEUTER RAMSHACKLE EAR RUMP PALINDROME EXEMPLARY YARD')
    snake('CAN NINCOMPOOP PANTS SCRIMSHAW WASTELAND DIRK KOMBAT TEMP PLUNGE ESTER REGRET TOMBOY')
    snake('NICKEL LEDERHOSEN NARCOTRAFFICANTE EAT TO OATS SOUP PAST TELEMARKETER RUST THINGAMAJIG GROSS SALTPETER REISSUE ELEPHANTITIS')
