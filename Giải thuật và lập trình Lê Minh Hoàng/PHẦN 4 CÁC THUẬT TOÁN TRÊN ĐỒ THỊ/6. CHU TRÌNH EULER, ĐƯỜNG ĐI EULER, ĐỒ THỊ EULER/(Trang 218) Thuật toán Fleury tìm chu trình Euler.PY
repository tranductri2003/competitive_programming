#n: số đỉnh của đồ thị và m là số dòng tiếp theo biểu diễn cạnh nối
n,m=list(map(int,input().split()))

#Tạo ma trận kề chứa số cạnh liên kết
matrix=[]
for i in range(0,n+1):
    matrix.append([])
    for j in range(0,n+1):
        matrix[i].append(0)


#m dòng tiếp theo, mỗi dòng chứa 3 số nguyên dương cách nhau ít nhất 1 dấu cách có dạng u v k cho 
#biết giữa đỉnh u và đỉnh v có k cạnh nối

for i in range(0,m):
    u,v,k=list(map(int,input().split()))
    matrix[u][v]=k
    matrix[v][u]=k

#Hàm này kiểm tra nếu xóa một cạnh nối (x,y) thì y có còn quay lại được x hay không?
def CanGoBack(x,y):
    queue=[]
    queue.append(y)     #Kiểm tra có đường đi từ y đến x không nên ta thêm y làm phần tử đầu tiên của queue
    free=[True]*(n+1)

    #Thử xóa một cạnh (x,y) =>Số cạnh nối (x,y) giảm 1
    matrix[x][y]-=1
    matrix[y][x]-=1

    #Áp dụng BFS để xem từ y có quay lại x được không
    while len(queue)!=0:
        u=queue[0]    #Xuất phát từ y
        queue.pop(0)

        for v in range(1,n+1):
            if free[v]==True and matrix[u][v]>0:
                free[v]=False
                queue.append(v)

            if free[x]==False:   #Từ y đến được x
                matrix[x][y]+=1  #Ở trên đã thử xóa cạnh thì giờ phải phục hồi
                matrix[y][x]+=1
                return True   #Từ y trở về x được nên trả về true
    matrix[x][y]+=1  #Ở trên đã thử xóa cạnh thì giờ phải phục hồi
    matrix[y][x]+=1    
    return False   #Từ y không thể trở về x

#Thuật toán Fleury

current=1    #Điểm xuất phát ban đầu ta chọn là 1 (Bất cứ điểm nào cũng được)
print("Chu trình Euler: 1",end="")  #Vì đây là một chu trình nên ta có thể chọn bất kỳ điểm xuất phát ban đầu

next=-1
while next!=0:
    next=0
    for v in range(1,n+1):
        if matrix[current][v]>0: #Có đường đi từ current đến v
            next=v #Ta tạm thời gán next=v
        if CanGoBack(current,next)==True:
            break #Nếu đây không phải là đường một đi không trở lại thì ta chính thức gán luôn, nếu đây là đường một đi không trở lại thì ta lại tìm v tới khi v không phải là đường một đi không trở lại
    
    matrix[current][next]-=1   #Ở đây ta chính thức xóa cạnh đó khi ta vừa đi qua
    matrix[next][current]-=1

    if next==0: #Không còn bất cứ đường nào để đi nữa
        break
    print(f" -> {next}",end="")    
    current=next

if current!=1:
    print(" ")
    print("Dồ thị trên không tồn tại chu trình euler")
"""
4 5
1 2 1
1 3 2
1 4 1
2 3 1
3 4 1
"""

"""
Bài toán 7 cây cầu kinh điển: không phải tất cả các đỉnh đều bậc 2 nên không tồn tại chu trình euler

4 5
1 2 2
1 3 2 
2 4 1 
3 4 1 
1 4 1 
"""
""""""

"""
Euler hình đồng hồ các
5 6
1 2 1
1 5 1
2 5 1
5 3 1
5 4 1 
3 4 1
"""

""" 
Bài tập trang 222:
6 12
1 2 1
1 3 1
2 3 1 
2 4 1
3 4 1
3 6 1
4 6 1
4 5 1
2 5 1
1 6 1
1 5 1
6 5 1

"""