x = 5
y = 0
try:
    print(x/y)
except ZeroDivisionError:
    print(x/(y+1))
finally:
    print("Nicely done")

x2 = input()
try:
    print(10/x2)
except TypeError:
    try:
        print(10/int(x2))
    except ValueError:
        print("This is not a number")