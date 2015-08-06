import sys


input = open(sys.argv[1]).read().splitlines()

for test in a:
    print(test)


for couple in input:
    num1, num2 = couple.split()
    ret = "{:030b}".format(int(num1) ^ int(num2)).count('0')
    print("{:.2f}% Compatibility".format(ret*100/32))
    print("{} should avoid {}".format(int(num1), 0xFFFFFFFF ^ int(num1)))
    print("{} should avoid {}".format(int(num2), 0xFFFFFFFF ^ int(num2)))
    print('')
