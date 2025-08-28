def check_spec(n):
    t = n
    if n < 1:
        print(n, 'is not a special number.')
    if n // 10 == 0:
        print(n, 'is not a special number.')
    else:
        def fact(n):
            fac = 1
            for i in range(1, n + 1):
                fac *= i
            return fac

        sum = 0
        while t > 0:
            sum += fact(t % 10)
            t //= 10
        if sum == n:
            print(n, 'is a special number.')
        else:
            print(n, 'is not a special number.')
