import random
print(1)
print(10, 100)
data = []
for i in range(10):
    data.append(random.randint(25, 75))

print(*data)
for i in range(100):
    l = random.randint(25, 50)
    r = random.randint(50, 100)
    print(l, r)
