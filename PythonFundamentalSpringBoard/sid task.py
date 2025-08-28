# 1. Hello World Program
import math

print('Hello World')
# 2. Take input from your name and print hello your name
name = input('Enter Your Name :')
print('Hello {}'.format(name))

# 3. take name, age and percentage from user and display as follows
"""
My Name is: Prakash Mohapatra
Age: 21
percentage: 69
"""
name = input('Enter Name: ')
age = input('Enter Age: ')
percentage = input('Percentage: ')
print('My Name: {}\nAge: {}\nPercentage: {}'.format(name, age, percentage))
"""
# sum of two Number
"""
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
print('The sum of {} and {} is {}'.format(num1, num2, num1 + num2))
# do all mathematical operation
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
print('The sum of {} and {} is {}'.format(num1, num2, num1 + num2))
print('The subtraction of {} and {} is {}'.format(num1, num2, num1 - num2))
print('The multiplication of {} and {} is {}'.format(num1, num2, num1 * num2))
print('The division of {} and {} is {}'.format(num1, num2, num1 // num2))
print('The modulus of {} and {} is {}'.format(num1, num2, num1 % num2))
print('The square of {} and {} is {}'.format(num1, num2, num1 ** 2))
# calculate simple interest
p = input('Enter Principal Ammount: ')
t = input('Enter Time: ')
r = input('Enter Rate of Interest: ')
print('Simple Interest(S.I) is :{}'.format((p * t * r) / 100))
# square root of number without inbuilt function
x = input('Enter a number: ')
x = int(input())
print(x ** 0.5)
"""
area of square, rectange, and circle
"""
radius = int(input('Enter radius: '))
print('Area of Circle is {}'.format(math.pi * radius ** 2))
length = int(input('Enter length: '))
breath = int(input('Enter breath: '))
print('Area of Rectange: {}'.format(length * breath))
side = int(input('Enter Side of Square: '))
print('Side of Square is {}'.format(side ** 2))
"""
odd or even
"""
num1 = int(input("Enter the Number: "))
if num1%2 == 0:
    print('{} is Even'.format(num1))
else:
    print('{} is Odd'.format(num1))
"""
leap year
"""


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
        leap = True
    return leap


year = int(input())

"""
use switch to print seven days
"""
val = int(input('Enter Value: '))
match val:
        case 1:
            print('Sunday')
        case 2:
            print('Monday')
        case 3:
            print('Tuesday')
        case 4:
            print('Wednesday')
        case 5:
            print('Thursday')
        case 6:
            print('Friday')
        case 7:
            print('Saturday')
        case default:
            print('Invalid Input')
"""
large between two floating number
"""
val1 = float(input('Enter first number: '))
val2 = float(input('Enter second number: '))
if val2>val1:
    print('{} is greater than {}'.format(val2, val1))
else:
    print('{} is greater than {}'.format(val1, val2))
mark = int(input('Enter Mark: '))
if 90 <= mark <=100:
    print('A+')
elif 80<= mark <= 89:
    print('A')
elif 70 <= mark <= 79:
    print('B+')
elif 60 <= mark <= 69:
    print('B')
elif 55 <= mark <= 59:
    print('C+')
elif 50 <= mark <= 54:
    print('C')
else:
    print('F')

"""
smallest number between three numbers
"""

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))
min = num1 if num1 < num2 else num2 if num2 < num3 else num3
print(min)