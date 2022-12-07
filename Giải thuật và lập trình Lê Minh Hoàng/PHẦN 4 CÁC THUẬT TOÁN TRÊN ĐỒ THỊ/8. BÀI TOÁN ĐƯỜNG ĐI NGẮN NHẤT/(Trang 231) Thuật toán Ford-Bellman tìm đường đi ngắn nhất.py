def fordbellman():
    MAX=10**9

    #n: số đỉnh, m: số cung, s: đỉnh xuất phát, f: đỉnh đích
    n,m,s,f=list(map(int,input().split()))

    #Tạo ma trận trọng số
    matrix=[]

    for i in range(0,n+1):
        matrix.append([])
        for j in range(0,n+1):
            if i==j:
                matrix[i].append(0)
            else:
                matrix[i].append(MAX)  #Những cạnh không có trong đồ thị được gán trọng số dương vô cùng

    for i in range(0,m):
        u,v,c=list(map(int,input().split()))
        matrix[u][v]=c

    #d[v]: Chi phí thấp nhất từ s đến v
    d=[MAX]*(n+1)
    d[s]=0 

    #Truy vết:
    trace=[0]*(n+1)
    trace[s]=-1

    #Thuật toán Ford-Bellman:
    for lapse in range(1,n):
        stop=True
        for u in range(1,n+1):
            for v in range(1,n+1):
                if d[v]>d[u]+matrix[u][v]:   #Ta sẽ tối ưu lại d[v]
                    d[v]=d[u]+matrix[u][v]
                    trace[v]=u
                stop=False  
        if stop==True:   #Thuật toán kết thúc khi không sửa nhãn các d[v] được nữa hoặc đã lặp đủ n-1 lần
            break

    if d[f]==MAX:
        print(f"There is no path from {s} to {f}")
    else:
        print(f"Distance from {s} to {f}: {d[f]}")
        while f!=s:
            print(f,end="<-")
            f=trace[f]
        print(s)

"""for i in range(1,n+1):
    print(matrix[i][1:])"""

"""
6 7 1 4
1 2 1
1 6 20
2 3 2
3 6 3
3 4 20
5 4 5
6 5 4
"""
fordbellman()