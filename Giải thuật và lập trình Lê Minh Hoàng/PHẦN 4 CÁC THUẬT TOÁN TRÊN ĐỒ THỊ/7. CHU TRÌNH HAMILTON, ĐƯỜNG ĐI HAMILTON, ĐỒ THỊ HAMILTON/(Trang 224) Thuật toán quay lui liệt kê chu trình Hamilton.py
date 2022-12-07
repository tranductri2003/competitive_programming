#n: Đỉnh, m: cạnh

n,m=list(map(int,input().split()))

matrix=[]
for i in range(0,n+1):
    matrix.append([])
    for j in range(0,n+1):
        matrix[i].append(False)

for i in range(0,m):
    u,v=list(map(int,input().split()))
    matrix[u][v]=True
    matrix[v][u]=True

free=[True]*(n+1)    #Mảng đánh dấu free[v]=True nếu chưa đi qua đỉnh v
free[1]=False    #Đặt free[1] =False vì nếu free[1]=True thì trong quá trình đi đến n, các đỉnh sẽ có thể rẽ vô 1
route=[0]*(n+1)     #Chu trình Hamilton sẽ tìm là 1=route[1] -> route[2] ... ->route[n] -> route[1]=1
route[1]=1   #Bắt đầu từ đỉnh 1

def Try(i):  #Thử các cách chọn đỉnh thứ i trong hành trình   
    for j in range(1,n+1):   #Đỉnh thứ i route[i] có thể chọn trong những đỉnh
        if free[j]==True and matrix[route[i-1]][j]==True:     #Nếu đỉnh này chưa bị đi qua và kề với đỉnh route[i-1]
            route[i]=j  #Thử một cách chọn route[i]
            if i<n:     #Nếu chưa thử chọn đến route[n]
                free[j]=False       #Đánh dấu đỉnh j là đã đi qua
                Try(i+1)    
                free[j]=True    #Ta sẽ thử phương án khác cho x[i] nên sẽ bỏ đánh dấu đỉnh vừa thử
            else:    #Nếu đã thử chọn đến route[n]
                if matrix[j][route[1]]==True:   #Và nếu route[n] lại kề với route[1] thì ta có chu trình hamilton
                    print(*route[1:n+1],end=" ")
                    print(1)


print("Các chu trình Hamilton: ")
Try(2)
"""
5 6
1 2 
1 3
2 4
3 5
4 1 
5 2
"""