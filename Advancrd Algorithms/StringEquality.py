# 3. Write a program for testing string equality
import random

string1 = input('Enter 1st string : ')
pattern = input('Enter 2nd string : ')
sum1 = 1
ran = random.randint(1, 50)
ran = 2*ran + 1
for i in string1:
    sum1 = ord(i) + sum1 % ran
sum2 = 1
for i in pattern:
    sum2 = ord(i) + sum2 % ran
if sum1 == sum2:
    print('String matched ')
else:
    print('String not matched ')