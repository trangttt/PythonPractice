#!python3
input = "00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000"
# input = "1101010"
print_line = lambda x: "".join(' ' if c==0 else 'x' for c in x)
prev = [int(c) for c in input]
print(print_line(prev))
for i in range(25):
    prev.append(0)
    prev.insert(0,0)
    next = [ prev[i-1] ^ prev[i+1] for i in range(1, len(prev)-1)]
    print(print_line(next))
    prev = next
