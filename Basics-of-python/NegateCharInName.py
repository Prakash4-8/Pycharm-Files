# 2. WAP to take your name as input and store those letters which aren't presence in your name. Categories them as
# vowels and consonants.
#
# For example:
# Name: siddharth singh kushwaha
# Output:
# letters not in my name: ['b', 'c', 'e', 'f', 'j', 'l', 'm', 'o', 'p', 'q', 'v', 'x', 'y', 'z']
# Vowels - 2
# Cosonants - 12
name = input('Enter your name : ')
charpool = []
for i in range(97, 123):
    if chr(i) not in name:
        charpool.append(chr(i))
vow = 0
cons = 0
for i in charpool:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vow += 1
    else:
        cons += 1
print('Letters not in my name', charpool)
print('Number of vowels', vow)
print('number of constants', cons)