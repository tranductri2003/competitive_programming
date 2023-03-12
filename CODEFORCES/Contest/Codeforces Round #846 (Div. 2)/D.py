t = int(input())
for _ in range(t):
    res = 0
    while True:
        n = int(input())
        if n == 0:
            print("!", res)
            break
        else:
            print("-", 2**(n-1))
            res += (2**(n-1))
