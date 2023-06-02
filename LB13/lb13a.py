# Wersja I - najwolniejsza
# import mplcatppuccin
import matplotlib as mpl
import matplotlib.pyplot as plt
from time import time
import numpy as np

def f(z):
    z0 = z
    for i in range (255):
        if abs(z) > 2:
            return i
        z = z**2 + z0
    return 255

x = np.arange ( -2 ,1.01 ,.01)
y = np.arange ( -1.5 ,1.51 ,.01)
x,y = np.meshgrid(x,y)
z = x + 1j*y
s = z.shape
t = time()
res = np.array([[f(z[i, j]) for j in range(s[1])] for i in range(s[0])])
print(time()-t)
plt.imshow(res)
plt.show()