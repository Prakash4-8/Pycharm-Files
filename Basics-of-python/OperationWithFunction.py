# 3. WAP to create a simple calculator to perform addition, sub, multiplication,
# and division using function. [Just learn how to work with function]
def add(a,b):
    return a + b
def sub(a,b):
    if a > b :
        return a - b
    else:
        return b - a
def mul(a,b):
    return a * b
def div(a,b):
    if a > b :
        return a // b
    else:
        return b // a
inpu = input('Enter operation you want to perform :')
if inpu == '+':
    num1 = int(input('Enter 1st number : '))
    num2 = int(input('Enter 2nd number : '))
    print(add(num1,num2))
elif inpu == '-':
    num1 = int(input('Enter 1st number : '))
    num2 = int(input('Enter 2nd number : '))
    print(sub(num1,num2))
elif inpu == '*':
    num1 = int(input('Enter 1st number : '))
    num2 = int(input('Enter 2nd number : '))
    print(mul(num1,num2))
elif inpu == '/':
    num1 = int(input('Enter 1st number : '))
    num2 = int(input('Enter 2nd number : '))
    print(div(num1,num2))
else:
    print('Invalid input ')
