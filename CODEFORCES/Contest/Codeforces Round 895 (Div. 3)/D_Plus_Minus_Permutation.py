import math

t=int(input())
for _ in range(t):
    n,x,y = list(map(int,input().split()))
    
    temp = math.lcm(x,y)
    chung = n//temp    

    trencon = n//x-chung
    duoicon = n//y-chung




    tongtren = (n-trencon+1+n)*trencon/2
    tongduoi = (1+duoicon)*duoicon/2
    res = int(tongtren-tongduoi)
    print(res)
