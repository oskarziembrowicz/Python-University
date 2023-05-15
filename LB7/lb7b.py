import matplotlib.pyplot as plt
import numpy as np

def julia(z, c):
    for i in range(150):
        z = z**2 + c
        if abs(z) > 2: return i
    return 100

c = -0.8 + 0.156j
X, Y = np.meshgrid(np.linspace(-1.5, 1.5, 700), np.linspace(-1.5, 1.5, 700))

Z = X + Y*1j

color = np.frompyfunc(julia, 2, 1)(Z, c).astype(np.float64)

plt.figure(figsize=(10,10))
plt.contourf(X, Y, color, 200, levels=np.linspace(0, 100, 101), cmap="turbo")
plt.show()


#game of life - automat komórkowy