import random
import copy

def initialize():
    '''Initialize game
    '''
    car = random.randint(0,2)
    l = []
    for i in range(3):
        if (i == car) : l.append('c')
        else : l.append('g')
    return l

def choice():
    '''Choose a door
    '''
    return random.randint(3)

def main():
    n = int(raw_input("Input a number:"))
    m = n
    s1 = 0
    s2 = 0
    while (n>0):
        car = random.randint(1,3)
        pick = random.randint(1,3)
        if ( pick == car):
            s1 += 1
        else :
            s2 += 1
        n -= 1
    print "Tactic 1: {0:3.2%} winning chance".format(float(s1/m))
    print "Tactic 2: {0:3.2%} winning chance".format(float(s2/m))
        
if  __name__ == "__main__" :
    main()
