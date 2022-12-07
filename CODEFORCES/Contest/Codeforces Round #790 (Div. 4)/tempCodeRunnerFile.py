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
            
    
    #Kết quả là tổng của 2 đường cheo lớn nhất
    duongcheo1=[]
    i=n-1
    j=0
    for start in range(n-1,-1,-1):
        i=start
        j=0
        temp=0
        while i<=n-1 and j<=m-1:
            temp+=matrix[i][j]
            i+=1
            j+=1
        duongcheo1.append(temp)
    a=[]
    for start in range(m):
        i=start
        j=i
        temp=0
        while i<=n-1 and j<=m-1:
            temp+=matrix[i][j]
            i+=1
            j+=1
        a.append(temp)
    print(a)
        
        