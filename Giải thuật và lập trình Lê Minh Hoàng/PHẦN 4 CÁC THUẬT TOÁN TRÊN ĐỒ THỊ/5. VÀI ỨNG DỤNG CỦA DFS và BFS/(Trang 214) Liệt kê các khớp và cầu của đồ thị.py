#n: số đỉnh của đồ thị vô hướng G, m: số cạnh của đồ thị vô hướng G
n,m=list(map(int,input().split()))

#Tạo ma trận kề
matrix=[]

for i in range(0,n+1):
    matrix.append([])
    for j in range(0,n+1):
        matrix[i].append(False)


for i in range(0,m):
    u,v=list(map(int,input().split()))
    matrix[u][v]=True    #Vì đây là đồ thị vô hướng nên đây là các cạnh, có hai chiều đi
    matrix[v][u]=True

count=0
MAX=10**9

number=[0]*(n+1)     #Đánh số các đỉnh
low=[0]*(n+1)   #low[u] là giá trị number[.] nhỏ nhất của những đỉnh đến được từ nhánh DFS gốc u bằng một cung ngược
#Tức là nếu nhánh DFS gốc u có nhiều cung ngược hướng lên phía gốc thì ta ghi nhận lại cung ngược hướng lên cao nhất
#Nếu nhánh DFS gốc u không chứa cung ngược thì ta cho low[u]=+infinity

parent=[0]*(n+1)   #Chỉ ra nút cha của nút v trên cây DFS, nếu v là gốc của một cây DFS thì parent[v]=-1
#Công dụng của mảng parent là cho phép duyệt tất cả các cạnh trên cây DFS và kiểm tra một đỉnh có phải là gốc của cây DFS hay không

def  visit(u): #Duyệt DFS, định chiều, đánh số
    global count

    count+=1
    number[u]=count

    low[u]=MAX   #Khởi gián low[u]=+infinity

    for v in range(1,n+1):
        if matrix[u][v]==True: #Nếu có cạnh nối u với v
            matrix[v][u]=False

            if parent[v]==0: #Nếu đỉnh v chưa thăm, (u,v) vẫn là cung DFS
                parent[v]=u
                visit(v)
                low[u]=min(low[u],low[v])
            else:   #Nếu đỉnh v đã thăm rồi, tức (u,v) là cung ngược
                low[u]=min(low[u],number[v])
    
for u in range(1,n+1):
    if parent[u]==0:   #Nếu gặp một đỉnh chưa thăm
        parent[u]=-1   #Cho u là một gốc của cây DFS
        visit(u)       #Xây dựng cây DFS gốc u

nChildren=[0]*(n+1)   # nChildren[u]=Số nhánh con của nhánh DFS gốc u
IsCut=[False]*(n+1)   #  IsCut[u]=True: u là cut vertices hay chính là khớp


for v in range(1,n+1):
    u=parent[v]
    if u!=-1:
        nChildren[u]+=1   #Số nhánh con của nhánh DFS gốc u tăng thêm 1



for v in range(1,n+1):
    u=parent[v]
    if u!=-1 and low[v]>=number[v]:  #Từ một đỉnh thuộc nhánh DFS gốc v đi theo các cung định hướng chỉ đi được tới những đỉnh nội bộ trong nhánh DFS gốc v mà thôi
        print(f"Bridges: {parent[v]} {v}")

"""for v in range(1,n+1):
    if parent[v]!=-1:   #Không xét v là gốc, v nhỏ nhất có thể là áp gốc
        u=parent[v]
        if low[v]>=number[u]:   #Điều kiện tiên quyết để xác định khớp: nếu bỏ u thì đi từ v không có cách nào lên được các tiền bối của u
            if parent[u]!=-1 or nChildren[u]>=2: #u không phải gốc cây DFS hoặc u có >=2 nhánh con
                IsCut[u]=True
"""

for v in range(1,n+1):
    u=parent[v]
    if u!=-1:
        if (parent[u]!=-1 and low[v]>=number[u]) or (nChildren[u]>=2 and low[v]>=number[u]):
            IsCut[u]=True

for u in range(1,n+1):
    if IsCut[u]==True:
        print(f"Cut vertices: {u}")



"""
12 14
1 2
1 3
2 3
2 4
2 5
2 7
3 6
4 5
4 7
5 10
6 8
6 9
8 9
11 12
"""


