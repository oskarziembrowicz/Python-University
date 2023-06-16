import numpy as np

def comparer(primer1, primer2):
    if not primer1 or not primer2:
        return -1
    else:
        primer2 = primer2[::-1]
        p1_tab = '*' * (len(primer1 + primer2) - 2) + primer1
        p2_tab = '*' * (len(primer1) - 1) + primer2
        align = []
        for i in range(len(primer1 + primer2) - 1):
            common = list(zip(p1_tab[i:], p2_tab))
            align.append(
                common.count(("A", "T")) + common.count(("T", "A")) +
                common.count(("C", "G")) + common.count(("G", "C"))
            )
        return max(align)

import time
file_in = open("primers.txt", 'r')
base = []
print("Scanning...")
for line in file_in:
    base.append(line.split(",")[0])
count = len(base)
s = 0

start_t = time.time()
primer_1 = base[0]
for j in range(count):
    primer_2 = base[j]
    s += comparer(primer_1, primer_2)
end_t = time.time()
print("\t", end_t - start_t)
print(s)


