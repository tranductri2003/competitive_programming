n=int(input())

for i in range(0,n):
    quan=int(input())
    

    for j in range(0,quan):
        print("("*(quan-j),end="")
        print(")"*(quan-j),end="")
        print("()"*j,end="")
        print(" ")

