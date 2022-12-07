



t=int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(0)
    for i in range(n):
        a=list(map(int,input().split()))
        for j in range(m):
            matrix[i][j]=a[j]
            
