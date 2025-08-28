# 7. WAP to modify the name as follow:
# Input - Prakash chandra mohapatra
# Output - P.C.Mohapatra        [Note how 'chandra' is written as C]
name = input('Enter your name : ')
sur = name.split()
fnam = ''
for i in range(0,len(sur)-1):
    fnam+=sur[i][0].upper()
for i in fnam:
    print(i,'.',sep='',end='')
print(sur[len(sur)-1].upper())