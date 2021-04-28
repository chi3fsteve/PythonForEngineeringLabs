import requests
import io
import numpy as np
import matplotlib.pyplot as plt

response = requests.get('https://wp.faculty.wmi.amu.edu.pl/pom_x.npy')
response.raise_for_status()
x = np.load(io.BytesIO(response.content))
response = requests.get('https://wp.faculty.wmi.amu.edu.pl/pom_y.npy')
response.raise_for_status()
y = np.load(io.BytesIO(response.content))

vander1stOrder = np.vander(x, 3)
print(vander1stOrder)

stack = np.stack((x, np.ones(len(x))), axis=1)
m, c = np.linalg.lstsq(stack, y, rcond=None)[0]

plt.plot(x, x*m+c)
plt.scatter(x,y)
plt.show()

vander2ndOrder = np.vander(x, 4)
print(vander2ndOrder)