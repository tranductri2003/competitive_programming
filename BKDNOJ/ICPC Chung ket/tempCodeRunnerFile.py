n = int(input())
data = []
for i in range(1, n+1):
    t = int(input())
    if i % 2 == 1:
        if data == []:
            data.append((1, t))
        elif data[-1][1] == t:
            temp = data[-1][0]
            data.pop()
            data.append((temp+1, t))
        else:
            data.append((1, t))
    else:
        if data == []:
            data.append((1, t))
        else:
            temp = data[-1][0]
            data.pop()
            data.append((temp+1, t))

res = 0
for num in data:
    if num[1] == 0:
        res += num[0]
print(res)
