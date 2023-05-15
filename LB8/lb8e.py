# tworzymy kwadratowa macierz n X n podzieloną na klatki wypełnoną wartościami 0,1
# na jej podstawie generujemy drugą macierz na podstawie:
# stawiamy 1 na postawie jej otaoczenia (3X3) zależnie od tego ile 1 naliczę robię co innego
# dla 0 i jego 3 sąsiadów to stawiamy 1
# dla 1 i jego 2,3 sąsiadów to stawiamy 1
# pozostałe stawiamy 0

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

grid_size = 100
Z = np.random.rand(grid_size, grid_size)
Z[Z>0.5] = 1
Z[Z!=1] = 0

def anim(frame, Z, grid_size):
    newZ = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        for j in range(grid_size):
            sum = Z[i - 1:i + 2, j - 1:j + 2].sum() - Z[i, j]
            if (Z[i,j] == 1 and (sum == 2 or sum == 3) or (Z[i,j] == 0 and sum == 3)):
                newZ[i,j] = 1
    Z[:] = newZ[:]
    mat.set_data(Z)
    return mat

fig, ax = plt.subplots()
mat = ax.matshow(Z, cmap="plasma")
anim = FuncAnimation(fig, anim, frames=200, fargs=(Z, grid_size), interval=5)
plt.show()