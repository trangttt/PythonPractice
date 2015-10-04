import random
import sys

def next_move(matrix):
    dirs = [ (x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x, y) != (0, 0) ]
    width = len(matrix[0])
    height = len(matrix)


    def is_out_of_matrix(x, y):
        if x < 0 or x >= height or y < 0 or y >= width:
            return True
        else: return False

    nextMatrix = [['' for y in range(width)] for x in range(height)]

    for x in range(height):
        for y in range(width):
            count = []
            for dir in dirs:
                neighbour = (x + dir[0], y + dir[1])
                if not is_out_of_matrix(*neighbour) and matrix[neighbour[0]][neighbour[1]] != ' ':
                    count.append(matrix[neighbour[0]][neighbour[1]])

            if matrix[x][y] != ' ' and len(count)<=1: nextMatrix[x][y] = ' '
            elif matrix[x][y] != ' ' and 2 <= len(count) <= 3: nextMatrix[x][y] = matrix[x][y]
            elif matrix[x][y] != ' ' and len(count)>=4: nextMatrix[x][y] = ' '
            elif matrix[x][y] == ' ' and len(count)==3: nextMatrix[x][y] = random.choice(count)
            else: nextMatrix[x][y] = matrix[x][y]
    return nextMatrix


if __name__ == "__main__":
    file = open(sys.argv[1])
    matrix = []
    maxX = 0
    for line in file.readlines():
        if len(line.rstrip('\n')) > maxX: maxX = len(line.rstrip('\n'))
        matrix.append(list(line.rstrip('\n')))

    for index, row in enumerate(matrix):
        if len(row) < maxX: matrix[index] += ' ' * (maxX - len(row))

    for line in next_move(matrix):
        print(''.join(line))
