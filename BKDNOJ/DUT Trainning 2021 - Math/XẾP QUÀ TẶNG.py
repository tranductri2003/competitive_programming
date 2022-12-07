testcase=int(input())
M=10**9+7


for test in range(testcase):
    n=int(input())
    ans=(2*(n**2)-n)%M
    print(ans)
    #ans=((n%M)*((2*(n-1)+1)%M))%M
    #print(ans)

