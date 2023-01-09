
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == 1:
        print("NO")
    else:
        print("YES")
        a.sort()
        i = 0
        j = n-1
        res = []
        while i <= j:
            if i == j:
                res.append(a[i])
                break
            else:
                res.append(a[i])
                res.append(a[j])
                j -= 1
                i += 1
        print(*res)
