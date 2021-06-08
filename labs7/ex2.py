import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
X = np.linspace(-10, 20, 20)
Y = np.linspace(-10, 20, 20)
X, Y = np.meshgrid(X, Y)
dxdt = (1.3**X)*(1-Y/20)
dt = np.ones(X.shape)
dx = dxdt * dt

f1 = plt.figure(1)
plt.streamplot(X, Y, dt, dx)
f2 = plt.figure(2)
plt.quiver(X, Y, dt, dx, headwidth=2.0, angles='xy', scale=25.)


plt.show()