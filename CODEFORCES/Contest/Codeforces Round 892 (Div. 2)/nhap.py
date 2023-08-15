import random


print(5)
res=[]
for _ in range(5):
    n = random.randint(1,10)
    q = random.randint(1,5)
    a =[]
    for i in range(n):
        a.append(random.randint(1,1000))

    print(n,q)
    print(*a)
    query=[]
    for i in range(q):
        l = random.randint(1,len(a))
        r = random.randint(l, len(a))
        maxx = max(a[l-1:r])
        a=a[:l-1]+[maxx]+a[r:]
        query.append((l,r))

    for pair in query:
        print(pair[0], pair[1])
    res.append(a)

print()
print()

for num in res:
    print(*num)

