from urllib import request
import numpy as np

url = "https://wp.faculty.wmi.amu.edu.pl/populacje.txt"
data = request.urlopen(url)
values = []

for i in data:
    values.append(i.decode('utf-8').split(' '))
values[0].pop(0)
val = []
for i in values:
    j = list(i[0].rstrip().split('\t'))
    val.append(j)
for i in val[1:]:
    i[0] = int(i[0])
    i[1] = float(i[1])
    i[2] = float(i[2])
    i[3] = int(i[3])
val = np.array(val[1:])
print(val)

maximum1 = np.amax(val, axis=0)
print(maximum1)
