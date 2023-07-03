N, X = list(map(int, input().split()))
a = list(map(int, input().split()))

data = []
for i in range(1, N):
    data.append(abs(a[i]-a[i-1]))

print(data)
prefixSum = [0]
temp = 0
for num in data:
    temp += num
    prefixSum.append(temp)

print(prefixSum)
