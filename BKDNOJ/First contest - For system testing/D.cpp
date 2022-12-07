#include <bits/stdc++.h>
using namespace std;
long long f1[1000000],f2[1000000];
long long mod=1e9+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n,d1=0,d2=0;
    cin>>n;
    vector < pair<long long,long long> > tam;
    vector <long long> v; v.push_back(-1);
    for (int i=1; i<=n; i++){
        long long x,y,z;
        cin>>x>>y>>z;
        if (x==0) d1++; else 
        if (y==0) d2++; else {
            tam.push_back({x,y});
        }
    }
    sort(tam.begin(),tam.end());
    int d=1;
    for (int i=1; i<tam.size(); i++)
    if (tam[i]==tam[i-1]) d++; else {
        v.push_back(d);
        d=1;
    }
    v.push_back(d);
    for (int i=1; i<v.size(); i++)  f1[i]=f1[i-1]+v[i];
    for (int i=v.size()-1; i>=1; i--) f2[i]=f2[i+1]+v[i];
    long long res=0;
    res=(long long) (d1*d2*(n-d1-d2))%mod;
    for (int i=1; i<v.size()-1; i++) {
        res=res + (long long) (f1[i-1]*v[i]*f2[i+1])%mod; res=res%mod;
        res=res + (long long) ((d1+d2)*v[i]*f2[i+1])%mod; res=res%mod;
    }
    cout<<res;
    
    
    //for (auto x:v) cout<<x<<" ";
}