print("Mời bạn nhập kích thước bàn cờ n:")
n=int(input())

#Đổi 0->00, 5->05,...
def balanced(n):
    n=str(n)
    if len(n)==1:
        n="0"+str(n)
        return n
    else:
        return n


def numToCoordinate(N):
    x=(N-1)%n
    y=(N-1)//n
    return x,y


position=[]
def possiblePosition(N):
    a=[]
    x,y=numToCoordinate(N)
    if x>=1 and y>=2:
        a.append(N-2*n-1)
    if x<=n-2 and y>=2:
        a.append(N-2*n+1)
    if x>=2 and y>=1:
        a.append(N-n-2)
    if x<=n-3 and y>=1:
        a.append(N-n+2)
    if x>=2 and y<=n-2:
        a.append(N+n-2)
    if x>=1 and y<=n-3:
        a.append(N+2*n-1)
    if x<=n-2 and y<=n-3:
        a.append(N+2*n+1)
    if x<=n-3 and y<=n-2:
        a.append((N+n+2))
    return a

def visualization():
    print("Bạn có thể tham khảo mô hình dưới đây:")

    for i in range(1,n**2+1):
        x,y=numToCoordinate(route[i])
        matrix[y][x]=balanced(i)

    for i in range(0,n):
        print(*matrix[i])

matrix=[]

for i in range(0,n):
    matrix.append([])
    for j in range(0,n):
        num=balanced(j+n*i+1)
        matrix[i].append(num)


route=[0]*(n**2+1)
free=[True]*(n**2+1)

for i in range(0,n):
    print(*matrix[i])

#Hàm để thử cách chọn ô thứ i trong bàn cờ
def Try(i):
    u=route[i-1]
    position=possiblePosition(u)
    for v in position:
        route[i]=v
        if free[int(v)]==True:
            if i<n**2:
                free[v]=False
                Try(i+1)
                free[v]=True
            else:
                print("Đường đi Hamilton là: ")
                print(*route[1::])
                visualization()
                quit()

for u in range(1,n**2+1):
    route[1]=u
    free[u]=False
    Try(2)
    route=[0]*(n**2+1)
    free=[True]*(n**2+1)

