all_items = [1, 2, 3, 4, 5]
condition = lambda x: x < 3

not_all_items = not all(condition(x) for x in all_items)
some_items = any(not condition(x) for x in all_items)

print(not_all_items == some_items)

A = [True, False]
print(not all(A) == any(not i for i in A))