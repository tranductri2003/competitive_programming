n = int(input())
m = int(input())

res = [i for i in range(1, 2*n+1)]
for _ in range(m):
    t = int(input())
    if t == 0:
        temp = []
        j = 0
        k = n
        for i in range(n):
            temp.append(res[j])
            temp.append(res[k])
            j += 1
            k += 1
        res = temp.copy()
    else:
        res = res[t:2*n]+res[0:t]
for num in res:
    print(num)
