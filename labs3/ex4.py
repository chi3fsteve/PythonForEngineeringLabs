import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

args = np.random.uniform(low=-1.0, high=1.0, size=(2, 500))
print(args)

fig = plt.figure()
ax = fig.add_subplot(projection='polar')

color = cm.get_cmap()

# smart indexing
for x, y in zip(args[0], args[1]):
    if -1 < x < -0.5 or 0 < x < 0.5:
        ax.scatter(x*2*np.pi, y, c=args[0], cmap="jet")
    else:
        ax.scatter(x*2*np.pi, y, c=args[0], cmap="terrain")
plt.show()