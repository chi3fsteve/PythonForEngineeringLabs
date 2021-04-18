# Create a matrix 9x9 of random numbers (int32) in
# the range of -100 to 100. Using this matrix create
# an array that only contains the even elements
# sorted in ascending order

import numpy as np

mx = np.random.randint(-100, 101, [9, 9], dtype='int32')
ar = np.sort(mx[mx % 2 == 0])

print(mx)
print(ar)
