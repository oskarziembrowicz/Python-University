#l = [i**2 for i in range(1,21) if i%2 == 1]

#l = [[i**j for i in range(1,11)]  for j in range(1, 11)]

#print(l)

#l1 = [i/3 for i in l]

#print(l1)

l2 = ["x" if i%2 == 0 else "o" for i in range (10)]
#print(l2)

print("_".join("x"*i for i in range(4)))

k = (i**2 for i in range(10))
print(type(k))
for i in k:
    print(i)