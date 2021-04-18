import matplotlib.pyplot as plt
import numpy as np
from urllib import request
from matplotlib import cm
url = "https://wp.faculty.wmi.amu.edu.pl/pie.txt"
data = request.urlopen(url)
values = []

for i in data:
    values=i.decode('utf-8').split(' ')
values.pop(-1)
values = list(map(float, values))
spaces = (0.1,0.03,0.03,0.03,0.03)
plt.pie(values, colors=cm.terrain(np.arange(0.0, 1.0, 0.2)), explode=spaces)
plt.show()