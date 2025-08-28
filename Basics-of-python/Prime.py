def check_prime(n):
    flag = True
    if n <= 1:
        print('%d is not a prime number' % n)
    elif n > 1:
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                flag = False
                break
        if flag:
            print('%d is a prime number' % n)
        else:
            print('%d is not a prime number' % n)
