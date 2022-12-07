#n: số đỉnh, m: số cạnh, s: đỉnh xuất phát, f: đỉnh kết thúc

print(f"Mời bạn nhập lần lượt số đỉnh, số cạnh, đỉnh xuất phát, đỉnh kết thúc: ", end="")
n,m,s,f=list(map(int,input().split()))

#Khởi tạo danh sách kề
adjacencyList={}

#Khởi tạo truy vết
trace=[0]*(n+1)   #Mọi đỉnh đều được thiết lập là chưa được thăm, đỉnh thăm được có giá trị khác 0
trace[s]=-1   #Đỉnh xuất phát được thiết lập là -1


#Tạo hàm dfs
def dfs(u):
    for v in adjacencyList[u]:
        if trace[v]==0: 
            trace[v]=u    #Đỉnh đến v là u
            
            dfs(v)

print("Mời bạn nhập các danh sách kề: ")
for i in range(1,n+1):
    print(f"Các đỉnh kề với đỉnh {i}:")
    value=list(map(int,input().split()))
    adjacencyList[i]=value

print(adjacencyList)

print("#############################################")
dfs(s)
print(f"From {s} you can visit: ",end="")

for v in range(1,n+1):
    if trace[v]!=0:   #Nếu đỉnh v reachable thì trace[v]!=0
        print(v, end=", ")

print(" ")

print(f"The path from {s} to {f}:",end=" ")

while f!=s:
    print(f, end=" <- ")
    f=trace[f]
print(s)
"""for i in range(1,n+1):
    print(matrix[i][1:n+1])"""