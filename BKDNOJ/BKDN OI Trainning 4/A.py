n = int(input())
m = int(input())
res = 0
current = m
stop = 0
for i in range(n):
    x, y = list(map(int, input().split()))  # So xe vao, so xe ra
    current = current + x - y
    res = max(res, current)
    if current < 0:
        stop = 1

if stop == 1:
    print(0)
else:
    print(res)
