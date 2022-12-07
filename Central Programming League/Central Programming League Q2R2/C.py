n, m = list(map(int, input().split()))
A = [(0, 0) for i in range(0, n+1)]
B = [(0, 0)for i in range(0, m+1)]
for i in range(n):
    a, b = list(map(int, input().split()))
    A[i+1] = (a, b)

for i in range(m):
    a, b = list(map(int, input().split()))
    B[i+1] = (a, b)

res1 = 0
for i in range(2, n+1):
    d = abs(A[i][0]-A[i-1][0])+abs(A[i][1]-A[i-1][1])
    res1 += d**2


d = abs(B[1][0]-A[n][0])+abs(B[1][1]-A[n][1])
res1 += d**2

for i in range(2, m+1):
    d = abs(B[i][0]-B[i-1][0])+abs(B[i][1]-B[i-1][1])
    res1 += d**2


res2 = 0
d = abs(B[1][0]-A[1][0])+abs(B[1][1]-A[1][1])
res2 += d**2
for i in range(2, m+1):
    d = abs(B[i][0]-B[i-1][0])+abs(B[i][1]-B[i-1][1])
    res2 += d**2
d = abs(B[m][0]-A[2][0])+abs(B[m][1]-A[2][1])
res2 += d**2


for i in range(3, n+1):
    d = abs(A[i][0]-A[i-1][0])+abs(A[i][1]-A[i-1][1])
    res2 += d**2
print(min(res1, res2))
