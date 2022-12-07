t = int(input())
for _ in range(t):
    n=int(input())
    if n==3:
        print(3, 2, 1)
        print(1, 3, 2)
        print(3, 1, 2)
    else:
        current=[]
        for i in range(n,0,-1):
            current.append(i)
        print(*current)
        for i in range(2, n+1):
            current.insert(0,current[-1])
            current.pop(-1)
            print(*current)
        
        