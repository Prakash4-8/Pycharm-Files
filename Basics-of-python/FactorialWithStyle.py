#5. WAP to print factorial of a number. The output should be like this: 5! = 5 X 4 X 3 X 2 X 1 = 120
num=int(input('Enter a number :'))
print('{0}! ='.format(num),num,end='')
fact=1
while num!=0:
        fact=fact*num
        num-=1
        print(' X',num,end='')
print(' =',fact)