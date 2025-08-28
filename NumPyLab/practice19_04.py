# datatypes in numpy
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


import numpy as np

arr = np.array([2, 3, 5, 7])
print(arr.dtype)
arr2 = np.array([2, 4, 5], dtype='S')
print(arr2)
print(arr2.dtype)
arr3 = arr2.astype('i')
print(arr3)
print(arr3.dtype)
arr4 = np.array([23.23, 22.34, 43.23, 23.21])
print(arr4.dtype)
arr4c = arr4.astype(bool)
print(arr4c)
print(arr4c.dtype)