#https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
sum = 100
values = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]



def divide_and_conquer(values, sum):
    if len(values) == 0 :
        return None

    if len(values) == 1:
        return [values] if sum == values[0] else None


    first = values[0]
    rest = values[1:]

    result = []

    #ADD
    p_result_add = divide_and_conquer(rest, sum - first)
    result += map(lambda x: [first] + x, p_result_add) if p_result_add is not None else []

    #SUBTRACT
    rest[0] *= -1
    p_result_sub = divide_and_conquer(rest, sum - first)
    result += map(lambda x: [first] + x, p_result_sub) if p_result_sub is not None else []

    #JOIN
    new_values = [int(''.join(map(str, values[0:2])))] + (values[2:] if len(values) >=2 else None)
    p_result_group = divide_and_conquer(new_values, sum)
    result += p_result_group if p_result_group is not None else []

    if result == [] : return None
    return result


for i in  divide_and_conquer(values, sum):
    print(i)
    print(eval("+".join(map(str, i))))

