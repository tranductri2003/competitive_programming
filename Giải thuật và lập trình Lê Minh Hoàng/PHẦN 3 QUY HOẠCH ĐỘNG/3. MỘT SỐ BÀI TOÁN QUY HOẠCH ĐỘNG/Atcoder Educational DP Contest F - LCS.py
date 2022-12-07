a=str(input())
b=str(input())

a=str(1)+a
b=str(1)+b

dp=[]
for i in range(0,len(a)):
    dp.append([])
    for j in range(0, len(b)):
        dp[i].append([])

for i in range(0, len(b)):
    dp[0][i]=0

for i in range(0, len(a)):
    dp[i][0]=0
#dp[i][j]: dãy con dài nhất tính đến phần tử thứ i của dãy 1 và phần tử thứ j của dãy 2
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

"""for i in range(0, len(a)):
    print(dp[i])
"""
max=dp[len(a)-1][len(b)-1]

i=len(a)-1
j=len(b)-1
res=list()

while i*j!=0:  #Nếu số thứ tự của ký tự một trong hai dãy về 0 thì end luôn
    if a[i]==b[j]:
        res.append(a[i])
        i-=1
        j-=1
    elif dp[i-1][j]>dp[i][j-1]:
        i-=1
    else:
        j-=1

res.reverse()
for i in res:
    print(i, end="")
