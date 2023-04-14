t = int(input())
for _ in range(t):
    n, d = list(map(int, input().split()))
    s = input()
    for i in range(0, n):
        if int(s[i]) < d:
            s = s[:i]+str(d)+s[i:]
            break
    else:
        s += str(d)
    print(s)
