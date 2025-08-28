# rank 2 array
import numpy as np
a1 = np.array([[1, 2, 3], [4, 5, 6]]) # 2d array
a2 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
print(a1, a2)
# slicing
b1 = a1[1:3, :3]
print(b1)
b2 = a1[-2:, -2:]
print(b2)
b3 = a1[1:, 2:]
print(b3)
b4 = a1[2:, :]
print(b4)
print(b4.shape)
b4 = b4.reshape(-1)
print(b4)
x1 = np.array([[1, 2], [4, 6]])
y1 = np.array([[7, 8], [3, 4]])
print(x1 + y1)
print(x1 - y1)
print(x1 * y1)
print(x1 / y1)
pea = np.dot(x1, y1,)
print(pea)
# cumulative sum
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('original array', a)
print(a.cumsum())
print(a.cumsum(axis=0)) # axis 1
# array sort
age = np.array([10, 83, 73, 83, 48, 82])
sort_age = np.sort(age)
print('Original array', age)
print('Sorted array', sort_age)
# copy by view
#  shallow copy
# copy by response

a1 = np.array([5, 7, 9, 11, 13])
a2 = a1.view()
print(a2)


# copy by value

c1 = [[1, 2, 3], [4, 5, 6]]
a1 = np.array(c1)
a2 = a1.copy()
print(a2)
