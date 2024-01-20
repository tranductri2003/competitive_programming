n,m = list(map(int,input().split()))
print((n-m+1)*(n+1)**(m-1)%998244353)