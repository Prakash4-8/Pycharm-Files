#4. Write a program to check whether a substring is in the string or not. If yes, then print the index of it.
# Note: There is no duplication sub-string.
#Forex: Input string: We are learning python
#Input substring: python
#output [your output should look like this]: The substring "python" is present at 16 index.
#Suppose, Input substring: PYTHON
#output: The substring "PYTHON" is not present in the string.
str1=input('Enter sentences :')
print(str1)
str2=input("Enter a word to find it's index :")
if str2 in str1:
    print('The substring {0} is present at {1} index'.format(str2,str1.find(str2)))
else:
    print('The substring "new is not present in the string"')