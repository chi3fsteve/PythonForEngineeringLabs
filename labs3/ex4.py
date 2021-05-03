import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

args = np.random.uniform(low=-1.0, high=1.0, size=(2, 500))
print(args)

fig = plt.figure()
ax = fig.add_subplot(projection='polar')

color = cm.get_cmap()

jetcmapx = []
jetcmapy = []
terraincmapx = []
terraincmapy = []
# smart indexing
for x, y in zip(args[0], args[1]):
    if 0 < x < 1:
        jetcmapx.append(x*np.pi)
        jetcmapy.append(y)
    else:
        terraincmapx.append(x*np.pi)
        terraincmapy.append(y)
jetcmapx = np.array(jetcmapx)
terraincmapx = np.array(terraincmapx)
ax.scatter(jetcmapx, jetcmapy, c=jetcmapx, cmap="jet")
ax.scatter(terraincmapx, terraincmapy, c=terraincmapx, cmap="terrain")

plt.show()