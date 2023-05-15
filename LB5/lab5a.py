s = "%d %s o masie %f kilograma\nw notacji wykladniczej %e kilograma"
dane = (2, "samochody", 234.5765566, 234.5765566)
print(s % dane)
print("*%10s*" % "Hello")
print("*%-10s*" % "Hello")
print("|%-12.4f|" % 23.2344645754742)

s2 = "{1} {0} i {zwierzeta[1]}"
print(s2.format("koty", 2, zwierzeta = ["psy", "myszy"]))

print("|{0:_^12.4}|".format("Hello"))

print("|{0:_^12.3f}|".format(2.43654646))

x = 2
print(f"dlugosc wynosi {x}")
print(f"pole wynosi {x**2}")
print(f"pole wynosi {(x2 := x**3)}")
print(x2)

pi = 3.141594374267
print(f"{pi:*>10.3f}")