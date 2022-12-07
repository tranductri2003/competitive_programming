N = int(input())
a = list(map(int, input().split()))
res = []
for num in a:
    res.append(N+1-num)

print(*res)
