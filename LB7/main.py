import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
y = x**2

plt.scatter(x, y, c=y, s=100, cmap="jet")
plt.show()