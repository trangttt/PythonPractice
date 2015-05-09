import random
import copy



_DOOR = '''\
xxxx  
xxxx  
xxxx  
xxxx  
'''


_OPENED_DOOR = '''\
xxxx  
x  x  
x  x  
xxxx  
'''

def gameSimulation():
    n = raw_input("Input a number:")
    m = n
    print _DOOR
    
def testing():
    n = raw_input("Input a number :")
:

def main():
    n = int(raw_input("Input a number:"))
    m = n
    s1 = 0
    s2 = 0
    r
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
    #imain()
    gameSimulation()
