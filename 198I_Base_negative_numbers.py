import sys

def base2dec(number, base):
    total = 0
    for i, c in enumerate(reversed(number)):
        total += int(c) * (base**i)
    return total

def dec2base(number, base):
    result = ''
    div = number % base
    while number != 0 :
        result = str(div) + result
        number = int(number/base)
        div = number % base
    return result

print(base2dec('7211', -10))
print(dec2base(base2dec('1302201', -4), 4))
print(base2dec('12345678', -10))
print(dec2base(base2dec('12345678', -10), 10))
print(dec2base(base2dec('4021553', -7), 7))
# print(dec2base(base2dec('4016423', 7), -7))

