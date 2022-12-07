 





testcase=int(input())
for i in range(0,testcase):
    n,m,k=list(map(int,input().split()))
    if n==1:
        if m==0 and k >=2:
            print("YES")
        else:
            print("NO")
    else:
        if m<n-1 or m>n*(n-1)//2:
            print("NO")
        else:
            if m==n*(n-1)//2:
                if k>=3:
                    print("YES")
                else:
                    print("NO")
            else:
                if k>=4:
                    print("YES")
                else:
                    print("NO")