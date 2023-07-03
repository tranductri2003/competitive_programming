from random import randint

from collections import defaultdict


def solveTri(n, a):
    previous = defaultdict(lambda: -1)
    dp = [-1]*n
    dp[0] = 1
    previous[a[0]] = 1
    for i in range(1, n):
        if previous[a[i]] == -1:  # chua co
            dp[i] = dp[i-1]+1
            previous[a[i]] = dp[i]
        else:
            dp[i] = min(max(previous[a[i]]-1, 0), dp[i-1]+1)
            previous[a[i]] = dp[i]
    # print(dp)
    return (n-dp[-1])


def solveSon(n, a):
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
    return (dp[-1])


for i in range(100):
    n = randint(1, 5)
    a = []
    for i in range(n):
        a.append(randint(1, 5))

    if solveTri(n, a) != solveSon(n, a):
        print(n)
        print(a)
        break
