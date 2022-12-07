t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    solon=max(a)
    for i in range(n):
        if a[i]==solon:
            left=i
            break
        
    if a[:left+1]==sorted(a[:left+1]) and a[left:]==sorted(a[left:],reverse=True):
        print("YES")
    else:
        print("NO")
    # for i in range(n-1,-1,-1):
    #     if a[i]==solon:
    #         right=i
    # #         break
    # print(left,right)
    # for j in range(left,right):
    #     if a[j]!=solon:
    #         print("NO")
    #         break
    # else:
    #     check1=True
    #     for i in range(left):
    #         if a[i]>a[i+1]:
    #             print("NO")
    #             check1=False
    #             break
        
    #     check2=True
    #     for i in range(n-1,right,-1):
    #         if a[i]>a[i-1]:
    #             print("NO")
    #             check2=False
    #             break
        
    #     if check1==True and check2==True:
    #         print("YES")
        

