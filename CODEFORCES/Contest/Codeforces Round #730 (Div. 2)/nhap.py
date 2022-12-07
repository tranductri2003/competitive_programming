
from os import get_inheritable


n,k=list(map(int,input().split()))
a=[]
sophantu=0
while sophantu!=n:
    dayphu=list(map(int,input().split()))
    a+=dayphu
    sophantu+=len(dayphu)

for i in range(0,n):
    a[i]=a[i]%k
a.insert(0,0)
matrix=[]
for i in range(0,n+1):
    matrix.append([])
    for j in range(0,k):
        matrix[i].append(-10**9)
matrix[1][a[1]]=1
for i in range(2,n+1):
    for j in range(0,k):
        matrix[i][j]=max(matrix[i-1][j],matrix[i-1][(j-a[i]+k)%k]+1)
"""for i in range(0,n+1):
    print(*matrix[i])"""
    
res=max(matrix[n][0],0)
print(res)
        