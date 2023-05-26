from requests import get
import io

# f = get("http://docs.python.org")
# s = f.text
# f.close()
#
# f = get("http://docs.python.org", stream=True)
# for i in f.iter_lines():
#     print(i.decode("UTF-8"))
# f.close()

def stolica1(p):
    f = get("https://pl.wikipedia.org/wiki/"+p)
    s = f.text
    print(s.split("Stolica</a>")[1].split('">')[1].split("<")[0])
    f.close()

def stolica2(p):
    f = get("https://pl.wikipedia.org/wiki/"+p, stream=True)
    b, c, d = "", "", ""
    for i in f.iter_lines():
        a, b, c, d = (b, c, d, i.decode("UTF-8"))   # 4 kolejne linie
        if "Stolica</a>" in a:
            f.close()
            print(d.split('">')[1].split("<")[0])

# stolica1("Polska")

from time import time

panstwa = ["Polska", "Niemcy", "Szwecja", "Islandia", "Indie",
           "Japonia", "Tanzania",
           "Kanada",
           "Australia",
           "Kolumbia"]

t = time()
print(list(map(stolica1, panstwa)))
print(time()-t)