d = {"a":1, "b":2, "c":3}
d1 = dict((("e",4),("f",5)))

print(d1)
print(d.get("c"))

d["a"] = 10

d.update(d1)    #dodaj do słownika

print(d)

d["d"] = 7

print(d)

print("g" in d.keys())
print(list(d.keys()))
print(list(d.values()))

del d["a"]
print(d)