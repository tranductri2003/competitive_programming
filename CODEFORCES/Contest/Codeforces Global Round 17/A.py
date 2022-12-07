testcase=int(input())

for test in range(testcase):
    n,m=list(map(int,input().split()))
    if m==1 and n==1:
        print(0)
    
    elif m==1 or n==1:
        print(1)
    else:
        print(2)
    
        
        


