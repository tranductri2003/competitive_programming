t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    if n == 1000:
        print(1)
    for i in range(n-1, 0, -1):
        if a[i] == 10**19:
            pass
        else:
            if a[i] > 10**19:
                temp = a[i]-10**19
                a[i] -= temp
                a[i-1] -= temp
            else:
                temp = 10**19-a[i]
                a[i] += temp
                a[i-1] += temp

    if a[0] <= a[1]:
        print("YES")
    else:
        print("NO")
