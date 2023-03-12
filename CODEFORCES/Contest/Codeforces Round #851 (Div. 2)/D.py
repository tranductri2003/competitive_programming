t = int(input())
for _ in range(t):
    n = int(input())
    powww = [1]*(n+1)
    for i in range(1, n+1):
        powww[i] = powww[i-1]*2 % (10**9+7)
    a = list(map(int, input().split()))
    a.insert(0, 0)
    res = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            temp = a[j]-a[i]
            left = 1
            right = i-1
            bottom = 1
            while left < right+1:
                middle = (left+right)//2
                if (a[i]-a[middle]) <= temp:
                    right = middle-1
                else:
                    left = middle+1
            bottom = bottom*powww[right] % (10**9+7)
            res = (res+bottom) % (10**9+7)
    print(res)
