# Write a program to check a number is in binary format or not?
num = input('Eneter a number : ')
flg = True
for i in num:
    if i not in ['0', '1']:
        print(num, 'is not a binary number ')
        flg = False
        break
    else:
        continue
if flg:
    print(num, 'is a binary number')