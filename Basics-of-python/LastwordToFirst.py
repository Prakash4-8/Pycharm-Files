# 1. WAP to accept a line of text (String) from the user and modify it such that the last word comes to the first position.
# For example Input- It doesn't make sense
# Output-  sense It doesn't make
import collections

name = input('Enter a string : ')
tem=name.split()
print(tem[len(tem) - 1],end=' ')
for i in range(0,len(tem) -1) :
    print(tem[i],end=' ')
    # using collection
lis = collections.deque(tem)
print(type(lis))
lis.rotate()
for i in lis:
    print(i,end=' ')