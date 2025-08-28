# 6. WAP to print only duplicate elements in the list.
# For example Input- [5, 7, 5, 3, 2, 2, 1, 9, 2, 9,] Output: 5,2,9
list1 = [52, 65, 54, 2, 5, 2, 5, 6, 5, 4, 58, 56, 5, 84, 6, 56, 8, 4, 6, 4, 46, 78, 4, 2, 4, 5, 7 ]
unique =[]
for i in list1:
    if i not in unique:
        unique.append(i)
print(unique)
