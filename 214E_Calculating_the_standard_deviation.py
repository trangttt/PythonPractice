import math

num = [int(i) for i in input().split(' ')]
mean=sum(num)/len(num)
diff = [(i-mean)**2 for i in num]
total = sum(diff)
variance = total/len(num)
deviation = math.sqrt(variance)
print('%.4f' % deviation)
