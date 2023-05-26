from requests import get

# f = get("http://docs.python.org")
# s = f.text
# f.close()
#
# f = get("http://docs.python.org", stream=True)
# for i in f.iter_lines():
#     print(i.decode("UTF-8"))
# f.close()

def capital1(p):
    f = get("https://pl.wikipedia.org/wiki/"+p)
    s = f.text
    print(s.split("Stolica</a>")[1].split('">')[1].split("<")[0])
    f.close()

def capital2(p):
    f = get("https://pl.wikipedia.org/wiki/"+p, stream=True)
    b, c, d = "", "", ""
    for i in f.iter_lines():
        a, b, c, d = (b, c, d, i.decode("UTF-8"))   # 4 kolejne linie
        if "Stolica</a>" in a:
            f.close()
            print(d.split('">')[1].split("<")[0])

# capital1("Polska")

from time import time

panstwa = ["Polska", "Niemcy", "Szwecja", "Islandia", "Indie",
           "Japonia", "Tanzania", "Kanada", "Australia", "Kolumbia"]

# t = time()
# print(list(map(capitol1, panstwa)))
# print(time()-t)

from threading import Thread

def w_capital(i):
    print(capital1(i))

t = time()
threads = [Thread(target=w_capital, args=(p,)) for p in panstwa]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time()-t)