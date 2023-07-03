t = int(input())
for _ in range(t):
    n, time = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = -1
    currentVui = 0
    for i in range(n):
        if time >= a[i]:
            if b[i] > currentVui:
                currentVui = b[i]
                res = i+1
        time -= 1
    print(res)
