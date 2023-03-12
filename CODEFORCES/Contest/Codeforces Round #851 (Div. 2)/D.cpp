#include <bits/stdc++.h>
using namespace std;
#define int long long
#define rep(i,a,b) for(int i=(a);i<(b);i++)
const int M=1e9+7;
int32_t main() {
    int n;
    cin>>n;
    vector<int> pw(n+1,1),a(n+1);
    rep(i,1,n+1) pw[i]=pw[i-1]*2%M;
    rep(i,1,n+1) cin>>a[i];
    int ans=0;
    
    rep(i,1,n+1) {
        rep(j,i+1,n+1) {
            int x=a[j]-a[i];
            int l=1,r=i-1;
            int t=1;
            while(l<r+1) {
                int m=(l+r)>>1;
                if(a[i]-a[m]<=x) r=m-1;
                else l=m+1;
            }
            t=(t*pw[r])%M;
            l=j+1,r=n;
            while(l<r+1) {
                int m=(l+r)>>1;
                if(a[m]-a[j]<x) l=m+1;
                else r=m-1;
            }
            t=(t*pw[n-l+1])%M;
            ans=(ans+t)%M;
        }
    }
    cout<<ans<<'\n';
    return 0;
}