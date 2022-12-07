import time

a = time.time()


for i in range(10000):
    pass
b = time.time()
print(b-a)
