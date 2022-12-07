n, k = list(map(int, input().split()))
a = [0]*(n+1)

l = 0
r = 0


def check(x):
    dem = 0
    for i in range(1, n+1):
        dem += a[i]//x
    return dem >= k


r = sum(a)/k
temp = list(map(float, input().split()))
for i in range(1, n+1):
    a[i] = temp[i-1]
    r = max(r, a[i])

while l <= r:
    mid = (l+r)/2
    if check(mid):
        l = mid
    else:
        r = mid
    if abs(l-r) <= 0.0000001:
        break

res = l
if "." not in str(res):
    res = str(res)+'.00'
    print(res)
else:
    office = (format(res, ".2f"))
    print(office)

    # print(res[:vitri+3])
