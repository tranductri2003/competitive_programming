n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
a.sort()
maxDis2Card = -10**9
minDis3Card = 10**9

for i in range(1, n+1):
    maxDis2Card = max(maxDis2Card, a[i]-a[i-1])
for i in range(2, n+1):
    minDis3Card = min(minDis3Card, a[i]-a[i-2])

if maxDis2Card >= minDis3Card:
    print(0)
else:
    print(maxDis2Card)
