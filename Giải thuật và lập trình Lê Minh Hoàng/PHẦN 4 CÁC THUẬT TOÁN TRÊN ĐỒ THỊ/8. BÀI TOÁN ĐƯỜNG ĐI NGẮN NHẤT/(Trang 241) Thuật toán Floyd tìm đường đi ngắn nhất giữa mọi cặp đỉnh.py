MAX=10**9
n,m,s,f=list(map(int,input().split()))

matrix=[]
for i in range(0,n+1):
    matrix.append([])
    for j in range(0,n+1):
        if i==j:
            matrix[i].append(0)
        else:
            matrix[i].append(MAX)

for i in range(m):
    u,v,c=list(map(int,input().split()))
    matrix[u][v]=c

trace=[]
for u in range(0,n+1):
    trace.append([])
    for v in range(0,n+1):
        trace[u].append(v)   #Giả sử đường đi ngắn nhất giữa mọi cặp đỉnh là đường trực tiếp
        #trace[u][v] là điểm liền sau u trên đường tới v


#Thuật toán Floyd
for k in range(1,n+1):
    for u in range(1,n+1):
        for v in range(1,n+1):
            if matrix[u][v]>matrix[u][k]+matrix[k][v]:     #Đường đi qua từ k tốt hơn
                matrix[u][v]=matrix[u][k]+matrix[k][v]  #Ghi nhận đường đi đó thay cho đường đi cũ
                trace[u][v]=trace[u][k]   #Lưu vết đường đi

print(f"Distance from {s} to {f} is: {matrix[s][f]}")


while s!=f:
    print(s,end="->")
    s=trace[s][f]
print(f)

for i in range(1,n+1):
    print(matrix[i])
#Khác biệt rõ ràng của thuật toán floyd là khi cần tìm đường đi ngắn nhất giữa một cặp đỉnh khác
#chương trình chỉ việc in kết quả chứ không phải thực hiện lại thuật toán floyd nữa.


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
