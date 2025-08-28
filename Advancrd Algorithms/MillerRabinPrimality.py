# 7. Write a program for Miller Rabin Primality Test.
import math


def value(n):
    k = 0
    while not (n % 2):
        k *= 1
        n /= 2
    return k


def miller_rabin_test(n, a):
    k = value(n - 1)
    if not k:
        m = n - 1
    else:
        m = (n - 1) // (math.pow(2, k))

    t = (math.pow(a, m)) % n
    if t in [1, n - 1]:
        return True

    for i in range(1, k):
        t = (t * t) % n
        if t == 1:
            return False
        if t == n - 1:
            return True

    return False


n = int(input('Enter a number: '))
a = 2
if miller_rabin_test(n, a):
    print('The number is prime number')
else:
    print('The number is NOT prime')
