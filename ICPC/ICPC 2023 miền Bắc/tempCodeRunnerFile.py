n = int(input())
res = n*(n-3)//2+1+1/24*n**4-1/4*n**3+11/24*n**2-1/4*n
print(round(res)% 987654321)