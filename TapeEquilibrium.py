#!//bin/python2.7

def solution(A):
    left = 0
    right = sum(A)
    result = []
    for pivot in xrange(0,len(A)-1):
        left += A[pivot]
        right -= A[pivot]
        if left == right : return 0
        else : result.append(abs(left - right))
    return min(result)


print(solution([3, -1, 2, 4]))
