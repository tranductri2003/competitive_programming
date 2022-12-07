INF=10**17

n,k,p=list(map(int,input().split()))  #Số người, số chìa và địa điểm office
a=list(map(int,input().split()))    #Vị trí người đứng có n số
a.sort()

b=list(map(int,input().split()))    #Vị trí khóa   có k số
b.sort()

#Sẽ gắp cặp increasing order


#dp[key][person]: Tức là tại chìa khóa thứ key, người thứ person sẽ tốn thời gian ít nhất là

dp=[]
for i in range(k+1):
    dp.append([])
    for j in range(n+1):
        dp[i].append(INF)

dp[0][0]=0

for key in range(k):
    for person in range(n+1):
        #Don't take person
        dp[key+1][person]=min(dp[key+1][person],dp[key][person])
        
        #Do take person
        if person<n:
            dp[key+1][person+1]=min(   dp[key+1][person+1],   max(    dp[key][person],  abs(a[person]-b[key])+abs(b[key]-p)))
            
print(dp[k][n])

            

        


#Do not cross
#Chỉ cần tìm được thời gian của người cuối cùng

