t=int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    a.sort()
    data=[]
    for i in range(n):
        data.append(a[i]**2)
        
    q = int(input())
    for i in range(q):
        x,y = list(map(int,input().split()))
        ketqua = x**2-2*y
        