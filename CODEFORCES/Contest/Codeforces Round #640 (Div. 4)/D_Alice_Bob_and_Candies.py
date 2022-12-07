t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    alice=0
    bob=0
    move=1
    A=a[0]

    i=1
    j=n-1
    

    while i<=j:
        if move%2==1: #Đến lượt Bob
            B=0
            while j>=i and B<=A:
                B+=a[j]
                j-=1
            move+=1
        else: #Đến lượt Alice
            A=0
            while i<=j and A<=B:
                A+=a[i]
                i+=1
            move+=1
    alice=sum(a[:i])
    bob=sum(a)-alice
    print(move,alice,bob)
                
            
            

        
        
        
        
        