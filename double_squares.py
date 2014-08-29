import sys
import math

def load_file(fn):
    data = []
    with open(fn) as f:
        for line in f:
            data.append(int(line))
    return data[1:]


def double_squares(data):
    for number in data:
        no = 0
        x = 0
        y = int(math.sqrt(number))
        while not y < x:
            sum = pow(x, 2) + pow(y, 2)
            if sum == number:
                no += 1
                x += 1
                y -= 1
            elif sum < number:
                x += 1
            elif sum > number:
                y -= 1
        print no

if __name__ == "__main__":
    double_squares(load_file(sys.argv[1]))
