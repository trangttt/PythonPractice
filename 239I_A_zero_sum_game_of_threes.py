import sys

def zero_sum(n):
    result= three(n,0)
    if result:
        for k in sorted(result.keys(), reverse=True):
            print(k, result[k])
    else:
        print("Impossible")

def memoize(f):
    class memodict(dict):
        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self,key):
            ret = self[key] = self.f(*key)
            return ret

    return memodict(f)

@memoize
def three(n, sum):
    if n < 1:
        return {}
    elif n == 1:
        if sum == 0: return {1:0}
        else: return {}
    elif n%3 == 0:
        ret = three(int(n/3), sum)
        if ret:
            ret[n] = 0
    elif n%3 == 1:
        ret =  three( int((n-1)/3), sum+1 )
        if ret:
           ret[n] = -1
        else:
            ret = three( int((n+2)/3), sum-2)
            if ret: ret[n] = 2
    if n%3 == 2:
        ret = three( int((n+1)/3), sum-1 )
        if ret:
            ret[n] = 1
        else:
            ret = three( int((n-2)/3), sum+2 )
            if ret: ret[n]=-2
    return ret

if __name__ == "__main__":
    zero_sum(int(sys.argv[1]))
