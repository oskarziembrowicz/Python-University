import matplotlib.pyplot as plt
import random

x = [0]
y = [0]

for i in range(100000):
    rand = random.randrange(1, 100)

    if rand <= 85:
        curX = x[-1]
        curY = y[-1]
        x.append(curX * 0.85 + 0.04 * curY)
        y.append(-0.04 * curX + 0.85 * curY + 1.6)
    elif rand <= 92:
        curX = x[-1]
        curY = y[-1]
        x.append(-0.15 * curX + 0.28 * curY)
        y.append(0.26 * curX + 0.24 * curY + 0.44)
    elif rand <= 98:
        curX = x[-1]
        curY = y[-1]
        x.append(0.2 * curX - 0.26 * curY)
        y.append(0.23 * curX + 0.22 * curY + 1.6)
    else:
        curY = y[-1]
        x.append(0)
        y.append(0.16 * curY)

print(plt.plot(x, y, ".", markersize=0.8))
plt.show()

x = [0]
y = [0]

import numpy as np

a = np.array([
    [[0.85, 0.04, 0], [-0.04, 0.85, 1.6]],
    [[-0.15, 0.28, 0], [0.26, 0.24, 0.44]],
    [[0.2, 0.26, 0], [0.23, 0.22, 1.6]],
    [[0, 0, 0], [0, 0.16, 0]]
])

n = 10000

for i in random.choices([0, 1, 2, 3], weights=[85, 7, 7, 1], k=n):
    x.append(a[i][0][0] * x[-1] + a[i][0][1] * y[-1] + a[i][0][2])
    y.append(a[i][1][0] * x[-2] + a[i][1][1] * y[-1] + a[i][1][2])  # [-2] bo x się dodał

plt.figure(figsize=(6, 10))
plt.plot(x, y, marker='.', linewidth=0, markersize=0.5)
plt.show()

