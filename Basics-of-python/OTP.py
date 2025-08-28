#16. WAP to generate OTP (One Time Code) of 4-digit number only.
import random
num = int(input('Enter number of digit OTP you want : '))
min = pow(10, num-1)
max = pow(10,num)-1
print(random.randrange(min,max))