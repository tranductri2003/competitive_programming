print("Gõ chu trinh nếu bạn muốn tìm chu trình Hamilton")
print("Gõ duong di nếu bạn muốn tìm đường đi Hamilton")

query=input()



print("Mời bạn nhập lần lượt n, m là số đỉnh và số cạnh của đồ thị:")
n,m=list(map(int,input().split()))

matrix=[]
for i in range(0,n+1):
    matrix.append([])
    for j in range(0,n+1):
        matrix[i].append(False)

print("Mời bạn nhập các cạnh của đồ thị:")
for i in range(0,m):
    u,v=list(map(int,input().split()))
    matrix[u][v]=True
    matrix[v][u]=True

route=[0]*(n+1)
route[1]=1
free=[True]*(n+1)
free[1]=False

if "chu trinh" in query:

    def Try(i):
        for j in range(1,n+1):
            if free[j]==True and matrix[route[i-1]][j]==True:
                route[i]=j
                if i<n:
                    free[j]=False
                    Try(i+1)
                    free[j]=True
                else:
                    if matrix[j][route[1]]==True:
                        print("Một chu trình Hamilton của đồ thị:")
                        print(*route[1:n+1],end=" ")
                        print(1)
                        quit()

                     

if "duong di" in query:

    def Try(i):
        for j in range(1,n+1):
            if free[j]==True and matrix[route[i-1]][j]==True:
                route[i]=j
                if i<n:
                    free[j]=False
                    Try(i+1)
                    free[j]=True
                else:
                    print("Một đường đi Hamilton của đồ thị:")
                    print(*route[1:n+1])
                    quit()
                

Try(2)


"""
chu trinh
5 6
1 2
1 3
2 4
3 5
4 1
5 2


chu trinh
5 8
1 2 
1 5
2 5
2 3
5 4
4 3 
2 4
3 5

duong di
4 4
1 2
2 3
3 4
2 4

chu trinh
5 7
1 2
1 4
5 2
5 4
2 3
4 3
5 3


"""   