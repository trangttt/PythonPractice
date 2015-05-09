def base_three(n):
    result = []
    while n>0:
        result.insert(0, n%3)
        n = n/3
    return result

def sum_carry(a, b):
    result = []
    carry = 0
    for i, v in enumerate(a):
        sum = v + b[i] + carry
        if sum > 2 :
            carry = 1
            sum = sum%3
        else : carry = 0
        result.append(sum)
    if carry == 1: result.append(1)
    return result

def sub_not_carry(a, b):
    result = []
    for i, v in enumerate(a):
        sub = v - b[i] if i < len(b) else v
        if sub == -1 :
            result.append('L')
        elif sub == 0 :
            result.append('-')
        elif sub == 1:
            result.append('R')
    return result

def get_b(n):
    return [1 for i in range(n)]

def answer(x):
   x_3 = base_three(x)
   x_3_reversed = [i for i in reversed(x_3)]
   b = get_b(len(x_3))
   sum = sum_carry(x_3_reversed, b)
   ret = sub_not_carry(sum, b)
   return ret


if __name__ == "__main__":
    print answer(8)



# def matrix_mul(a, b):
#     if not len(a) == len(b):
#         return False
#     result = 0
#     for i, v in enumerate(a):
#         result += v * (b[i] -1)
#     return result
#
# def create_vector_a(n):
#     return [3**i for i in range(n)]
#
# _vector_b = -1
#
# def get_vector_b(n):
#     global _vector_b
#     _vector_b += 1
#     ret = base_three(_vector_b)
#     ret.append(2)
#     while len(ret) < n:
#         _vector_b += 1
#         ret = base_three(_vector_b)
#         ret.append(2)
#     if len(ret) > n : return False
#     return ret
#
# def base_three(n):
#     result = []
#     while True:
#         result.append(n%3)
#         n = n/3
#         if n == 0 : break
#     return result
#
# def answer(x):
#     size = len(base_three(x)) + 1
#     while True :
#         vector_a = create_vector_a(size)
#         vector_b = get_vector_b(size)
#         while not vector_b == False:
#              if matrix_mul(vector_a, vector_b) == x :
#                  result = []
#                  for i, v in enumerate(vector_b):
#                      if v == 0 : result.append('L')
#                      if v == 1 : result.append('-')
#                      if v == 2 : result.append('R')
#                  return result
#              else :
#                  vector_b = get_vector_b(size)
#         size += 1

