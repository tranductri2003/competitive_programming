def build(s, e, i, a):
    if s == e:
        segT[i] = a[s]
        return
    mid = s + (e - s) // 2
    build(s, mid, 2 * i + 1, a)
    build(mid + 1, e, 2 * i + 2, a)
    segT[i] = segT[2 * i + 1] & segT[2 * i + 2]

def range_query(s, e, i, qs, qe):
    if qs <= s and qe >= e:
        return segT[i]
    if qs > e or qe < s:
        return 10**9  # Sử dụng một số nguyên lớn thay cho float('inf')
    mid = s + (e - s) // 2
    l = range_query(s, mid, 2 * i + 1, qs, qe)
    r = range_query(mid + 1, e, 2 * i + 2, qs, qe)
    return l & r

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    query = int(input())
    segT = [0] * (4 * n)
    build(0, n - 1, 0, a)
    while query > 0:
        st, k = map(int, input().split())
        st -= 1
        h = n - 1
        l = st
        ans = -1
        while l <= h:
            mid = l + (h - l) // 2
            scanner_pay_me = range_query(0, n - 1, 0, st, mid)
            if scanner_pay_me >= k:
                l = mid + 1
                ans = mid
            else:
                h = mid - 1
        if ans >= 0:
            ans += 1
        print(ans, end=" ")
        query -= 1
    print()
