import matplotlib.pyplot as plt
import numpy as np

p = np.arange(0.9, 1.1, 0.01)
c = []

for x in p:
    A = np.array([[1, np.sqrt(x)], [1, 1 / np.sqrt(x)]])
    cond = np.linalg.cond(A)
    c.append(cond)
np_cond = np.array(c)

plt.plot(p,c)
plt.show()