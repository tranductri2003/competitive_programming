import math
#N: So luong hoc sinh
#M: So hoc sinh phong van
N,M=list(map(int,input().split()))

matrix=[]
for i in range(0,N+1):
    matrix.append([i])

    
for i in range(M):
    u,v=list(map(int,input().split()))
    matrix[u].append(v)
    matrix[v].append(u)

for i in range(0,N+1):
    for j in matrix[i]:
        pass
        
free=[True]*(N+1)

res=0
for i in range(0,N+1):
    num=0
    for j in range(0,N+1):
        if matrix[i][j]==1 and free[j]==True:
            num+=1
            free[j]=False
    if num>=3:
        res+=math.factorial(num)%(10**9+7)
        
print(res)
    