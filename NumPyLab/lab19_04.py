import numpy as np
a1 = np.array(10) # array index 0 to 9
print(a1)
print(a1.shape)
a2 = np.arange(0, 10, 2)
print(a2)
print(a2.shape)
a3 = np.zeros(5)
print(a3)
print(a3.shape)
a4 = np.full((2, 3),2)
print(a4)
a5 = np.eye(4)
print(a5)
a6 = np.random.random((2, 4))
print(a6)


#  list
lis1 = [7,34, 64, 24]
r1 = np.array(lis1)
print(r1)

# flags
x = np.array([1, 2, 3, 4, 5])
print(x.flags)

a = np.array([1, 2, 3, 4, 5], dtype=complex, order = 'c')
print(a)
num = np.arange(20)
print(num)
odd_num = num[num % 2 == 1]
print(odd_num)