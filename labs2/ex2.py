import matplotlib.pyplot as plt
from urllib import request
from matplotlib import cm

url = "https://wp.faculty.wmi.amu.edu.pl/scatter.txt"
data = request.urlopen(url)
values = []

for i in data:
    values.append(i.decode('utf-8').split(' '))

for j in range(len(values)):
    values[j].pop(-1)
    values[j] = list(map(float, values[j]))

print(values)

c = values[1]
color = cm.get_cmap()

ax = plt.axes(polar="true")
ax.scatter(values[0], values[1], s=6, c=c, cmap='jet')
ax.set_ylim(0, 1.4)

plt.show()
