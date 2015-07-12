def solution(X, Y, D):
    j = 0
    while X < Y:
        X += D
        j += 1
    return j

print(solution(10, 85, 30))
