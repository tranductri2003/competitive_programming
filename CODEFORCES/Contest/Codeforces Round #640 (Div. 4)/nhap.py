

n,m,k=list(map(int,input().split()))

dp=[0]*(n*m+1)


a=[]
aa=[]
for i in range(n+1):
    a.append([])
    aa.append([])
z=0
for i in range(1,n+1):
    a[i]=list(map(int,input().split()))
    aa[i]=a[i].copy()
    


for i in range(1,n*m+1):
    so_con_lai_MAX=-10**9
    so_o_cuoi_MIN=10**9 
    vi_tri_MIN=-1
    tong_cap_MAX=-10**9
    vi_tri_MAX=-1
    vi_tri_cap=-1
    for j in range(1,n+1):
        t=len(a[j])
        
        if t==0:  #đã hết
            if aa[j][-1]<so_o_cuoi_MIN:
                so_o_cuoi_MIN=aa[j][-1]
                vi_tri_MIN=j
                
        elif t!=m:  #chưa hết
            if aa[j][m-t-1]<so_o_cuoi_MIN:
                so_o_cuoi_MIN=aa[j][m-t-1]
                vi_tri_MIN=j
                
            if aa[j][m-t]>so_con_lai_MAX:
                so_con_lai_MAX=aa[j][m-t]
                vi_tri_MAX=j
                
            if m-t+1<m:
                if (aa[j][m-t]+aa[j][m-t+1])>tong_cap_MAX:
                    tong_cap_MAX = aa[j][m-t]+aa[j][m-t+1]
                    vi_tri_cap=j
    
    if dp[i-1]+so_con_lai_MAX>dp[i-1]-so_o_cuoi_MIN+tong_cap_MAX:
        dp[i]=dp[i-1]+so_con_lai_MAX
        a[vi_tri_MAX].pop(0)
    else:
        dp[i]=dp[i-1]-so_o_cuoi_MIN+tong_cap_MAX
        a[vi_tri_cap].pop(0)
        a[vi_tri_cap].pop(0)

        t=len(a[vi_tri_MIN])
        a[vi_tri_MIN].append(aa[vi_tri_MIN][-(t+1)])
    print(dp)
print(dp[k])
            
    


