

MAX=10**9

n,m,s,f=list(map(int,input().split()))
matrix=[]
for i in range(0,n+1):
    matrix.append([])
    for j in range(0,n+1):
        if i==j:
            matrix[i].append(0)
        else:
            matrix[i].append(MAX)

    
for i in range(0,n):
    u,v,c=list(map(int,input().split()))
    matrix[u][v]=c

#List chứa danh sách các đỉnh theo thứ tự đánh số mới
list=[1]*(n+1)

free=[True]*(n+1)


#Thuật toán đánh số các đỉnh

def visit(u):
    global count
    free[u]=False
    for v in range(1,n+1):
        if free[v]==True and matrix[u][v]!=MAX:
            visit(v)
    list[count]=u
    count-=1

count=n
for u in range(1,n+1):
    if free[u]==True:
        visit(u)

d=[MAX]*(n+1)
d[0]=0
trace=[0]*(n+1)

for i in range(1,n):
    for j in range(i+1,n+1):
        u=list[i]
        v=list[j]
        if d[v]>d[u]+matrix[u][v]:
            trace[v]=u

print(d[f])

