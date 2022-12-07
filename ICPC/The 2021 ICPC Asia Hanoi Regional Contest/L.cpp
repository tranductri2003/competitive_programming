#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
long long gcd(long long x,long long y){ if (y==0) return x; return gcd(y,(long long) x%y); }
long long lcm(long long x,long long y){ return (long long) x*y/gcd(x,y); }
long long power(long long x,long long n){long long res=1; do { if (n&1) res=(long long) (res*x); x=(long long) x*x; n/=2;} while(n); return res;}
long long power(long long x,long long n,long long mod){long long res=1; x=(long long) x%mod; do { if (n&1) res=(long long) (res*x)%mod; x=(long long) (x*x)%mod; n/=2;} while(n); return res;}



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long t;
    cin>>t;
    while (t--){
        long long n;
        cin>>n;
        string s="";
        do {
            if (n&1) s='R'+s; else s='L'+s;
            n/=2;
        } while (n!=1);
        cout<<s<<"\n";
    }
   
}