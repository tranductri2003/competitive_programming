t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n%2==0:
        print(2)
        print(1,n)
        print(1,n)
    else:
        temp=a[0]
        for i in range(0,n):
            temp ^=a[i]
        if temp==0:
            print(1)
            print(1,n)
        else:
            for i in range(1,n-1):
                left = 0
                for j in range(0,i):
                    left ^=a[j]
                right = 0
                for j in range(i,n):
                    right^=a[j]
                
                if left == right:
                    print(3)
                    print(1,i-1)
                    print()
                    
                
                
            
            