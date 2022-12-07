from collections import defaultdict
N, K = list(map(int, input().split()))
data = []
for i in range(3*N):
    data.append(input())


data = data[::-1]
check = defaultdict(lambda: 0)
for num in data:
    check[num] += 1

dataa = []
time = defaultdict(lambda: 0)
for num in data:
    if time[num] == 0:
        dataa.append(num)
        time[num] += 1

res = []
for num in dataa:
    res.append((num, check[num]))
res = sorted(res, key=lambda x: x[1], reverse=True)
for i in range(min(K, len(res))):
    print(res[i][0])
