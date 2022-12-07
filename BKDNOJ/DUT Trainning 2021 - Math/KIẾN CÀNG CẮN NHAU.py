
testcase=int(input())

for test in range(testcase):
    N=int(input())
    res=pow(2,1-N,10**9+7)
    print(res)

"""
#include<bits/stdc++.h>

using namespace std;

const long long MOD=1e9+7;

long long pw(long long a, long long b){
    if (b==0) return 1;
    long long m=pw(a,b/2) % MOD;
    if (b%2==0) return m*m %MOD;
    return m*m % MOD * a %MOD;
}

long long mod(long long a){
    return pw(a,MOD-2);
}

void solve(){
    long long t;
    cin>>t;
    
    long long res;
    long long count;
    count = pw(2,t);
    res= mod(count);
    res=res*2%MOD;
    cout<<res<<endl;
    
}
int main(){
    int t;
    cin>>t;
    for (int i =0 ; i<t;i++){
        solve();
    }
    return 0;
}
"""