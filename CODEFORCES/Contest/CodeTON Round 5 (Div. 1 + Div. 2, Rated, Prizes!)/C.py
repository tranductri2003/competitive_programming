from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    dp = [0]*(n+1)

    last = defaultdict(lambda: 0)
    for i in range(1, n+1):
        if last[a[i]] == 0:
            dp[i] = dp[i-1]
            last[a[i]] = i
        else:
            dp[i] = dp[i-1]
            dp[i] = max(dp[i], dp[last[a[i]]-1]+i-last[a[i]]+1)

            if last[a[i]]-1-dp[last[a[i]]-1] > i-1-dp[i-1]:
                last[a[i]] = i
    print(dp[-1])
