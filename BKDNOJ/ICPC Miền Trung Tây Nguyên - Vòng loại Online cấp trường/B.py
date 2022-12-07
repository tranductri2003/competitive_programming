n, k = list(map(int, input().split()))
data = []
soso0 = 0

for i in range(k):
    temp = int(input())
    if temp == 0:
        soso0 += 1
    else:
        data.append(temp)
data.sort()
print(data)
