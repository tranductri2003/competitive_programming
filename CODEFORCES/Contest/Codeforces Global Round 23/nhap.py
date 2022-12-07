import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
res = 1
for num in a:
    res *= num

for i in range(n):
    temp = 1
    for j in range(n):
        if j != i:
            temp *= a[j]
    res = max(res, temp)
print(res % (10**9+7))
