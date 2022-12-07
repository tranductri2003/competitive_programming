from collections import defaultdict
x, k = list(map(int, input().split()))
a = list(map(int, input().split()))


# dp = defaultdict(lambda: -1)

# dp[0] = 0
# for i in range(0, x):
#     if dp[i] == 0:
#         for num in a:
#             dp[i+num] = 1
#     else:
#         for num in a:
#             dp[i+num] = 0

# if dp[x] == 1:
#     print("Tuan")
# else:
#     print("Hao")


dp = defaultdict(lambda: -1)


def query(x, k):
    if dp[x] != -1:
        return dp[x]

    u = 1
    for i in range(0, k):
        if x-a[i] >= 0:
            u &= query(x-a[i], k)

    if u == 1:
        dp[x] = 0
    else:
        dp[x] = 1


dp[0] = 0

query(x, k)

# print(dp)
if dp[x] == 1:
    print("Tuan")
else:
    print("Hao")
