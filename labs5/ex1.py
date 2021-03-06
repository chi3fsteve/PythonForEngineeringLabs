import requests
import io
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

response = requests.get('https://wp.faculty.wmi.amu.edu.pl/daneX.npy')
response.raise_for_status()
x = np.load(io.BytesIO(response.content))
response = requests.get('https://wp.faculty.wmi.amu.edu.pl/daneY.npy')
response.raise_for_status()
y = np.load(io.BytesIO(response.content))

gridx = np.linspace(min(x), max(x), 100)
gridy = np.linspace(min(y), max(y), 100)

H, xedges, yedges = np.histogram2d(x, y, bins=[gridx, gridy])

ax = plt.subplot(111, sharex=[0,100], sharey=[0,100])
X, Y = np.meshgrid(xedges, yedges)
ax.pcolormesh(X, Y, H)


for pair in combinations(X,2):
    assert np.array_equal(pair[0],pair[1])


plt.show()


