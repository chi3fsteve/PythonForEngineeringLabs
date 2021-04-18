import matplotlib.pyplot as plt
from urllib import request

url = "https://wp.faculty.wmi.amu.edu.pl/data2.dat"
data = request.urlopen(url)
values = []

for i in data:
    j=i.rstrip()
    values.append(j.decode('utf-8'))
values = list(map(float, values))
print(values)
# plt.hist(values,bins=100, cumulative=True)
fig, (ax1, ax2) = plt.subplots(2,1)
ax1.hist(values, bins=100, cumulative=True)
ax2.hist(values, bins=100)
plt.show()