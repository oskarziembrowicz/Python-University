# def cut_touple(x):
#     y = list(x)
#     while len(y) > 2:
#         y.pop()
#     x = tuple(y)

l1 = [(1, 2, 4), (2, 3), (5,), (3, 4, 5, 6)]

# print([type(x) for x in l1])

# l1 = list(filter(lambda x: len(x) >= 2, l1))
# l1 = [cut_touple(x) if len(x) > 2 else x for x in l1]
# l1 = [touple()]

l1 = [tuple(i[:2]) for i in l1 if len[i] > 1]

print(l1)