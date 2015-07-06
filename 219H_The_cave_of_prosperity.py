#!/bin/python3
import sys

bar, nu, *nuggets = [float(i) for i in open(sys.argv[1]).read().splitlines()]


get_masks = lambda no: [ str(bin(i)).lstrip('0b').rjust(no, '0') for i in range(2**no)]
get_mask = lambda x: [float(i) for i in x]
total = lambda x,y: sum([ t1*t2 for t1,t2 in zip(x,y)])


def calculate_subset_sum(subset):
    masks = get_masks(len(subset))
    return [ (total(get_mask(mask), subset), mask) for mask in masks]

pre_nuggets = nuggets[:int(nu/2)]
pos_nuggets = nuggets[int(nu/2):]

pre_sum = calculate_subset_sum(pre_nuggets)
pos_sum = sorted(calculate_subset_sum(pos_nuggets), key = lambda x: x[0])

#print(pre_sum)
#print(pos_sum)

def quick_search(a, bar, s):
    if s >= bar: return
    lb = 0
    ub = len(a)-1
    cur = int((ub+lb)/2)
    new_s = s
    while lb < ub:
        new_s = s + a[cur][0]
        if new_s < bar and s + a[cur+1][0] > bar :
            return cur
        if new_s < bar :
            cur = int((cur+ub)/2)
            lb = cur + 1
        else :
            cur = int((lb+cur)/2)
            ub = cur - 1


total_sum = []
for s, m in pre_sum:
    if s >= bar : continue
    index = quick_search(pos_sum, bar, s)
    if index is not None : total_sum.append( (s + pos_sum[index][0], m, pos_sum[index][1]))


max_sum = max(total_sum, key=lambda x: x[0])

print("%.7f" % max_sum[0])
for i,v in enumerate("".join(max_sum[1:])):
    if v == "1": print(nuggets[i])


#print("%.7f" % (max_mask[0]))
#for i, v in enumerate(max_mask[1]):
    #if v == '1' : print(nuggets[i])
