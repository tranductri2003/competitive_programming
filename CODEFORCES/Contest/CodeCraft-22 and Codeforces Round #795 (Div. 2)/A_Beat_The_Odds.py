
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    chan=0
    le=0
    for num in a:
        if num %2==0:
            chan+=1
        else:
            le+=1
    print(min(chan,le))