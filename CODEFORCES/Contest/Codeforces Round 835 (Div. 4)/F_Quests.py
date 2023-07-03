def check(k, c, d):
    inkday = 0

    for i in range(n-1, max(-1, n-1-k-1), -1):
        inkday += a[i]
    if c % inkday == 0:
        time = (c//inkday-1)*(k+1)
        rest = c-(c//inkday-1)*inkday
        i = n-1
        while rest > 0:
            rest -= a[i]
            i -= 1
            time += 1
    else:
        time = c//inkday*(k+1)
        rest = c-c//inkday*inkday
        i = n-1
        while rest > 0:
            rest -= a[i]
            i -= 1
            time += 1

    if time <= d:
        return True
    else:
        return False


t = int(input())
for _ in range(t):
    n, c, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    res = 10**16
    if c <= a[-1]:
        print("Infinity")
    elif c > a[-1]*d:
        print("Impossible")
    else:
        l = 0
        r = 10**16
        while l <= r:
            mid = (l+r)//2
            if check(mid, c, d):
                l = mid+1
                res = mid
            else:
                r = mid-1
        if res == 10**16:
            print("Infinity")
        else:
            print(res)
