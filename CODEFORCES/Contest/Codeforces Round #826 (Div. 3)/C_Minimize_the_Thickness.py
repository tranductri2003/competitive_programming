def timuoc(n):
    data = []
    for i in range(1, n+1):
        if i**2 > n:
            break
        elif i**2 == n:
            data.append(i)
            break
        else:
            if n % i == 0:
                data.append(i)
                data.append(n//i)
    data.sort()
    return data


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    tong = sum(a)
    uoc = timuoc(tong)
    stop = False
    data = []
    for num in uoc:
        stack = 0

        for i in range(n):
            stack += a[i]
            if stack == num:
                stack = 0
            elif stack > num:
                break
        else:
            data.append(num)
    if stop == True:
        print(n)
    else:
        res = []
        for num in data:
            stack = 0
            count = 0
            temp = 0
            for i in range(n):
                stack += a[i]
                count += 1
                if stack == num:
                    stack = 0
                    temp = max(temp, count)
                    count = 0
            res.append(temp)
        print(min(res))
