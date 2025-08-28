#3. WAP to check whether a number is Armstrong or not for three digits number only
num=int(input('Enter any three digit number :'))
temp=num
sum=0
while num != 0:
    rem=num % 10
    sum=rem*rem*rem+sum
    num=num//10
if temp==sum:
    print('This is a Armstrong number')
else:
    print('This is not a Armstrong number')