# x1 = a1
# x2 = a2
# x3 = a3
# . . .
# xk = ak
# xn = xn−1 ⊕ xn−2 ⊕ xn−3 ⊕ xn−4 . . . ⊕ xn−k, n > k


n=int(input())
a=list(map(int,input().split()))
tmp=a[0]

for i in range(1,n):
    tmp^=a[i]
a.append(tmp)
q=int(input())
for _ in range(q):
    l,r=list(map(int,input().split()))
    start=(l-1)%(n+1)
    end=(r-1)%(n+1)
    res=a[start]
    for i in range(start+1,end+1):
        res^=a[i]
    print(res)


# ll arr[200002];
# ll prefixor[200002];
# void solve(){
#     int k;
#     cin>>k;
#     ll pr=0;
#     prefixor[0]=0;
#     for (int i=1; i<=k; i++){
#         cin>>arr[i];
#         prefixor[i]=prefixor[i-1]^arr[i];
#         pr=pr^arr[i];
#     }
#     arr[k+1]=pr;
#     prefixor[k+1]=prefixor[k]^pr;
#     int n;
#     cin>>n;
#     ll l,r;
#     for (int i =0; i<n; i++){
#         cin>>l>>r;
#         l=(l-1)%(k+1) +1;
#         r=(r-1)%(k+1) +1;
        
#         cout<< (prefixor[r]^prefixor[l-1]) <<endl;
#     }
# }
        
