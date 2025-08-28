# reverse a integer
import math

var1 = int(input('Enter an integer : '))


def reverse(var2):
    newvar = 0
    while var2 != 0:
        newvar = newvar * 10 + var2 % 10
        var2 = var2 // 10
    return newvar


# print(reverse(var1))
# to check number is armstrong or not
def length(var2):
    count = 0
    while var2 != 0:
        count += 1
        var2 //= 10
    return count


def armstrong(var2):
    len = length(var2)
    temp = var2
    newnum = 0
    while var2 != 0:
        rem = var2 % 10
        newnum = math.pow(rem, len) + newnum
        var2 //= 10
    if temp == newnum:
        return True
    else:
        return False


# print(armstrong(var1))

# prime number

def prime(var2):
    flag = True
    for i in range(2, var2 // 2 + 1):
        if var2 % i == 0:
            flag = False
            break
    return flag


# print(prime(var1))

# fibonacci series using iteration
def fibonacci_itr(var2):
    print('0\n1')
    n1 = 0
    n2 = 1
    for i in range(var2 - 2):
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3


# fibonacci_itr(var1)


# fibonacci series using recursion

def fibonacci_rec(var2):
    if var2 == 0:
        return 0
    elif var2 == 1:
        return 1
    else:
        return fibonacci_rec(var2 - 1) + fibonacci_rec(var2 - 2)

    # for i in range(var1):
    print(fibonacci_rec(i))


# palindrome number using iterative method
def palindrome_ite(var2):
    var3 = reverse(var2)
    if var2 == var3:
        return True
    else:
        return False


# print(palindrome_ite(var1))
def palindrome_rec(var2):
    len = length(var2)


def reverse_rec(var2):
        len = length(var2)
        print(len)
        if var2 == 0:
            return 0
        else:
            return var2%10*pow(10,len-1) + reverse_rec(var2//10)
print(reverse_rec(var1))