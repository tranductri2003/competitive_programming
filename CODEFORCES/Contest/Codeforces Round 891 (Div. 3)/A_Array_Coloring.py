t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    tong=sum(a)
    if tong%2==1:
        print("NO")
    else:
        print("YES")