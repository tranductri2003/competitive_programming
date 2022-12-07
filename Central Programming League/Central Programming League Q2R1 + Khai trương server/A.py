from collections import defaultdict 
while True:
    n=int(input())
    if n==0:
        break
    else:
        data=[]
        for i in range(n):
            x,y=list(map(int,input().split()))
            data.append((x,y))
        check=defaultdict(lambda:-1)
        
        x=10
        y=10
        check[(x,y)]=1
        
        
        m=int(input())
        for i in range(m):
            direction,l=input().split()
            l=int(l)
            if direction=="N":
                for i in range(l):
                    y+=1
                    check[(x,y)]=1
            if direction=="S":
                for i in range(l):
                    y-=1
                    check[(x,y)]=1
            if direction=="E":
                for i in range(l):
                    x+=1
                    check[(x,y)]=1
            if direction=="W":
                for i in range(l):
                    x-=1
                    check[(x,y)]=1    
        for num in data:
            x,y=num[0],num[1]
            if check[(x,y)]==-1:
                print("No")
                break
        else:
            print("Yes")
                    
            