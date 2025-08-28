#Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)
x=input('Eneter the operation you want to perform (+,-,*,/) :')
if x in ['+', '-', '*','/']:
    y = int(input('Enter 1st operand :'))
    z = int(input('Enter 2nd operand :'))
    if x == '+':
        print('Addition of {0} and {1} is {2}'.format(y, z, y + z))
    if x == '-':
        print('Subtraction pf {0} and {1} is {2}'.format(y, z, y - z))
    if x == '*':
        print('Multiplication of {0} and {1} is {2}'.format(y, z, y * z))
    if x == '/':
        print('Division of {0} and {1} is {2}'.format(y, z, y / z))

