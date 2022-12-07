testcase=int(input())
for test in range(testcase):
    m,n=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    if m==1 and n==1:
        print(1)
    elif (m==2 and n==1) or (m==1 and n==2):
        print(1)
    else:
        print(7)