l, r = list(map(int, input().split()))
temp = 1
data = []
for _ in range(1):
    res = 0
    for i in range(l, r+1):
        temp = 1
        for j in range(len(str(i))):
            temp *= int(str(i)[j])
        res = max(res, temp)
        if res == 567:
            print(i)
print(res)
