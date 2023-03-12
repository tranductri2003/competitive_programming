import time
from array import array

# Cach append
start = time.time()
list = []
for i in range(10**8):
    list.append(10**9)
finish = time.time()
print(finish-start)


# Cach gan
start = time.time()
list = [0]*(10**8)
for i in range(10**8):
    list[i] = 10**9
finish = time.time()
print(finish-start)

# test list
start = time.time()
a = 0
for i in range(10**8):
    a += list[i]
finish = time.time()
print(finish-start)

# test array
list = array("i", list)
start = time.time()
a = 0
for i in range(10**8):
    a += list[i]
finish = time.time()
print(finish-start)
