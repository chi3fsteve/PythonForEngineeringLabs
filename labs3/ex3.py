# Create a graph of the sine and
# cosine functions in the range
# from 0 do 3*PI. Evaluate
# where the function graphs are
# close to each other (distance <
# 0.1) and indicate this using
# points.

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.linspace(0, 3*np.pi, 500)
ax = fig.add_subplot()
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x), 'g')
crossing = np.extract(abs(np.sin(x) - np.cos(x)) < 0.1, x)
print(crossing)
plt.scatter(crossing, np.sin(crossing), 20, 'r')
plt.scatter(crossing, np.cos(crossing), 20, 'r')
plt.ylim(-1.5, 1.5)
plt.xlim(-2, 10)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
plt.show()
