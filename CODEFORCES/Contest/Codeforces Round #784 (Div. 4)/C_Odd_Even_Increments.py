t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    chan=[]
    le=[]
    stop=False
    for i in range(n):
        if i%2==0:
            chan.append(a[i])
        else:
            le.append(a[i])
    for i in range(len(chan)-1):
        if chan[i]%2==chan[i+1]%2:
            pass
        else:
            stop=True
    for i in range(len(le)-1):
        if le[i]%2==le[i+1]%2:
            pass
        else:
            stop=True
    
    if stop==True:
        print("NO")
    else:
        print("YES")