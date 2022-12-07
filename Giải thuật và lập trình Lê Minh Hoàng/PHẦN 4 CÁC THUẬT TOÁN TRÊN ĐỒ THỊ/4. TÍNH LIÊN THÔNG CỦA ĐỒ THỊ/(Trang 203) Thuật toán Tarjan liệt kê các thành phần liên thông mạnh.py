#n: số đỉnh, m: số cung
n,m=list(map(int,input().split()))

#number[u]: là số thứ tự của đỉnh u theo cách đánh số thứ tự các đỉnh từ đỉnh đầu tiên đến đỉnh được thăm cuối cùng
number=[0]*(n+1)
#low[u]: là giá trị number[.] nhỏ nhất trong các đỉnh có thể đến được từ một đỉnh v nào đó của nhánh DFS gốc u bằng một cung.
low=[0]*(n+1)
#stack: ta dùng ngăn xếp này để lấy ra các đỉnh thuộc một nhánh nào đó. Khi thăm tới một đỉnh u, ta đẩy ngay đỉnh u đó vào ngăn xeepsm thì khi duyệt xong đỉnh u, mọi đỉnh thuộc nhánh DFS gốc u sẽ được đẩy vào ngăn xếp stack ngay sau u
stack=[]
#free[u]: free[u]=True nếu như u chưa bị liệt kê vào thành phần liên thông nào, tức là u chưa bị loại ra khỏi đồ thị
free=[True]*(n+1)

count=0  #Đánh số thứ tự các đỉnh
componentCount=0 #Đánh số thành phần liên thông mạnh

matrix=[]
for i in range(0,n+1):
    matrix.append([])
    for j in range(0,n+1):
        matrix[i].append(0)   #matrix[i][j]: từ đỉnh i đến j không có cạnh

def visit(u):
    global count   #Đặt biến toàn cục để đánh thứ tự các đỉnh
    global componentCount    #Đặt biến toàn cục để đánh thứ tự các phần tử liên thông mạnh
    count +=1
    number[u]=count  #Trước hết đánh số u
    low[u]=number[u]  #Coi u có cung tới i, nên ta có thể khởi gán low[u] như thế này rồi cực tiểu hóa dần
    stack.append(u)  #Đẩy u vào ngăn xếp
    for v in range (1,n+1):
        if free[v]==True and matrix[u][v]==1:   #Đỉnh v vẫn còn nằm trong đồ thị và đỉnh v kề đỉnh u
            if number[v]!=0:  #Tức là đỉnh v đã được thăm
                low[u]=min(low[u],number[v])
            else: #Chưa thăm đỉnh v, ta gọi đệ quy đi thăm v 
                visit(v)  #Tiếp tục tìm kiếm theo chiều sâu bắt đầu từ v
                low[u]=min(low[u],low[v])
    
    #Đến đây thì đỉnh u được duyệt xong, tức là các đỉnh thuộc nhánh DFS gốc u đều đã thăm
    if number[u]==low[u]:   #Nếu u là chốt
        componentCount+=1
        print (f"Component {componentCount}:")   #Liệt kê các thành phần liên thông mạnh có chốt u
        while stack[-1]!=u: 
            print(stack[-1],end=", ")
            free[stack[-1]]=False   #Loại đỉnh đó ra khỏi đồ thị
            stack.pop()  #Lấy dần đỉnh ra khỏi ngăn xếp
        print(stack[-1])
        free[stack[-1]]=False
        stack.pop()

for i in range(0,m):
    u,v=list(map(int,input().split()))
    matrix[u][v]=1

#Thay vì thêm một đỉnh giả x và các cung (x,v) với mọi đỉnh v rồi gọi visit(x), ta có thể làm thế này cho nhanh
for u in range(1,n+1):  #Vì sẽ có trường hợp đồ thị gồm nhiều thành phần liên thông riêng biệt
    if number[u]==0:
        visit(u)


"""
11 15
1 2
1 8
2 3
3 4
4 2
4 5
5 6
6 7
7 5
8 9
9 4
9 10
10 8
10 11
11 8
"""


"""
6 6 
1 2
2 3
1 3
4 5
5 6
4 6
"""