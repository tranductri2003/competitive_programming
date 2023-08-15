t=int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    if len(set(a))==1:
        print(-1)
    else:
        a.sort()
        minn = min(a)
        temp = a.count(minn)
        mangB=[]
        mangC=[]
        for i in range(temp):
            mangB.append(minn)
        for i in range(temp,n):
            mangC.append(a[i])
        print(len(mangB), len(mangC))
        print(*mangB)
        print(*mangC)