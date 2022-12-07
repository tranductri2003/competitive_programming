t=int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    print(max(sum(a)-m,0))