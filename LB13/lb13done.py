from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def julia(z, c):
    for i in range(150):
        z = z**2 + c
        if abs(z) > 2: return i
    return 100

x, y = np.meshgrid(np.linspace(-1.5, 1.5, 700), np.linspace(-1.5, 1.5, 700))
z = x+1j*y
s = z.shape

fig = plt.figure(figsize=(10, 10))
z0 = -0.8 + 0.156j
res = 255*np.ones(s)
w = plt.imshow(res, vmin=0, vmax=255, cmap='binary')

def anim(i):
    global z
    res[np.abs(z) > 2] = i
    z = (res == 255)*(z**2+z0)
    w.set_array(res)

a = FuncAnimation(fig, anim, frames=256, interval=40, repeat=False)
plt.show()