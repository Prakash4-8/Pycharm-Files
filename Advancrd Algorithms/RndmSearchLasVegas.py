# 1. Write a program for Randomized Search using (a) Las Vegas algorithm

import random

size = int(input('Enter the size of the list : '))
lis1 = []
# input element in the list
for i in range(size):
    num = int(input('Enter number {} : '.format(i + 1)))
    lis1.append(num)
ser = int(input('Enter the number you want search : '))
flg = True
while flg:
    ran = random.randrange(0, len(lis1))
    if lis1[ran] == ser:
        print('Element is present at index {}'.format(ran + 1))
        break
