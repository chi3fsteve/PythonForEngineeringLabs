import numpy as np
import matplotlib.pyplot as plt
from urllib import request

url = 'https://wp.faculty.wmi.amu.edu.pl/PCAdata.txt'
data = request.urlopen(url)
values = []
for i in data:
    values.append(i.decode('utf-8').split(' '))
values.pop(0)
for j in range(len(values)):
    values[j] = list(map(float, values[j]))
print(values)

petalLength = values[0]
sepalLength = values[1]
sepalWidth = values[2]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(petalLength, sepalLength, sepalWidth)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Length')
ax.set_zlabel('Sepal Width')


covPlenSlen = np.cov(petalLength, sepalLength)
covPlenSwdth = np.cov(petalLength, sepalWidth)
covSlenSwdth = np.cov(sepalLength, sepalWidth)

print("Covariance matrix of petal length and sepal length:")
print(covPlenSlen)

print("Covariance matrix of petal length and sepal width:")
print(covPlenSwdth)

print("Covariance matrix of sepal length and sepal width:")
print(covSlenSwdth)

print("Covariance matrix of petal length and sepal length:")
print(np.corrcoef(petalLength, sepalLength))
print("Correlation matrix of petal length and sepal width:")
print(np.corrcoef(petalLength, sepalWidth))
print("Correlation matrix of sepal length and sepal width:")
print(np.corrcoef(sepalLength, sepalWidth))
print("Mean of petal length:")
print(np.mean(petalLength))
print("Mean of sepal length:")
print(np.mean(sepalLength))
print("Mean of sepal width:")
print(np.mean(sepalWidth))

plt.show()