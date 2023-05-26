from time import sleep

def old_print(*x):
    for i in x:
        print(i, end="")
        sleep(1e-5)
    print()
    sleep(1e-5)

old_print("ala ma kota")

from threading import Thread, Lock

def f(*n):
    for i in range(n[0]):
        with lock:
            old_print(n[1], i)

from time import time
t = time()
lock = Lock()
thread1 = Thread(target=f, args=(10,"a"))
thread2 = Thread(target=f, args=(10,"b"))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("End1")
print(time()-t)


# t = time()
# for i in range(2):
#     for j in range(10):
#         print(i, j)
# print("End2")
# print(time()-t)