
t=int(input())
for _ in range(t):
    n, m = list(map(int,input().split()))
    x = input()
    s = input()
    res =0
    while s not in x:
        x+=x
        res+=1
        if res>10:
            print(-1)
            break
    else:
        print(res)