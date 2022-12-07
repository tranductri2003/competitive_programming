n, k = list(map(int, input().split()))
a = [0]*(n+1)

l = 0
r = 0


def check(x):
    dem = 0
    for i in range(1, n+1):
        dem += a[i]//x
    return dem >= k


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
    if abs(l-r) <= 0.01:
        break

res = l
nguyen = res//1
thapphan = res % 1
thapphan = thapphan*100
if "." not in str(res):
    res = str(res)+'.00'
    print(res)
else:
    thapphan = str(thapphan[:2])
    res = str(nguyen)+'.'+str(thapphan)
    print(res)
