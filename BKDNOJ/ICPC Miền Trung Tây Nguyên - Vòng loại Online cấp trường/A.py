n, k = list(map(int, input().split()))
data = []
for i in range(n):
    temp = int(input())
    data.append(temp)

pre = [0]
temp = 0
for num in data:
    temp += num
    pre.append(temp)

res = -10**9
for i in range(k, n+1):
    res = max(res, pre[i]-pre[i-k])
print(res)
