#1. A number is said to be a Perfect number if the sum of all the divisors except number itself, is equal to that number.
#   Write the program to find whether a number is Perfect or not.
 #   Example: Divisor of 6 are 1, 2, and 3. Sum of divisor 1 + 2 + 3 = 6 (which is equals to that number) so, 6 is a perfect number.
num=int(input("Enter a number to know  whether it's perfect or not :" ))
temp=num
sum=0
for i in range(1,num):#bydefalut i will starts from 0 to n-1
    if num%i == 0:
        sum=sum+i
if sum==temp:
    print('This is a perfect number')
else:
    print('This is not a perfect number')