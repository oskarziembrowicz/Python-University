import matplotlib.pyplot as plt
import numpy as np
from time import time

# x = np.arange(-2, 1, 0.01)
# y = np.arange(-1.5, 1.5, 0.01)
# x, y = np.meshgrid(x, y)
# z = x + 1j*y    # siatka liczb zespolonych
# s = z.shape
#
# t = time()
# z0 = np.copy(z)
# res = 255 * np.ones(s)
# for i in range(255):
#     res[np.abs(z) > 2] = i  # dla spełnionego warunku element jest równy i
#     z = z**2 + z0       # wykonuje na całej macierzy
# print(time()-t)
#
# plt.matshow(res)
# plt.show()

a = np.ones((3,3))
b = 2 * np.ones((2, 3))
c = 5 * np.ones((3, 2))

print(np.vstack((a, b)))

print(np.hstack((a, c)))

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

matrix = np.array([[i*j for i in range(1, 21)] for j in range(1, 11)])
print(matrix)


size = matrix.shape
n = 5
len = round(size[1]/n)
# scat = [matrix[:, 0 + len * i:len + len * i] for i in range(round(n))]
scat = [matrix[:, i*len:(i+1)*len] for i in range(round(n))]
print("\nScat:")
print(scat)

