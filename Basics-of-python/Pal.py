def check_pal(n):
    t = n
    if n < 0:
        print(n, 'is not a palindrome number.')
    else:
        rev = 0
        while t > 0:
            rev = rev * 10 + (t % 10)
            t //= 10
        if rev == n:
            print(n, 'is a palindrome number.')
        else:
            print(n, 'is not a palindrome number.')
