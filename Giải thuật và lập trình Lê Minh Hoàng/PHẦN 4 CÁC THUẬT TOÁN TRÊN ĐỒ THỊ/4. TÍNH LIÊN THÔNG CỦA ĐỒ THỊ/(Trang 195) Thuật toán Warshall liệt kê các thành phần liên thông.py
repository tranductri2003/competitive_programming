#n: đỉnh, m: cạnh


n,m=list(map(int,input().split()))

matrix=[]
for i in range(0,n+1):
    matrix.append([])
    for j in range(0,n+1):
        matrix[i].append(0)
for i in range(0,n+1):    #A[v][v]=1 (True) với mọi v
    matrix[i][i]=1

#Bước 1: Nhập ma trận kề của đồ thị
for i in range (0,m):
    u,v=list(map(int,input().split()))
    matrix[u][v]=1
    matrix[v][u]=1

#Bước 2: Dùng thuật toán Warshall tìm bao đóng, khi đó A là ma trận kề của bao đống đồ thị
for k in range(1,n+1):
    for u in range(1,n+1):
        for v in range(1,n+1):
            if matrix[u][k]==1 and matrix[k][v]==1:
                matrix[u][v]=1
                #Nếu từ u có đường đi tới k và từ k lại có đường đi tới v thì tất nhiên từ u sẽ có đường đi tới v

#Bước 3: Dựa vào ma trận kề, đỉnh 1 và những đỉnh kề với nó sẽ thuộc thành phần liên thông thứ nhất, với đỉnh u nào đố
#không kề với đỉnh 1, thì u cùng với những đỉnh kề nó sẽ thuộc thành phân liên thông thứ hai, với đỉnh v
# nào đố không kề với cả đỉnh thứ 1 và đỉnh u, thì v cùng với những đỉnh kề nó sẽ thuộc thành phần liên
#thông thứ 3...
free=[True]*(n+1)  #Quy ước mọi đỉnh đều chưa được liệt kê vào bất cứ thành phần liên thông nào
count=0
for i in range(1,n+1):    
    if free[i]==True:#Xét từ điểm 1 đến điểm n, nếu điểm đó chưa được liệt vào bất cứ thành phần liên thông nào thì xét tiếp
        count+=1
        print(f"Connected Component {count}:")
        for j in range(1,n+1):  #Xét toàn bộ đỉnh, lấy ra các đỉnh kề với nó
            if matrix[i][j]==1:
                print(j,end=", ")
                free[j]=False   #Vì được liệt rồi nên đỉnh này không còn tự do nữa
        print(" ")




"""for i in range(0,n+1):
    print(matrix[i])
"""
"""
12 9
1 3
1 4
1 5
2 4
6 7
6 8
9 10
9 11
11 12
"""