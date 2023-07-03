MAX = 1000000  # Maximum value of D can be 10^6

t = int(input())

dp = [float('inf')] * (MAX + 1)  # initialise dp[i] with infinity
# Here dp[i] = min. number of days to make the charges i on a single day.

dp[1] = 1  # Initial charge is Rs. 1, so no extra days required

for i in range(2, MAX + 1):
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i - 1 >= 1:
        dp[i] = min(dp[i], dp[i - 1] + 1)

for _ in range(t):
    n = int(input())

    # minimum number of days to make the charges for a single day, equal to n
    print(dp[n])

    seq = []

    # Now, perform a traceback to get the sequence of charges on each day.
    i = n
    while i > 1:
        seq.append(i)
        if i - 1 >= 1 and dp[i] == 1 + dp[i - 1]:
            i = i - 1
        elif i % 2 == 0 and dp[i] == 1 + dp[i // 2]:
            i = i // 2
        elif i % 3 == 0 and dp[i] == 1 + dp[i // 3]:
            i = i // 3

    seq.append(1)

    seq.reverse()

    print(' '.join(map(str, seq)))
