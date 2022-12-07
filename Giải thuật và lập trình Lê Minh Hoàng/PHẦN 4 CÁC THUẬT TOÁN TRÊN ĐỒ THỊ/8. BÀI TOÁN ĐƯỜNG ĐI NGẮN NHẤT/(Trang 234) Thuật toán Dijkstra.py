def dijkstra():
    MAX=10**9




    #n: số đỉnh, m: số cạnh, s: đỉnh xuất, f: đỉnh kết thúc
    n,m,s,f=list(map(int,input().split()))

    matrix=[]
    for i in range(0,n+1):
        matrix.append([])
        for j in range(0,n+1):
            if i==j:
                matrix[i].append(0)
            else:
                matrix[i].append(MAX)

    for i in range(0,m):
        u,v,c=list(map(int,input().split()))
        matrix[u][v]=c

    #d[v] là độ dài đường đi ngắn nhất từ s tới v
    d=[MAX]*(n+1)
    d[s]=0

    #Thao tác cố định nhãn
    free=[True]*(n+1)  #Các đỉnh đều được coi là tự do
    #Nhãn của mỗi đỉnh có hai trạng thái tư do hay cố định
    #Nhãn cố định tức là d[v] đã bằng độ dài đường đi ngắn nhất từ s tới v nên không thể tối ưu thêm



    #Truy hồi
    trace=[0]*(n+1)
    trace[s]=-1

    #Thuật toán Dijkstra
    stop=False  
    while stop==False:
        #Tìm trong các đỉnh nhãn tự do ra đỉnh u có d[u] nhỏ nhất
        u=0
        min=MAX
        for i in range(1,n+1):
            if free[i]==True and d[i]<min:
                min=d[i]
                u=i

        #Thuật toán sẽ kết thúc khi các đỉnh tự do đều có nhãn MAX hoặc đã chọn đến đỉnh f
        if u==0 or u==f:
            stop=True
        
        #Cố định nhãn đỉnh u
        free[u]=False

        #Dùng đỉnh u để tối ưu những nhãn tự do kề với u

        for v in range(1,n+1):
            if free[v]==True and d[v]>d[u]+matrix[u][v]:
                d[v]=d[u]+matrix[u][v]
                trace[v]=u

    for i in range(1,n+1):
        print(*matrix[i][1:])

    print(f"Distance from {s} to {f}: {d[f]}")

    while f!=s:
        print(f,end="<-")
        f=trace[f]
    print(s)

dijkstra()