n, k = list(map(int, input().split()))
res = 2**(k-1)*(n-k+1) % (10**9+7)
print(res)
