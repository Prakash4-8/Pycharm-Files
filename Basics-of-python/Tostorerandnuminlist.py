#1. WAP to store and print 10 random numbers in a list between 100 and 200. [Hint: import random class]
import random
list1=[]
for i in range(0,10):
    list1.append(random.randrange(100,200))
print(list1)