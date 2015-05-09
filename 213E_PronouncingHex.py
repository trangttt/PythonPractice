import re

number = input()

tens = {'A': 'atta', 'B' : 'bibbity', 'C': 'city', 'D' : 'dickety', 'E': 'ebbity', 'F' : 'fleventy'}
ones = {'1': 'one', '2': 'two', '3': 'three', '4' :'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',\
        'A': 'aa', 'B': 'bee', 'C' : 'cee', 'D': 'dee', 'E' : 'ee', 'F': 'fee'}


number = number[2:]



parts = re.findall(r'[A-F0-9]{2}', number)
pronounce = ''
for i, part in enumerate(reversed(parts)):
    if part is None :
        continue
    j = 1 if i > 0 else 0
    k = 1 if part[1] is not '0' else 0
    pronounce = tens.get(part[0], 'Error1') + \
                k * (('-') + ones.get(part[1], 'Error2') ) +\
                j * ' bitey' + ' ' + pronounce

print(pronounce)


