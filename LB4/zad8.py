l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# l1 = [x*2 if x%2 == 0 else x for x in l1 if x%3 != 0]
l1 = list(map(lambda x: x*2 if x%2 == 0 else x, filter(lambda x: x%3 != 0, l1)))
print(l1)