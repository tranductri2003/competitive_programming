testcase=int(input())

for test in range (0,testcase):
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split())) 
    b=sorted(a) 
    for i in range(0,n):
        if a[i]!=b[i]:
            if n-1-i<x and i<x:
                print("NO")
                break   
    else:
        print("YES")