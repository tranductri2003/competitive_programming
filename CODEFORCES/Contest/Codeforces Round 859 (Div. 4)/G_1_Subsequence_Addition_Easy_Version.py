t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    if c[0] != 1:
        print("NO")
    else:
        temp = 1
        for i in range(1, n):
            if c[i] > temp:
                print("NO")
                break
            else:
                temp += c[i]
        else:
            print("YES")
