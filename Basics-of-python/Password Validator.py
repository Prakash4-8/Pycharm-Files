# 3. Program to check whether the user have a enter a valid password or not.
# A valid password must contains
# At least 8 characters (maximum 20)
# At least one uppercase letter
# At least one lowercase letter
# At least one number
# At least one special symbol. Only these are valid special symbol: ! @ # $ % ^ & * ( )
password = input('Enter a password : ')
flg = False
flg1 = False
flg2 = False
flg3 = False
flg4 = False
if 8 <= len(password) <= 20:
    for i in password:
        if i.isupper():
            flg1 = True
        if i.islower():
            flg2 = True
        if i.isnumeric():
            flg3 = True
        if i in ['!', '@', '#', '$', '%', '^', '&', '*', ')', '(']:
            flg4 = True
        if flg1 and flg2 and flg3 and flg4:
            flg = True
            break
if flg:
    print(password, 'is valid password')
else:
    print(password, 'is not valid password')