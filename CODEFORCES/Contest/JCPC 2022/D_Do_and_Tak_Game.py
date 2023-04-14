

import random


def HuyVu(N, K):
    if (N * K) % (K+1) == 0:
        return 0
    else:
        return 1
# import sys
# sys.stdin = open("dotak.in", "r")


# @lru_cache(maxsize=100)
def cal(n, k, num):

    if num == 0:
        return 0
    if f[num] != -1:
        return f[num]
    ans = 1-cal(n, k, num-1)
    if num >= k:
        ans = max(ans, 1-cal(n, k, num-k))
    f[num] = ans
    return ans


for _ in range(int(input())):
    f = [-1]*(10001)
    n = random.randint(1, 3)
    k = random.randint(1, 3)
    if HuyVu(n, k) == cal(n, k, n*k):
        print("true")
    else:
        print(n, k, HuyVu(n, k))
        a = input()
