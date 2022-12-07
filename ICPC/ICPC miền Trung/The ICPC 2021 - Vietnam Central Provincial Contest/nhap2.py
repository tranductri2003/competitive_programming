import math
def DFS(u,current_root):
    for v in range(N+1):
        if matrix[u][v]==True and root[v]==-1:
            root[v]=current_root
            DFS(v,current_root)
            
        

N,M=input()

root=[-1]*(N+1)

matrix=[]
for i in range(0,N+1):
    matrix.append([])
    for j in range(0,N+1):
        matrix[i].append(False)

for i in range(M):
    u,v=list(map(int,input().split()))
    matrix[u][v]=True
    matrix[v][u]=True

for u in range(0,N+1):
    current_root=u
    DFS(u,current_root)

res=[0]*(N+1)
for num in root:
    res[num]+=1

ans=0
for num in res:
    if num>=3:
        ans+=math.factorial(num)%(10**9+7)

print(ans)