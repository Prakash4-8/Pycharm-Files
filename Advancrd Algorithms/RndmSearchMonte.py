# (b) Monte Carlo Algorithm.
import random
size1 = int(input('Enter the size of the list : '))
lis1 = []
# input element in the list
for i in range(size1):
    num = int(input('Enter number {} : '.format(i + 1)))
    lis1.append(num)
ser = int(input('Enter the number you want search : '))
itr = int(input('Enter number of iteration you want to wait : '))
for i in range(itr):
    ran = random.randrange(0, len(lis1)) # pick a random value between 0-list length
    if lis1[ran] == ser:
        print('Element is present at index {}'.format(ran + 1))
        break
