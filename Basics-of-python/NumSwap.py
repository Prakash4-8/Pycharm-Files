#2. Write a program to swap two numbers with and without the use of extra variables (Single program).
num1=int(input('Using Temporary Variables\n Enter 1st number :'))
num2=int(input('Enter 2nd number :'))
print('Before swapping num1 : {0} num2 : {1}'.format(num1,num2))
temp=num1
num1=num2
num2=temp
print('After swapping num1 : {0} num2 : {1}'.format(num1,num2))
print('Without Temporary Variables\nBefore swapping num1 : {0} num2 : {1}'.format(num1,num2))
num1=(num1+num2)
num2=num1-num2
num1=num1-num2
print('After swapping num1 : {0} num2 : {1}'.format(num1,num2))
