import time

a = time.time()
v = 0
for i in range(1, 1000000):
    v += 1000000

b = time.time()
print(b-a)
