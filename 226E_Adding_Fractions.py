import sys
from functools import reduce

file = open(sys.argv[1])
no = int(file.readline())

fracs = []
for i in range(no):
    num, den = map(int, file.readline().split("/"))
    fracs.append((num, den))


def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)


def lcd(a, b):
    return a*b/gcd(a, b)

com_den = reduce(lcd, [frac[1] for frac in fracs])
#com_den = reduce(lambda x, y: x*y, [frac[1] for frac in fracs])
sum_num = reduce(lambda x, y: x+y, [int(frac[0]*com_den/frac[1]) for frac in fracs])
max_fac = gcd(com_den, sum_num)

print("{}/{}".format(int(sum_num/max_fac), int(com_den/max_fac)))
