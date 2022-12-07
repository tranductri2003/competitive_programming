a, b, c = list(map(int, input().split()))
n = int(input())

data = []
res = [-1]*(a+b+c+1)
for i in range(n):
    x, y, z, t = list(map(int, input().split()))
    if t == 1:
        res[x] = 1
        res[y] = 1
        res[z] = 1
    else:
        data.append((x, y, z))

for i in range(len(data)):
    temp = []
    for num in data[i]:
        if res[num] != 1:
            temp.append(num)
    data[i] = temp

new = []
for i in range(len(data)):
    temp = data[i]
    if len(temp) == 1:
        res[temp[0]] = 0
    else:
        new.append(temp)

for i in range(1, a+b+c+1):
    if res[i] == -1:
        print(2)
    else:
        print(res[i])
