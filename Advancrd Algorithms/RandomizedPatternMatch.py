# 4. Write a program for Randomized pattern matching algorithm.
import random

def hash(val):
    sum = 1
    for i in val:
        sum = ord(i) + sum % ran
    return sum
text = input('Enter Text : ')
pattern = input('Enter Pattern : ')

ran = random.randint(1, 50)
ran = 2*ran + 1
patt = 0
for i in range(len(text) - len(pattern) +1):
    if hash(text[i: i + len(pattern)]) == hash(pattern):
       print('Pattern match')
       patt = 1
if patt != 1:
    print('Pattern not match')