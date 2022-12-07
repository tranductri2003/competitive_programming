    dp[1] = 1
    for i in range(2, n+1):
        if check[i] == 0:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1]+dp[i-2]) % (14062008)
    print(dp[n])
