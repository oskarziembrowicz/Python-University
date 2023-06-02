import matplotlib.pyplot as plt
import numpy as np
from time import time
from multiprocessing import Process, Queue

x = np.arange(-2, 1, 0.02)
y = np.arange(-1.5, 1.5, 0.02)
x, y = np.meshgrid(x, y)
z = x + 1j*y    # siatka liczb zespolonych
s = z.shape

def mand(z, a, q):
    t = time()
    z0 = np.copy(z)
    s = z.shape
    res = 255 * np.ones(s)
    for i in range(255):
        res[np.abs(z) > 2] = i
        z = z ** 2 + z0
    # return res
    print("Function: ", time()-t)
    q.put((a,res))

q = Queue()
n = 4
l = [z[:, i*s[1]//n:(i+1)*s[1]//n] for i in range(n)]
p = [Process(target=mand, args=(l[i],i,q)) for i in range(n)]
# l = map(mand, l)
# res = np.hstack(l)

t = time()
for i in p:
    i.start()

print("Program: ", time()-t)

res = sorted([q.get() for _ in range(n)], key=lambda x: x[0])
res = [x[1] for x in res]
res = np.hstack(res)

plt.matshow(res)
plt.show()