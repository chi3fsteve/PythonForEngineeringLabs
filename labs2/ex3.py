import matplotlib.pyplot as plt
import numpy as np
from urllib import request


url = "https://wp.faculty.wmi.amu.edu.pl/bars.txt"
data = request.urlopen(url)
values = []

for i in data:
    values.append(i.decode('utf-8').split(' '))

for j in range(len(values)):
    values[j].pop(-1)

values[0] = list(map(int, values[0]))
values[1] = list(map(float, values[1]))

grouped = list(zip(values[0],values[1]))

c = values[1]
color = plt.get_cmap("copper")

plt.bar(values[0], values[1], color=color(values[1]))

for x, y in zip(values[0],values[1]):
    plt.text(x,y+0.01,y, ha='center')

plt.xticks(range(12))
plt.yticks(np.arange(0,1.1,0.1))
plt.show()
