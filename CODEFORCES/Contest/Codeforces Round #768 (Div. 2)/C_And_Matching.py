testcase=int(input())
for test in range(testcase):
    n,k=list(map(int,input().split()))
    res=0
    maxAND=0
    minAND=0
    i=n-1
    while i>=0:
        maxAND+=i&(i-1)
        i-=2
    i=0
    j=n-1
    while i<=j:
        minAND+=i&j
        i+=1
        j-=1
    if minAND>maxAND:
        minAND,maxAND=maxAND,minAND
        
    # print(minAND,maxAND)
    num0=len(bin(n-1)[2:])
    for i in range(0,n):
        print("0"*(num0-len(bin(i)[2:]))+bin(i)[2:])
        
    print("á")
        
    # if k>maxAND or k<minAND:
    #     print(-1)
    # else:
    #     if k==minAND:
    #         i=0
    #         j=n-1
    #         while i<=j:
    #             print(i,j)
    #             i+=1
    #             j-=1
    #     elif k==maxAND:
    #         i=n-1
    #         while i>=0:
    #             print(i, i-1)
    #             i-=2
    #         i=0
    #         j=n-1   
    #     else:
    #         print("as")