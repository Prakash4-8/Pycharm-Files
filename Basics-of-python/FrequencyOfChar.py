# 9. WAP to print the frequency of each character in a string (single word). For example,
# Input (only letters, ignore uppercase and lowercase)- madam
# Output-
# Character   Frequency
# m                 2
# a                 2
# d                 1
sen = input('Enter a word : ')
sen2 = ''
for i in sen :
    if i not in sen2:
        sen2 += i
print('Character Frequency')
for i in sen2:
    print('   {} \t\t\t {}'.format(i,sen.count(i)))