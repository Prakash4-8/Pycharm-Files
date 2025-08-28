# 5. WAP to print the frequency of each element present in the list.
# For example Input- [5, 7, 5, 3, 2, 2, 1, 9, 2, 9,] Output:
# Element      Frequency
# 5                   2
# 7                   1
# 3                   1
# 2                   3
# 1                   1
# 9                   2
list1 = [1, 23, 65, 54, 75, 64, 25, 46, 15, 66, 45, 1, 48, 62, 15, 65, 15]
unique = []
for i in list1:
    if i not in unique:

        unique.append(i)
print('Element Value')
for i in unique:
    count = 0
    for j in list1:
        if j == i:
            count+=1
    print('{}\t\t{}'.format(i,count))


