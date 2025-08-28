#7.
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
for i in range(0,5):
    for j in range(0,5):
        print('* ',end='')
    print('')
#8.
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(0,6):
    for j in range(0,i):
        print('* ',end='')
    print('')
#9.
# * * * * *
# * * * *
# * * *
# * *
# *
print('')
for i in range(5,0,-1):
    for j in range(0,i):
        print('* ',end='')
    print('')
print('')
#10.
# * * *
# * * * * *
# * * *
# * * * * *
# * * *
flag=1
for i in range(0,5):
    if flag == 1:
        for j in range(0,3):
            print('* ',end='')
        flag=0
    elif flag == 0:
        for j in range(0,5):
            print('* ',end='')
            flag=1
    print('')
print('')
