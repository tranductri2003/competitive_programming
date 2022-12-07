for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
    else:
        res=[i for i in range(1,n)]
        res.insert(0,n)
        print(*res)
            

        
