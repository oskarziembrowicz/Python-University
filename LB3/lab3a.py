def kwadrat(x):
    return x**2

def s():
    #print("aaa")
    """to jest test"""

def concat(s1, s2 = "nie ma", s3 = "nic"):
    return s1 + " " + s2 + " " + s3 + "."

def concat1(s1, /, s2, *, s3):
    return s1 + " " + s2 + " " + s3 + "."

#print(concat("Ala", "ma", "chomika"))
#print(concat(s3 = "chomika", s1 = "Ala"))

def add(l = None, element = 'x'):     #lista l działa podobnie do wskaźnika
    if l == None:
        l = []
    l.append(element)
    return l

def f(a, b = None):     #jeśli nie podano arg b, to ma być równy a
    if b == None:
        b = a

def length(x):
    if type(x) in (str, list, tuple, bytes): return len(x)
    elif type(x) in (int, float, complex): return abs(x)
    else: return None

#print(length(123))

def fun(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return 1

#fun('a', 1, [1, 2], 3, 4, c = 5, d = "ala")

def fun1(a, b, *args, **kwargs):
    """ To jest dokumentacja funkcji """
    print(args)
    print(kwargs)
    return 1

#print(fun1.__doc__)     #wywołanie dokumentacji funkcji