# Create an array of 25 random floating-point
# numbers in the range [0, 100] and set the highest
# element equal to 200 and all numbers smaller
# than 50 equal to 0.

import numpy as np

numbers = np.random.randint(0,101, 25)
numbers[numbers.argmax()] = 200
numbers[numbers < 50] = 0
print(numbers)
