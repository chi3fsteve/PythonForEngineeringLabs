import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, sem



mu1, sigma1 = 3.0, 1.0
x = np.random.normal(mu1, sigma1, 100)
mu2, sigma2 = 1.0, 2.0
y = np.random.normal(mu2, sigma2, 100)

fig, axs = plt.subplots(1, 3)
axs[0].hist(x, density=True)
axs[1].hist(y, density=True)

muFit, sigmaFit = norm.fit(x)
print("Missclassification rate of first distribution")
print(abs(muFit-mu1)/mu1, abs(sigmaFit-sigma1)/sigma1)
muFit, sigmaFit = norm.fit(y)
print("Missclassification rate of second distribution")
print(abs(muFit-mu2)/mu2, abs(sigmaFit-sigma2)/sigma2)

left, right = axs[0].get_xlim()
print(left, right)
space = np.linspace(left, right, 50)
muFit, sigmaFit = norm.fit(x)
fitted_data = norm.pdf(space, muFit, sigmaFit)
axs[0].plot(space, fitted_data, 'r')

meanArray100 = []
for i in range(100):
    f = np.random.normal(3.0, 1.0, 100)
    mean = np.mean(f)
    meanArray100.append(mean)
axs[2].hist(meanArray100)
print("Standard error of 100 means:")
print(sem(meanArray100))
meanArray1000 = []
for i in range(1000):
    f = np.random.normal(3.0, 1.0, 100)
    mean = np.mean(f)
    meanArray1000.append(mean)
print("Standard error of 1000 means:")
print(sem(meanArray1000))
plt.show()
