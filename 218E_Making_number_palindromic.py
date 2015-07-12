#!/bin/python3


is_palindromic = lambda x: x == x[::-1]

def making_palindromic(n):
    step = 0
    while not is_palindromic(str(n)):
        n += int(str(n)[::-1])
        step += 1
    return (n, step)

numbers = ["123","286","196196871"]
for number in numbers:
    palindrome, step = making_palindromic(int(number))
    print(number, "gets palindromic after", step, "steps:", palindrome)
