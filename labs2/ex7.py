import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 5)
y1 = np.random.randint(3,9, size=4)
plt.plot(x, y1, 'r-.o', label='funkcja 1')

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5')
plt.grid(which='minor', linestyle=':', linewidth='0.5')

ax = plt.gca()

ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])

plt.show()