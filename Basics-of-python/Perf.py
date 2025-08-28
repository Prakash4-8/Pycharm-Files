def check_perf(n):
    if n <= 0:
        print(n, 'is not a perfect number')
    else:
        sum, j = 0, (n // 2) + 1
        for i in range(1, j):
            if (n % i == 0):
                sum += i
        if sum == n:
            print(n, 'is a perfect number')
        else:
            print(n, 'is not a perfect number')
