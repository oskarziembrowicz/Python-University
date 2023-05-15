def iloczyn_skalarny(l1, l2):
    return sum(map(lambda x,y:x*y, l1, l2))

a = [1, 2, 3, 4, 5]
b = [-2, 4, 2, -1, 3]
print(iloczyn_skalarny(a, b))
print(sum(map(lambda i:i[0]*i[1], zip(a, b))))