# 2x1+3x2=4
# 5x1+4x2=23

import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as sp

x1 = np.array(range(0, 20))
x2 = 4/3 - 2/3*x1
plt.plot(x1, x2)
x2 = 23/4 - 5/4*x1
plt.plot(x1, x2)

A = np.array([[2, 3], [5, 4]])
a = np.array([[4], [23]])

x1, x2 = np.linalg.solve(A, a)

print("x1: " + str(x1)+"\nx2: " + str(x2))
print("Rank of this matrix is: "+str(np.linalg.matrix_rank(A)))
print("Conditioning number of this matrix is: "+str(np.linalg.cond(A)))

p, l, u = sp.lu(A)
print("Permutation matrix")
print(p)
print("Lower triangular matrix")
print(l)
print("Upper triangular matrix")
print(u)
plt.show()

