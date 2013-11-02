import sys
def find_multiples(n):
    '''Find sum of all multiples of or and 5
    '''
    set = range(n)
    set = filter(lambda x: not x%3 or not x%5, set)
    return set

def main(n):
    ret = find_multiples(n)
    print ret
    print sum(ret)


if __name__ == "__main__" :
    if len(sys.argv) == 2 :
        main(int(sys.argv[1]))
    else :
        print 'Usage: %s n' % sys.argv[0]
        print 'Find all multiples of 3 and 5 less than n '
        sys.exit(2)
