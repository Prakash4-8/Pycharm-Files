# anonymous function to find factorial
import math

fact = lambda num: 1 if num == 0 else num * fact(num - 1)
x = int(input('Enter a number to find it\'s factorial: '))
print(fact(x))

# fibonacci series
def recursion(num):
    if num <= 1 :
        return num
    else:
        return (recursion(num - 1) + recursion(num - 2))
num = int(input('Enter a number : '))
for i in range(num):
    print(recursion(i))
# Calculate area of rectangle/square/triangle using variable length arguments
def areaOfshapes(*side):
    if len(side) == 1:
        return side[0] * side[0]
    elif len(side) == 2:
        return side[0] * side[1]
    elif len(side) == 3:
        s = (side[0] + side[1] + side[2])/2
        return math.sqrt(s*(s - side[0])*(s - side[1])*(s - side[2]))
    else:
        print('Invalid input !')
print('Area of Square : ',areaOfshapes(4))
print('Area of Rectangle : ',areaOfshapes(2,3))
print('Area of Triangle : ',areaOfshapes(2,3,4))