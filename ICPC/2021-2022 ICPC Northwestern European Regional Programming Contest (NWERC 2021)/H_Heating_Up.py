
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

attemped = set()
l = 0
r = max(a)


def checkPossible(initialValue, initialIndex):
    left = initialIndex
    right = (initialIndex+1) % n
    for i in range(0, n):
        if a[left] <= initialValue:
            initialValue += a[left]
            attemped.add(left)
            left = (left-1+n) % n
        elif a[right] <= initialValue:
            initialValue += a[right]
            attemped.add(right)
            right = (right+1+n) % n
        else:
            return False
    return True


def possible(initialValue):
    attemped.clear()
    for i in range(n):
        if i not in attemped and checkPossible(initialValue, i):
            return True
    return False


while l <= r:
    m = (l+r)//2
    if possible(m):
        r = m-1
    else:
        l = m+1

print(l)


"""
n = int(input())
a = list(map(int, input().split()))
v = [(a[i], i+1) for i in range(n)]
v.sort()

def check(mid):
    vis = [False] * (n+1)
    for j in range(1, n+1):
        if mid < v[j-1][0]:
            return False
        elif not vis[v[j-1][1]]:
            i = v[j-1][1]
            vis[v[j-1][1]] = True
            l = i - 1
            r = i + 1
            if l <= 0:
                l += n
            if r > n:
                r %= n
            count = mid + a[i-1]
            ch = True
            while l != r:
                kt_temp = False
                if count >= a[l-1]:
                    vis[l] = True
                    count += a[l-1]
                    kt_temp = True
                    l -= 1
                    if l <= 0:
                        l = n
                elif count >= a[r-1]:
                    count += a[r-1]
                    vis[r] = True
                    kt_temp = True
                    r += 1
                    if r > n:
                        r %= n
                if not kt_temp:
                    ch = False
                    break
            if ch and count >= a[l-1]:
                return True
    return False

l = 0
r = 10**13
while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1

mid = (l + r) // 2
if mid < 0:
    mid = 0
while not check(mid):
    mid += 1
while mid - 1 >= 0 and check(mid - 1):
    mid -= 1

print(mid)

"""
