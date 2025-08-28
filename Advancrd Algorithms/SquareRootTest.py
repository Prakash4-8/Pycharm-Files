# 6. Write a program for Square root test.
n = int(input('Enter a number: '))
count = 0
is_prime = True
for i in range(1, n - 1):
    temp = ((i * i) % n)
    if temp == 1:
        count += 1
    if count > 2:
        is_prime = False
        break

if is_prime:
    print('The number is prime')
else:
    print('The number is not prime')