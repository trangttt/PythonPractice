
import random

def isPrime(n):
    if n % 2 == 0 : return 0
    else :
        for i in range(5):
            a = random.randint(3,n-1)
            # if a^(n-1) == 1 (mod n) , n is probably a prime
            if pow(a, n-1, n) == 1 :
                if i == 4: return 1
                else : continue
            #else n is exactly a composite
            else : return 0

def isPalindrome(s):
    return s == s[::-1]


def primePalindrome() :
    for i in range(999,1, -1):
        if isPrime(i) and isPalindrome(str(i)):
            print i
            return 0
        else : continue

if __name__ == "__main__" :
    primePalindrome()

__author__ = 'dantoccatu'
