t=int(input())

for _ in range(t):
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a.sort()
    tren=a[0:n]
    duoi=a[n:]

    for i in range(n):
        if duoi[i]-tren[i]>=x:
            pass
        else:
            print("NO")
            break
    else:
        print("YES")