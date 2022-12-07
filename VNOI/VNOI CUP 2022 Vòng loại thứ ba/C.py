from collections import Counter
def showMatrix(n,m):
    for i in range(n):
        print(*matrix[i])
n,m=list(map(int,input().split()))
if n==2 and m==1:
    u,v,x,y=list(map(int,input().split()))
    print(x,y)
else:
    matrix=[]
    for i in range(2*m+1):
        matrix.append([])
        for j in range(n+1):
            matrix[i].append(0)
    for i in range(0,2*m,2):
        u,v,x,y=list(map(int,input().split()))
        matrix[i+1][u]=x
        matrix[i+1][v]=y
        matrix[i+2][u]=y
        matrix[i+2][v]=x        
    for i in range(1,n+1):
        data=[]
        for j in range(1,2*m+1):
            data.append(matrix[j][i])
        check=Counter(data)
        if len(check)==0:
            print(100,end=" ")
        else:
            ma=-1
            for num in range(len(check)):
                if num!=0:
                    ma=max(ma,check[num])
            print(ma,end=' ')
        
    print()