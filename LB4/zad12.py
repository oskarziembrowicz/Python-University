l = [(1, 2, 4), (2, 3), (5,), (3, 4, 5, 6)]
print([i for i in l if sum(i) % 2])