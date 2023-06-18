rule = 90
n = 21
k = 10

predict = ["***","**_","*_*","*__","_**","_*_","__*","___"]
prerule = ["_"*int(i=='0')+"*"*int(i=='1') for i in str(bin(rule))[2:].zfill(8)]
automat = {key: value for (key, value) in zip(predict, prerule)}

# for random start values
from random import random
# line = ""
# for i in range(n):
#     if random() < 0.5:
#         line += '_'
#     else:
#         line += '*'


# to a get nice triangle
if n % 2 == 0:
    line = (n-2)//2 * '_' + 2 * '*' + (n-2)//2 * '_'
else:
    line = (n-1)//2 * '_' + '*' + (n-1)//2 * '_'

print(line)

for i in range(0, k-1):
    newLine = ""
    newLine += automat[line[-1]+line[0]+line[1]]
    for j in range(1, n-1):
        newLine += automat[line[j-1:j+2]]
    newLine += automat[line[-2]+line[-1]+line[0]]
    print(newLine)
    line = newLine

