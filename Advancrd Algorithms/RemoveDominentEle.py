import random
# 2. Write a program for deleting dominate element of array by Monte
# Carlo Algorithm.
size = int(input('Enter the size of the list : '))
lis1 = []
# input element in the list
for i in range(size):
    num = int(input('Enter number {} : '.format(i + 1)))
    lis1.append(num)
# taking unique element into one list
list2 =[]
for i in lis1:
    if i not in list2:
        list2.append(i)
# list for counting frequency
dict = {}
for i in list2:
    temp = 0
    for j in lis1:
        if i == j:
            temp += 1
    dict[i] = temp
# finding most dominant element
mx = 0
k = 100 # number of iteration
for i in range(k):
    ran = random.randrange(0, len(dict.values()))
    x = dict.values()[ran]
    print(x)
    if mx <= x:
        mx = dict.values()[ran]
j = 0
for i in dict.keys():
    if dict[i] == mx:
        j = i
for i in lis1:
    if i == j:
        lis1.remove(i)
print(lis1)
