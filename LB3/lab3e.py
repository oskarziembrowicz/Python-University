from functools import reduce
l = [4, 0, 2, 3]    #ma dać 4023
print(int(reduce(lambda x,y: str(x)+str(y), l)))
print(reduce(lambda x,y:x*10+y,l))


w = [1, -2, 3]
x = 2
print(reduce(lambda a,b:a*x+b, w[::-1]))        #x(3x-2)+1