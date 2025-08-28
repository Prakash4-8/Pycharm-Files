#1. Program to Display Fibonacci Sequence Using Recursion
def recursion(num):
    if num <= 1 :
        return num
    else:
        return (recursion(num - 1) + recursion(num - 2))
num = int(input('Enter a number : '))
for i in range(num):
    print(recursion(i))