import sys
import re

file = open(sys.argv[1])

no = file.readline()
lines = file.read()

print(no)
#lines = re.sub(r' ?\+-*\+ ?', '', lines)
#lines = re.sub(r' ?(\||\+).*(\||\+) ?', "", lines)
lines = re.sub(r'([\+\|][^\|\+]*[\+\|])?([^\+\-\|]*)([\+\|][^\|\+]*[\+\|])?', r'\2', lines)
#lines = re.sub(r'  +(\w)', r'\1', lines)
#lines = re.sub(r'-\n', '', lines)
#lines = re.sub(r'\n\n', '|', lines)
print(lines)
#ret = []
#for line in lines.split('\n'):
    #ret.append(line.strip())
#print(re.sub(r'\|', r'\n', ' '.join(ret)))
