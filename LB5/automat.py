rule = 90
n = 20
k = 10

predict = ["***","**_","*_*","*__","_**","_*_","__*","___"]
prerule = ["_"*int(i=='0')+"*"*int(i=='1') for i in str(bin(rule))[2:].zfill(8)]
automat = {key: value for (key, value) in zip(predict, prerule)}

from random import random

line = ""
for i in range(0, n):
    if random() < 0.5:
        line += '_'
    else:
        line += '*'
print(line)

for i in range(0, k-1):
    newLine = "_"
    for j in range(0, n-2):
        newLine += automat[line[j:3+j]]
    newLine += "_"
    #newLine = "".join(automat[line[j-1]+line[j]+line[j+1] for j in range(0, n)]*(j<n))

    print(newLine)
    line = newLine

#automat[line[j-1]+cells[j]+cells[j+1] for i in range(0, n)]
