import io

f = open("plik.txt")
file = f.read()
print(file)

print(f.tell())
f.seek(0)
print(f.read())

f.seek(0)
print(f.readline())

f.seek(0)
print(f.readlines())

f.seek(0)
for i in f:
    print(i, end='')

f.close()

# try:
#     f = open("plik.txt", "w")
#     file = f.read()
# except FileNotFoundError:
#     print("\nNo such file exists")
# except io.UnsupportedOperation:
#     print("\nCannot read from this file")
# finally:
#     f.close()

with open("plik.txt") as f:
    print(f.read())