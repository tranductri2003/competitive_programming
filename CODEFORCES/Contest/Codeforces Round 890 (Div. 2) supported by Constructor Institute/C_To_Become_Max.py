def check(mid, expected, initial, n, k):
    ans = 10**9
    for i in range(n - 1):
        temp = mid
        difference = 0
        for j in range(i, n):
            if expected[j] >= temp and initial[j] < temp:
                difference += abs(initial[j] - temp)
                temp -= 1
            elif initial[j] >= temp:
                break
            elif expected[j] < temp:
                difference += 10**9
                break
        ans = min(ans, difference)
    return ans <= k



t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    expected = a[:]
    for i in range(n - 2, -1, -1):
        if expected[i] <= expected[i + 1]:
            expected[i] = expected[i + 1] + 1
    low = max(a)
    high = max(expected)
    ans = max(a)
    while low <= high:
        mid = low + (high - low) // 2
        if check(mid, expected, a, n, k):
            low = mid + 1
            ans = max(ans, mid)
        else:
            high = mid - 1
    print(ans)
