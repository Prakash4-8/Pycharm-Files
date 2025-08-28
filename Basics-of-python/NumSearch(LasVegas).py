# program to search a number in an array using las vegas algorithm
import random

list1 = []
n = int(input('Enter size of the list : '))
for i in range(n):
    put = int(input('Enter element {} : '.format(i+1)))
    list1.append(put)
find = int(input('Enter the element to find : '))
f = False
count = 0
while f == False:
    count += 1
    comp = list1.index(random.choice(list1))
    if list1[comp] == find:
        print('Element is found after {} comparison at index {}'.format(count, comp))
        f = True