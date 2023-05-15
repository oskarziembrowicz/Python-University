import matplotlib.pyplot as plt
import numpy as np

def julia(z, c):
    for i in range(100):
        z = z**2 + c
        if abs(z) > 2: return i
    return 0

c = -0.4 + 0.65j
d = 500       #ilość punktów w siatce w jednym kierunku
color = []
x = []
y = []

for i in range(d):
    for j in range(d):
        xi = -2.5 + 3/d * i   #-2.0 + 0.5/d * i
        yi = -1.5 + 3/d * j  #-0.25 + 0.5/d * j
        color.append(julia(0+0*1j, xi+yi*1j))
        x.append(xi)
        y.append(yi)

plt.figure(figsize=(10,10))
plt.scatter(x, y, c=color, s=0.5, cmap="jet")
plt.show()
