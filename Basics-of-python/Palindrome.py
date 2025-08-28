
def palindrome(string):
    if type(string) == int:
        temp = string
        rev = 0
        while string != 0:
            rem = string % 10
            rev = rev * 10 + rem
            string //= 10
        if rev == temp:
            flag = True
        else:
            flag = False
        return flag
    elif type(string) == str:
        name2 = ''
        name2 = name2.join(reversed(string.casefold()))
        if string == name2:
            flag = True
        else:
            flag = False
        return flag
