
N, M = list(map(int, input().split()))
s = list(map(int, input().split()))
q = [0]*M
for _ in range(M):
    q[_] = int(input())
res = [0]*M
for i in range(N):
    for j in range(M):
        if s[i] > q[j]:
            res[j] += q[j]
        else:
            res[j] += s[i]

for num in res:
    print(num)
