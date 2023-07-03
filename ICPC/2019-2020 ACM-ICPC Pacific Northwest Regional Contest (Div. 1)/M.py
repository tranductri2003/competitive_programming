R, C = list(map(int, input().split()))
data = []
for i in range(R):
    data.append([])
    for j in range(C):
        data[i].append(-1)

for i in range(R):
    s = input()
    for j in range(C):
        data[i][j] = s[j]

for i in range(R):
    print(*data[i])
