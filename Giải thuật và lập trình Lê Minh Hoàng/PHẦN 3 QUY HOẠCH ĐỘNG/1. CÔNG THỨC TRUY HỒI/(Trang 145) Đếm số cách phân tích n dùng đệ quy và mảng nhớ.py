v=int(input())
dp=[]
for i in range(0,v+1):
    dp.append([])
    for j in range(0,v+1):
        dp[i].append([])



def dequy(m,v):
    if dp[m][v]!=[]:
        return dp[m][v]
    else:
        if m==0:
            if v==0:
                dp[m][v]=1
                return 1
            else:
                dp[m][v]=0
                return 0
        else:
            if m>v:
                dp[m][v]= dequy(m-1,v)
                return dp[m][v]    #Phải trả về kết quả để xử lý

            else:
                dp[m][v]= dequy(m-1,v)+dequy(m,v-m)
                return dp[m][v]
        
print(dequy(v,v))