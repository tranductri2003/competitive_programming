type = int(input())
if type==1:
    n,w = list(map(int,input().split()))
    matrix =[]
    dp=[]
    for i in range(n):
        matrix.append([])
        dp.append([])
        for j in range(n):
            matrix[i].append(0)
            dp[i].append(0)
    
    for i in range(n):
        a = list(map(int,input().split()))
        for j in range(n):
            matrix[i][j] = a[j]

    if matrix[0][0]<w:
        matrix[0][0]=1
    
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                continue
            if i==0:
                dp[i][j] = dp[i][j-1]
                if matrix[i][j]<w:
                    dp[i][j] +=1
            elif j==0:
                dp[i][j] = dp[i-1][j]
                if matrix[i][j]<w:
                    dp[i][j]+=1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
                if matrix[i][j]<w:
                    dp[i][j]+=1

    
    print(dp[n-1][n-1])
                

