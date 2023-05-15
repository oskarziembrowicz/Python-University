import numpy as np

l1 = np.linspace(0,1,6)
l2 = np.arange(0, 1, 0.2)
print(l1)
print(l2)

import matplotlib.pyplot as plt

x = [i for i in range(0,11)]
y = [i**2 for i in x]
print(plt.plot(x,y))

import math
pi = math.pi
x = [-pi+2*pi/100*i for i in range(100)]
y = [math.cos(i) for i in x]
print(plt.plot(x,y, 0, '.'))

x = np.linspace(-pi, pi, 100)
print(plt.plot(x,np.cos(x), label = "cos(x)"))
plt.legend()
plt.show()

x = np.linspace(0,1,51)
for i in np.linspace(0.25,2,8):
    plt.plot(x, x**i, label = "x**"+str(i))
plt.legend()
plt.show()