
data = [1, 1]
for i in range(60):
    data.append(data[-1]+data[-2])


t = int(input())
for _ in range(t):
    n, x, y = list(map(int, input().split()))
    while n >= 1:
        if y <= data[n-1]:
            pass
        elif y > data[n]:
            y -= data[n]
        else:
            print("NO")
            break
        x, y = y, x
        n -= 1
    else:
        print("YES")
