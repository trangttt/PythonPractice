import sys
import re

file = open(sys.argv[1])

list = set()
for line in file.readlines():
    if line.startswith("addItem"):
        item = re.match(r'addItem\(\'(.*)\'\)', line)
        list.add(item.group(1).strip())
    if line.startswith("deleteItem"):
        item = re.match(r'deleteItem\(\'(.*)\'\)', line)
        try:
            list.remove(item.group(1).strip())
        except KeyError:
            print('Item not found!!!')
    if line.startswith('viewList();'):
        for item in list:
            print(item)
