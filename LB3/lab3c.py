cube = lambda x,y : x**y

#print(cube(12, 3))

def f(x):
    return 3*x

l = [2, 5, -1]
#print(list(map(f, l)))      #pozwala przemnożyć każdy element
print(list(map(lambda x:x*3, l)))


def even(x):
    return x%2 == 0

l1 = list(range(1,21))
print(list(filter(even, l1)))
print(list(filter(lambda x:x%2==0, l1)))


from functools import reduce
l2 = ['a', 'b', 'c', 'd', 'e']
def f1(x, y):
    print(x,y)
    return x+y

print(reduce(f1, l2))


n = 30;
print(reduce(lambda x,y:x*y, range(1,n+1)))     #silnia


l3 = [9, 1, 3, 7, 8, 2, 6, 4, 5]
print(sorted(l3, key = lambda i:i%2))       #sortowanie względem klucza

s = ["ola", "pies", "lokomotywa", "wyraz"]
print(sorted(s, key = lambda i:len(i)))