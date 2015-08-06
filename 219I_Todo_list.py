import sys
import re
from collections import defaultdict

coms  = open(sys.argv[1]).readlines()

cats = defaultdict(set)

for com in coms:
    if com.startswith('addItem'):
        matched = re.findall(r'\'([^\']*)\'', com)
        for i in range(1, len(matched)):
            cats[matched[i]].add(matched[0])
    elif com.startswith('deleteItem'):
        matched = re.findall(r'\'([^\']*)\'', com)
        for i in range(1, len(matched)):
            cats[matched[i]].remove(matched[0])
    elif com.startswith('viewList'):
        matched = re.findall(r"'([^\']*)'", com)
        res_set = cats[matched[0]]
        for i in range(1, len(matched)):
            res_set = res_set.intersection(cats[matched[i]])
        print("{:-^30}".format(" & ".join(s.upper() for s in matched)))
        for item in res_set:
            print("- ", item)
