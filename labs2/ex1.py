import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 5)
y1 = np.random.randint(3,9, size=4)
y2 = np.random.randint(3,9, size=4)

plt.plot(x, y1, 'g--o', label='funkcja 1')
plt.plot(x, y2, 'r--^', label='funkcja 2')
plt.xlim(0.5, 4.5)
plt.xticks([1, 2, 3, 4])
plt.xlabel("Parametere X")
plt.ylim(2.5, 8.5)
plt.yticks([3, 4.5, 7, 8])
plt.ylabel("Parameter Y")
plt.legend()
plt.title("Wykres")
plt.show()
