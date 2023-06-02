import matplotlib.pyplot as plt
import numpy as np
from time import time

x = np.arange(-2, 1, 0.01)
y = np.arange(-1.5, 1.5, 0.01)
x, y = np.meshgrid(x, y)
z = x + 1j*y    # siatka liczb zespolonych
s = z.shape

t = time()
z0 = np.copy(z)
res = 255 * np.ones(s)
for i in range(255):
    res[np.abs(z) > 2] = i  # dla spełnionego warunku element jest równy i
    z = z**2 + z0       # wykonuje na całej macierzy
print(time()-t)

plt.matshow(res)
plt.show()