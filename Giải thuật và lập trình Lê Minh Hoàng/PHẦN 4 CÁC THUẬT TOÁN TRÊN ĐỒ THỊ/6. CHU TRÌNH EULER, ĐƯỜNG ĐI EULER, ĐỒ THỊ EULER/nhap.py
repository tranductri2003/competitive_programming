"""
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

res=[]

stack=[]
stack.append(1)   #ngăn xếp ban đầu chỉ chứa đỉnh 1

while stack!=[]:
    u=stack[-1]
    for v in range(1,n+1):
        if matrix[u][v]>0:
            stack.append(v)
            matrix[v][u]-=1
            matrix[u][v]-=1
            break
    if u==stack[-1]: #Nếu phần tử ở đỉnh ngăn xếp vẫn là u => Vòng lặp trên không tìm thấy đỉnh nào kề với u nữa
        res.append(u)
        stack.pop()
    
res=res[::-1]

print(f"Chu trình Euler là: {res}")

"""
Thuật toán hoạt động với hiệu quả cao, dễ cài đặt, nhưng trường hợp xấu nhất thì stack sẽ phải chứa toàn bộ danh sách đỉnh
trên chu trình Euler chính vì vậy mà đa đồ thị có số cạnh quá lớn thì sẽ không đủ không gian nhớ
mô tả stack.
Ta cứ thử với đồ thị chỉ gồm 2 đỉnh nhưng giữa hai đỉnh đó có tới 10^6 cạnh nối sẽ thấy ngay.
Lý do thuật toán chỉ có thể áp dụng trong trường hợp số cạnh có giới hạn biết trước đủ nhỏ
là như vậy.
"""