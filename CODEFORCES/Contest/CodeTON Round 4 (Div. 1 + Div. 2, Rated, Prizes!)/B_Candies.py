t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    res = 0
    if n % 2 == 0:
        print(-1)
    else:
        while n % 2 == 1:
            if n == 3:
                res += 1
                data.insert(0, 2)
                break
            else:
                temp = n//2
                if temp % 2 == 1:
                    res += 1
                    data.insert(0, 2)
                    n = n//2
                else:
                    temp = temp+1
                    res += 1
                    data.insert(0, 1)
                    n = n//2+1

        print(res)
        print(*data)
