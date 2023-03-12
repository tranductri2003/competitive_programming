t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    check1 = False
    for i in range(0, n-1):
        if a[i] == -1 and a[i+1] == -1:
            a[i] = 1
            a[i+1] = 1
            check1 = True
            break

    if check1 == False:
        for i in range(0, n-1):
            if (a[i] == -1 and a[i+1] == 1) or (a[i] == 1 and a[i+1] == -1):
                a[i] *= -1
                a[i+1] *= -1
                check1 = True
                break

    if check1 == False:
        for i in range(0, n-1):
            if a[i] == 1 and a[i+1] == 1:
                a[i] = -1
                a[i+1] = -1
                check1 = True
                break
    print(sum(a))
