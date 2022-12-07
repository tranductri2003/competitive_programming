n, D = list(map(int, input().split()))
p = list(map(int, input().split()))

p.sort(reverse=True)
left = 0
right = n-1
res = 0
while left < right:
    can = D//p[left]
    if D % p[left] != 0:
        can += 1
    left += 1
    right -= can-1
    if left >= right:
        break
    res += 1
print(res)
