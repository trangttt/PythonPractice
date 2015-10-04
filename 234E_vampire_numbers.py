import sys
from functools import reduce
import itertools


def vampire_number(digits, fangs):
    noDigits = int(digits/fangs)
    for nums in itertools.combinations_with_replacement(range(10**(noDigits-1), 10**noDigits), fangs):
        total = reduce(lambda x,y: x*y, nums)
        if sorted(list(str(total))) == sorted(list(reduce(lambda x,y: x+y, map(str, nums)))):
            print(total, '=', '*'.join(map(str, nums)))


if __name__ == "__main__":
    digits, fangs = int(sys.argv[1]), int(sys.argv[2])
    vampire_number(digits, fangs)
