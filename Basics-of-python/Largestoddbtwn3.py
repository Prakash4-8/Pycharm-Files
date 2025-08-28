# write a program that examines  three variables _x,y,and z__ and prints the largest odd number among them. If none
# of them are odd then, it should print a message to that effect.
#x,y,z =10,13,18
max=0
x=int(input('Enter 1st number : '))
if x % 2 !=0:
    if max<x :
        max=x
y=int(input('Enter 2nd number : '))
if y % 2 !=0:
    if max<y :
        max = y
z = int(input('Enter 3rd number : '))
if z % 2 !=0:
    if max < z :
        max = z
if max == 0:
    print('No odd number')
else:
    print('The largest odd number is ',max)

# if _x % 2 == 1 and _x > y and _x > z__:
#     print('_x is greatest odd number ')
# elif y % 2 == 1 and y > _x and y > z__:
#     print('y is greatest odd number ')
# elif z__ % 2 ==1 and z__ > _x and z__ > y:
#     print('z__ is the greatest odd number ')
# elif _x % 2 == 1:
#     print('_x is greatest odd number ')
# elif y % 2 ==1 :
#     print('y is greatest odd number ')
# elif z__ % 2 == 1:
#     print('z__ is the greatest odd number ')
# else :
#     print('No odd number is there ')
