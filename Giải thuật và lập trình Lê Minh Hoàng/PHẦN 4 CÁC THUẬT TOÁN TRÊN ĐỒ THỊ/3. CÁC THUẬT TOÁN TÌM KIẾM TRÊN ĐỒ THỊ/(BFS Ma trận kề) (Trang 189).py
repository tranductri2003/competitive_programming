def BFS():
    #n: số đỉnh, m: số cạnh, s: đỉnh xuất phát, f: đỉnh kết thúc

    print(f"Mời bạn nhập lần lượt số đỉnh, số cạnh, đỉnh xuất phát, đỉnh kết thúc: ", end="")
    n,m,s,f=list(map(int,input().split()))


    #Tạo ma trận kề
    matrix=[]
    for i in range(0,n+1):
        matrix.append([])
        for j in range(0,n+1):
            matrix[i].append(False)

    for i in range(1,m+1):
        print(f"Mời bạn nhập cặp cạnh thứ {i}: ")
        u,v=list(map(int,input().split()))
        matrix[u][v]=True
        matrix[v][u]=True

    #Khởi tạo hàng đợi ban đầu chỉ gồm một đỉnh S
    queue=[]
    queue.append(s)

    #Khởi tạo truy vết
    trace=[0]*(n+1)
    trace[s]=-1

    #bfs
    while len(queue)!=0:   #BFS đến khi không còn phần tử nào trong list
        u=queue[0]          #Rút phần tử đầu ra FIFO
        queue.pop(0)
        for v in range(1,n+1):
            if trace[v]==0 and matrix[u][v]==True:
                trace[v]=u
                queue.append(v)       #Thêm vào queue

    print(f"From {f} you can visit: ",end="")
    for i in range(1,n+1):
        if trace[i]!=0:
            print(i,end=" ")
        
    print(" ")

    print(f"The path from {s} to {f} là: ",end="")


    while f!=s:
        print(f, end=" <- ")
        f=trace[f]
    print(s)
BFS()