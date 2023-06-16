# 75790

import numpy as np

# def comparer(primer1, primer2):
#     if not primer1 or not primer2:
#         return -1
#     else:
#         primer2 = np.array(list(primer2[::-1]))
#         p1_tab = np.array(['*'] * (len(primer1) + len(primer2) - 2) + list(primer1))
#         p2_tab = np.array(['*'] * (len(primer1) - 1) + list(primer2))
#         align = []
#         for i in range(len(primer1) + len(primer2) - 1):
#             common = np.array(list(zip(p1_tab[i:], p2_tab)))
#             align.append(
#                 np.count_nonzero(common == ("A", "T")) + np.count_nonzero(common == ("T", "A")) +
#                 np.count_nonzero(common == ("C", "G")) + np.count_nonzero(common == ("G", "C"))
#             )
#         return max(align)

from multiprocessing import Process, Queue

def comparer(primer1, primer2, queue):
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
        # queue.put(max(align))
        return max(align)

import time
file_in =open("primers.txt", 'r')

base = []
print("Scanning...")
for line in file_in:
    base.append(line.split(",")[0])
count = len(base)
base = np.array(base)

q = Queue()
s = 0
start_t = time.time()
primer_1 = base[0]
scat = np.array_split(base, 2000)

for j in range(len(scat)):
    p = [Process(target=comparer, args=(primer_1, base[j*5 + i], q)) for i in range(5)]
    for i in p:
        i.start()
        i.join()
    # primer_2 = base[j]
    # s += comparer(primer_1, primer_2)

s = sum([q.get() for _ in range(len(q))])
end_t = time.time()
print("\t", end_t - start_t)
print(s)