# Auto Associative Memory
import numpy as np

a1 = np.array([[-1, 1, -1, 1]])
a2 = np.array([[1, 1, 1, -1]])
a3 = np.array([[-1, -1, -1, 1]])

# find the transpose
a1_trans = np.transpose(a1)
a2_trans = np.transpose(a2)
a3_trans = np.transpose(a3)

# Connection matrix
C = a1 * a1_trans + a2 * a2_trans + a3 * a3_trans
print(C)

# recall the pattern
alpha = np.dot(C, a2_trans)
print(alpha)
alpha = np.transpose(alpha)

for i in range(1):
    for j in range(4):
        if alpha[0][j] > 0:
            alpha[0][j] = 1
        else:
            alpha[0][j] = -1

print(alpha)

if np.array_equal(alpha, a2):
    print("pattern is recalled")
else:
    print("pattern is not recalled")