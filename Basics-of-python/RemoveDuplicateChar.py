# 1. Write a program to remove duplicate characters in the given string.
name = input('Enter a string : ')
new=[]
for i in name:
    if i not in new:
        new.append(i)
print(*new,sep='')