import matplotlib.pyplot as plt
from urllib import request

url = "https://wp.faculty.wmi.amu.edu.pl/data3.dat"
data = request.urlopen(url)
values = []

for i in data:
    values.append(i.decode('utf-8').split(','))

for j in range(len(values)):
    values[j] = list(map(float, values[j]))

fig = plt.figure(figsize=[8, 4.5])
ax1 = fig.add_subplot()
ax1.boxplot(values)

plt.show()