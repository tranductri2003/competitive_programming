ll arr[200002];
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