t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = list(map(int, input().split()))
    best = 0
    currentVal = 0
    for i in range(n):
        if a[i] <= 10:
            if b[i] > currentVal:
                best = i+1
                currentVal = b[i]

    print(best)
