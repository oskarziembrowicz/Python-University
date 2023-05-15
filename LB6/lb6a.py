from time import time

xin = range(10**6)
xout = []
t = time()
for i in xin:
    xout.append(i**2)
print(time()-t)

t = time()
xout = [i**2 for i in xin]
print(time()-t)

t = time()
xout = list(map(lambda i:i**2, xin))
print(time()-t)

t = time()
xout = list(map((2).__rpow__, xin))
print(time()-t)
# (2).__add__(3)
# (2).__pow__(3)
# (2).__rpov__(3)

import numpy as np

t=time()
xin = np.arange(10**6)
xout = xin**2
print(time()-t)

import numpy as np

t=time()
xin = np.arange(10**6)
xout = xin**2
print(time()-t)