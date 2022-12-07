t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    res=0
    for i in range(1,4):
        if a[i]>a[0]:
            res+=1
    print(res)