t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    for i in range(len(str(n))):
        if i == 0:
            res += int(str(n)[0])
        else:
            res += 9
    print(res)
