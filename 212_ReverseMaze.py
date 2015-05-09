# Imports re which is the Regular expression package
import re
# Import chain which lets you generate an iterator from multiple
# iterable objects
from itertools import chain

# Grab the input data
height = int(input())
lines = [input().strip() for n in range(height)]
width = max(len(x) for x in lines)

# routes is a list of all possible (x,y) tuples where (x,y)
# is a space. (i.e. the list of all valid points)
routes = {(x, y)
            for x in range(width)
            for y in range(height)
            if lines[y][x].isspace()}

# This is the clever bit of the code, you parse through the input
# string and for each instruction you add a lambda function to the
# list which when given the current state of the system returns the
# next state. The state is represented by 4 variables, x, y, dx, dy
# where x and y is the current position and dx, dy encode the direction
raw_path = input().strip()
path = list(chain.from_iterable(
        {'l': lambda _: [lambda x, y, dx, dy: (x, y, dy, -dx)],
         'r': lambda _: [lambda x, y, dx, dy: (x, y, -dy, dx)]}
            .get(entry, lambda ct: [lambda x, y, dx, dy: (x + dx,
                                                          y + dy,
                                                          dx, dy)] * int(ct))
            (entry)
         for entry in re.findall('[rl]|[0-9]+', raw_path)))

test = list (chain.from_iterable(
        {'l': lambda _: ['left'], 'r' : lambda _: ['right']}
            .get(entry, lambda ct: ['straight'] * int(ct))
                (entry)
        for entry in re.findall('[rl]|[0-9]+', raw_path)
    ))

def get_entry(t):
    return [t]

test1 = list(chain.from_iterable(
    #{'l': lambda _: ['left'], 'r': lambda _: ['right']}.get(entry, lambda ct: [ct])
    get_entry(entry)
        #(entry)
    for entry in re.findall('[rl]|[0-9]+', raw_path)
))

print(test1)
for i in test1 :print(i)
print(raw_path)
print(path)
#for i in test : print(i)






