n, m = list(map(int, input().split()))  # n doi m bai
a = list(map(int, input().split()))
res = [0]*(n+1)
for i in range(n):
    b = list(map(int, input().split()))
    for j in range(m):
        if b[j] == a[j]:
            res[i+1] += 1

temp = max(res)
for i in range(1, n+1):
    if res[i] == temp:
        print(i)
        break
