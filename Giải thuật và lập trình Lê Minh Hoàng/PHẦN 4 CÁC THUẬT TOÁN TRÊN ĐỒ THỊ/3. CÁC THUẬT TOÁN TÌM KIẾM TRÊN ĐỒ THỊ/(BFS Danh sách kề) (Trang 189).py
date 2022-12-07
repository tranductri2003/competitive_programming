#n: số đỉnh, m: số cạnh, s: đỉnh xuất phát, f: đỉnh kết thúc
import time
print(f"Mời bạn nhập lần lượt số đỉnh, số cạnh, đỉnh xuất phát, đỉnh kết thúc: ", end="")
n,m,s,f=list(map(int,input().split()))


#Tạo danh sách kề
adjacencyList={}

for i in range(1,n+1):
    print(f"Mời bạn nhập các đỉnh kề với đỉnh {i}: ")
    value=list(map(int,input().split()))
    adjacencyList[i]=value

#Khởi tạo hàng đợi ban đầu chỉ gồm một đỉnh S
queue=[]
queue.append(s)

#Khởi tạo truy vết
trace=[0]*(n+1)
trace[s]=-1
start_time = time.time() 
#bfs
while len(queue)!=0:   #BFS đến khi không còn phần tử nào trong list
    u=queue[0]          #Rút phần tử đầu ra FIFO
    queue.pop(0)
    for v in adjacencyList[u]:    
        if trace[v]==0:
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
end_time = time.time()
#tính thời gian chạy của thuật toán Python
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")