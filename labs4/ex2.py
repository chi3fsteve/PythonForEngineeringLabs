import matplotlib.pyplot as plt
import numpy as np

# 2x1 + 3x2 = 4
# 5x1 + 4x2 = 23
# 0x1 + 5x2 = 18

x1 = np.array(range(-10, 15))
x2 = 4/3 - 2/3*x1
plt.plot(x1, x2)
x2 = 23/4 - 5/4*x1
plt.plot(x1, x2)
x2 = [18/5]*25
plt.plot(x1, x2)
plt.show()

A = np.array([[2, 3], [5, 4], [0, 5]])
a = np.array([[4], [23], [18]])