from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5,10,100000)
y = np.random.normal(5,10,100000)
plt.subplot(121)
counts,xbins,ybins,image = plt.hist2d(x,y,bins=100
                                      ,norm=LogNorm()
                                      , cmap = plt.cm.rainbow)
plt.colorbar()
plt.subplot(122)
plt.contour(counts.transpose(), extent=[xbins[0],xbins[-1],ybins[0],ybins[-1]],
    linewidths=3, cmap=plt.cm.rainbow, levels = [1,5,10,25,50,70,80,100])
print(len(x))

plt.show()

