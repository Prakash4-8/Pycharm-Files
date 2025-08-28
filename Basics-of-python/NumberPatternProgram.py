#11.
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,6):
        print('{} '.format(j),end='')
    print('')
print('')
#12.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(0,6):
    for j in range(0,i):
        print('{} '.format(j+1),end='')
    print('')
#13.
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
print('')
for i in range(5,0,-1):
    for j in range(0,i):
        print('{} '.format(j+1),end='')
    print('')
print('')
#14.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1,6):
    for j in range(0,i):
        print(i,end=' ')
    print('')
#15.
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
print('')
for i in range(5,0,-1):
    for j in range(0,i):
        print('{} '.format(i),end='')
    print('')