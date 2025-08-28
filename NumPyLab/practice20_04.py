from functools import reduce

import numpy as np

# Write a Python program to create a 3×3 matrix with values ranging from 2 to 10.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 20, 30, 45, 30])
print('max = ', x.max(), 'min = ', x.min(), 'mean = ', x.mean(), 'var = ', x.var())

# multiply all the values in the list
list1 = [1, 3, 4]
list2 = [3, 4, 5]
result1 = np.prod(list1)
result2 = np.prod(list2)
print(result1)
print(result2)
# or
result1or = reduce((lambda a, b: a * b), list1)
result2or = reduce((lambda a, b: a * b), list2)
print(result1or)
print(result2or)

# Write a Python program to create a 3×3 matrix
x = np.arange(2, 11).reshape(3, 3)
print(x)

# program to reverse an array
x = np.arange(0, 15)
print('Original array\n', x)
x = x[-1::-1]
print(x)

# program to append values at the end of an array

x = [[100, 200, 300], [23, 28, 29]]
print('Original Array', x)
x = np.append(x, [[100, 200, 39], [94, 292, 345]])
print(x)

x1 = np.array([2, 4])
y1 = np.array([4, 2])
print(np.dot(x1, y1))
# to find unique element of an element
print(np.unique(x))

# print array elements one by one without using function
print('\n Printing Array')
arr4 = np.array([[29, 29, 29, 12, 93], [28, 92, 92]])
for i in arr4:
    print(i)

arr_single = np.array([[1, 2, 3, 4]])
for i in range(len(arr_single)):
    print(arr_single[i], end= " ")
