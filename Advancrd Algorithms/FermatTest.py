# 5. Write a program for implementing Fermat test.
import math
import random

num = int(input('Enter a number : '))
ran = random.randint(2, num)
if (int(math.pow(ran, (num - 1))) % num) == 1:
    print('This is a prime number')
else:
    print('This is Not a Prime number')