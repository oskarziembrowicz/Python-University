import string

text = "Ala ma kota, psa, chomika i rybki."

# a solution
l = [i for i in text]
print(l)
d1 = dict.fromkeys(l)
print(d1)
d = {i:text.count(i) for i in l}
#print(d)
d2 = dict([[i,text.count(i)] for i in text])
print(d2)

#better solution
d3 = {}
for i in text:
    if i not in d3.keys():
        d3[i] = text.count(i)
print(d3)

#the best solution?
text.lower()
#s = "abcdefghijklmnopqrstuvwxyz, ."
s = string.ascii_lowercase
d4 = {}
for j in s:
    if j in text:
        d4[j] = text.count(j)
print(d4)