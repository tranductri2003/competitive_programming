
        
from collections import defaultdict

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
            
    # showMatrix(matrix,n,m)
    # Đường chéo chính: x-y không đổi, là đường chéo xuống như trong định thức
    # Đường chéo phụ: x+y không đổi, là dường chéo lên

    duongcheochinh=defaultdict(lambda:0)
    duongcheophu=defaultdict(lambda:0)
    
    for i in range(n-1,0,-1):
        t=i
        j=0
        temp=0
        while i<=n-1 and j<=m-1:
            temp+=matrix[i][j]
            i+=1
            j+=1
        duongcheochinh[t]=temp
    for j in range(0,m):
        t=j
        i=0
        temp=0
        while j<=m-1 and i<=n-1:
            temp+=matrix[i][j]
            i+=1
            j+=1
        duongcheochinh[-t]=temp

    for i in range(0,n-1):
        t=i
        j=0
        temp=0
        while i>=0 and j<=m-1:
            temp+=matrix[i][j]
            i-=1
            j+=1
        duongcheophu[t]=temp
    for j in range(0,m):
        t=j
        i=n-1
        temp=0
        while j<=m-1 and i>=0:
            temp+=matrix[i][j]
            i-=1
            j+=1
        duongcheophu[t+n-1]=temp
    res=-10**9
    for i in range(n):
        for j in range(m):
            res=max(res,duongcheochinh[i-j]+duongcheophu[i+j]-matrix[i][j])
    print(res)
    

    