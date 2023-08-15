t = int(input())
for _ in range(t):
    n, m, k, H = list(map(int, input().split()))
    h = list(map(int, input().split()))
    res = 0
    for num in h:
        if abs(num-H) % k == 0 and abs(num-H)//k <= m-1 and num != H:
            res += 1
    print(res)
