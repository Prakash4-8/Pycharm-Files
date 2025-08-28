import numpy as np
from numpy.linalg import norm

w1 = [2, 9, 4]
w2= [1, 5, 6]
comsine = np.dot(w1, w2)/(norm(w1)*norm(w2))
print(comsine)