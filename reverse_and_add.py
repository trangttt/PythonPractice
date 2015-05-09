import sys

def load_file(fn):
    data = []
    with open(fn) as f:
        for line in f:
            data.append(line)
    return data

def reverse(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(data):
    for line in data:
        n = int(line)
        loop_no = 1
        t = n + reverse(n)
        while not is_palindrome(t) :
            loop_no += 1
            t = t + reverse(t)
            continue
        print loop_no, t

if __name__ == "__main__" :
    reverse_and_add(load_file(sys.argv[1]))
