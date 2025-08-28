#6. WAP to check whether a number is prime or not.
while True:
    num = int(input('Enter a number :'))
    if num == -1:# to break loop
        break
    flag = True
    if num == 1 or num == 0:
        flag = False
    elif num > 1:
        for i in range(2, (num+2)//2):
            if num % i == 0:
                flag = False
    if flag:
        print(num, 'is a prime number')
    else:
        print(num, 'is not a prime number')
