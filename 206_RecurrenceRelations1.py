import functools

expr = input().split()

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

def recurrence(value) :
    for i in expr:
        value = operators.get(i[0], lambda x: x)(value, int(i[1:]))
    return value

start = int(input())
repetition    = int(input())

result = start
for j in range(repetition + 1):
    print("Term %d: %.2f" % (j, result))
    result = recurrence(result)


##############################
###      EXCITING!!!       ###
##############################
def recurrence(expr, val, end):
    str = functools.reduce(lambda l,r: "(%s%s)" % (l,r), expr.split(), "x")
    print(str)
    f = eval("lambda x: %s" % str)
    for i in range(end + 1):
        print("Term %d: %.2f" % (i, val))
        val = f(val)

recurrence(input(), int(input()), int(input()))