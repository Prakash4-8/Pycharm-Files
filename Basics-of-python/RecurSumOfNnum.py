#3. Program to find the sum of the first N natural number using recursion
def sum_n(num):
    if num == 0:
        return 0
    else:
        return num + sum_n(num - 1)
print(sum_n(5))