import math

def add_two(func):
    def new_add_two(value):
        return str(func(value)) + " + 2"
    return new_add_two

@add_two
def square(value):
    return math.sqrt(value)


print(square(9))
#print(square(-1))
