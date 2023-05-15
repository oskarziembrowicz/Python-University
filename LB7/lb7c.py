import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-np.pi/2, np.pi/2, 100)
y = np.linspace(-np.pi/2, np.pi/2, 100)

X, Y = np.meshgrid(x, y)

Z = np.sin(2*X )+ np.cos(2*Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="jet")
plt.show()