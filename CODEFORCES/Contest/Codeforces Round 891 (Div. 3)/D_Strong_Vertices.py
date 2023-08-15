t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b= list(map(int,input().split()))
    c=[0]*n
    for i in range(n):
        c[i] = a[i]-b[i]
    maxTemp = max(c)
    data=[]
    for i in range(n):
        if c[i]==maxTemp:
            data.append(i+1)
    print(len(data))
    print(*data)