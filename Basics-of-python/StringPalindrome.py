# 2. WAP to check whether a string is a palindrome or not. Ex: madam
name = input('Enter a name : ')
new = ''
for i in range(len(name)-1, -1,-1):
    new+=name[i]

if name.lower() == new.lower():
    print('{} id palindrome string '.format(name))
else:
    print('{} is not palindrome string '.format(name))