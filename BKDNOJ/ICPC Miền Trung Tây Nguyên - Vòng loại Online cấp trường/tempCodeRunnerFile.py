res = 10**9
n = int(input())

check = 1
for i in range(1, n+1):
    if i**2 > n:
        break
    if i**2 == n:
        break
    if n % i == 0:
        res = min(res, n//i)
print(res)
