import sys


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_contiguous_chain(x_stack, width, height, point):
    bk = []
    stack = [point]
    while len(stack) > 0:
        x, y = stack.pop()
        bk.append((x, y))
        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]
            if nx >= 0 and nx < width and ny >= 0 and ny < height and \
                    (nx, ny) not in bk and (nx, ny) in x_stack:
                x_stack.remove((nx, ny))
                stack.append((nx, ny))
    return 1


def count_contiguous_chain(x_stack, width, height):
    result = 0
    # result = []
    while len(x_stack) > 0:
        point = x_stack.pop()
        get_contiguous_chain(x_stack, width, height, point)
        result += 1
    return result


if __name__ == "__main__":
    file = open(sys.argv[1])
    height, width = file.readline().strip().split()
    width, height = int(width), int(height)
    x_stack = set([])
    for y in range(height):
        line = file.readline().rstrip()
        for x in range(width):
            if x < len(line) and line[x] == 'x':
                x_stack.add((x, y))
    result = count_contiguous_chain(x_stack, width, height)
    print(result)
    # print(len(result))
    # for i in range(len(result)):
        # print(result[i])
