import math
import numpy as np
import matplotlib as mpl
mpl.use('Qt5Agg')
import matplotlib.pyplot as plt
from numpy.linalg import inv


mu, sigma = 1, 1
original = np.random.normal(mu, sigma, (2, 1000))

fig1 = plt.figure(1)
plt.title('Original matrix')
plt.scatter(original[0], original[1])

zipMatrix = list(zip(original[0], original[1]))

'''Transformation along the x-axis via a scaling matrix that stretches the
point cloud of data by a factor 3'''

transformationMatrix3x = np.array([[3, 0], [0, 1]])
dotProduct = np.array(zipMatrix).dot(transformationMatrix3x)
a, b = list(zip(*dotProduct))

fig2 = plt.figure(2)
plt.title('Matrix stretched on x axis by a factor 3')
plt.scatter(a, b)

'''Rotate the point cloud by 45 degrees “up” using a rotation matrix.'''

rotationMatrix = np.array([[math.cos(-45), -math.sin(-45)],
                           [math.sin(-45), math.cos(-45)]])
rotationProduct = np.array(zipMatrix).dot(rotationMatrix)
a, b = list(zip(*rotationProduct))

fig3 = plt.figure(3)
plt.title('Matrix rotated by 45deg')
plt.scatter(a, b)

'''How can you apply both transformations (scaling and rotating) in a single
transformation?'''

newTransformationMatrix = transformationMatrix3x.dot(rotationMatrix)
combinedMatrix = np.array(zipMatrix).dot(newTransformationMatrix)
a, b = list(zip(*combinedMatrix))

fig4 = plt.figure(4)
plt.title('Matrix rotated by 45deg and stretched on x axis by a factor 3')
plt.scatter(a, b)

U, S, V = np.linalg.svd(list(zip(*combinedMatrix)), full_matrices=False)
print(U)
print(S)
print(V)


uf = zipMatrix@inv(U)
a, b = list(zip(*uf))
fig5 = plt.figure(5)
plt.title('Matrix rotated by 45deg and stretched on x axis by a factor 3')
plt.scatter(a, b)

plt.show()