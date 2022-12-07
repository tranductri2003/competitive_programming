
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        res = [1]*n
        print(*res)
    else:
        res = [2]*(n-2)+[1]+[3]
        print(*res)
