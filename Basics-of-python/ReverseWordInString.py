# 6. WAP to accept a line of text (string) and create a new string that stores the original string in reverse wordwise.
# For example,
# Input- This is python programming
# Output- programming python is This
sen = input('Enter a string : ')
sen2 = sen.split()
for i in range(len(sen2) - 1, -1, -1):
    print(sen2[i],end=' ')
