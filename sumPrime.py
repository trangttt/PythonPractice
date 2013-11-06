import sys
import math





def main(n):
    base = range(2,int(math.sqrt(n)))
    prime = range(2,n)
    for i in base :
        prime = filter(lambda x: x==i or x%i, prime)
    
    




if __name__ == "__main__" :
    if len(sys.argv) ==  2 :
        main(int(sys.argv[1]))
    else :
        print 'usage: %s N' %sys.argv[0]
        print 'Calculate all prime less than N'
    

