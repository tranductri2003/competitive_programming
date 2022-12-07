def solve(n,k):
    if k==1:
        return 1
    if k%2==0:
        return solve (n,k//2)*n%(10**9+7)
    if k%2==1:
        return solve(n,k-1)+1
    
testcase=int(input())
for i in range(0,testcase):
    n,k=list(map(int,input().split()))
    print(solve(n,k))