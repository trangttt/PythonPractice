import re
import sys

def roman2dec(roman):
    pattern = '^(M{1,4})?(CM)?(CD|D)?(C{1,3})?(XC)?(XL|L)?(X{1,3})?(IX)?(IV|V)?(I{1,3})?'
    res = re.match(pattern, roman)
    if res:
        number = 0
        if res.group(1): number += len(res.group(1)) * 1000
        if res.group(2): number += 900
        if res.group(3):
            if res.group(3) == 'CD': number += 400
            if res.group(3) == 'D': number += 500
        if res.group(4): number += len(res.group(4)) * 100
        if res.group(5): number += 90
        if res.group(6):
            if res.group(6) == 'XL': number += 40
            if res.group(6) == 'L': number += 50
        if res.group(7): number += len(res.group(7)) * 10
        if res.group(8): number += 9
        if res.group(9):
            if res.group(9) == 'IV': number += 4
            if res.group(9) == 'V': number += 5
        if res.group(10): number += len(res.group(10))

        print(number)
    else:
        print("Invalid Roman number")


if __name__ == "__main__":
    roman2dec(sys.argv[1])
