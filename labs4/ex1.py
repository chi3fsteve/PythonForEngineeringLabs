# 2x1+3x2=4
# 5x1+4x2=23

import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as sp

x2 = np.array(range(-10, 10))
x1 = 2 - 3/2*x2
plt.plot(x1, x2)
x1 = 23/5 - 4/5*x2
plt.plot(x1, x2)

A = np.array([[2, 3], [5, 4]])
a = np.array([[4], [23]])
X = np.append(A, a, axis=1)

x1, x2 = np.linalg.solve(A, a)
print("x1: " + str(x1)+"\nx2: " + str(x2))
print("Rank of this matrix is: "+str(np.linalg.matrix_rank(X)))
print("Conditioning number of this matrix is: "+str(np.linalg.cond(X)))
print(X)

p, l, u = sp.lu(A)
print("Permutation matrix")
print(p)
print("Lower triangular matrix")
print(l)
print("Upper triangular matrix")
print(u)
plt.show()

