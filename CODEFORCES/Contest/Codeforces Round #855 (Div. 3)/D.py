t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    res = 0
    for i in range(2, n):
        if s[i] == s[i-2]:
            res += 1
    print(n-1-res)
