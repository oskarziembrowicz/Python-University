import math
print(math.sin(math.pi/3))

import random
print(random.random())
print(random.randint(1,10))
print(random.choices("ACTG", weights=(3,1,1,3), k=10))
for i in random.choices("ACTG", weights=(3,1,1,3), k=10):
    print(i)