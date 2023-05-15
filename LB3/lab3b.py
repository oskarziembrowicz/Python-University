
i = 4
def f(x):
    global i
    i = i + 2
    return x**i

print(f(5))
print(i)