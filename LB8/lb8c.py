import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()    #rysunek
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
scat = ax.plot(x,y)[0]

# funkcja do modyfikacji wykersu:
def anima(frame,x,y):
    y[:-1] = y[1:]
    y[-1] = np.sin(2*np.pi*frame/100)
    scat.set_data([x,y])

animation = FuncAnimation(fig, anima, frames=100,interval=10)
plt.show()