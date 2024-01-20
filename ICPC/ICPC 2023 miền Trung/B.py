from random import randint
n = int(input())
a = []
for _ in range(n):
    a.append(randint(2,10**5))

print(n)
print(*a)
a.sort()
q = randint(1,10)
print(q)
for _ in range(q):
    x = min(a)
    y = max(a)
    k = _
    print(x,y,k)

    