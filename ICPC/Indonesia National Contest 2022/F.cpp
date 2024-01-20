#include<bits/stdc++.h>
#define pb push_back
#define ff first
#define ss second
#define vt vector
#define ins insert
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define make_unique(x) sort(all((x))); (x).resize(unique(all((x))) - (x).begin())
#define debug(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "
using namespace std;

typedef unsigned long ull;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;
typedef map<int, int> mii;
typedef vt<int> vti;
const double Pi = acos(- 1.0);
template<typename T>ostream& operator<<(std::ostream& os, const std::vector<T>& vec) {for(T x : vec) cout << x << ' '; cout << endl;return os;}
const int inf = INT_MAX;


void Duck(){
    ll n, p0, x;
    cin >> n >> p0 >> x;
    vt<ll> d(n);
    for(int i = 0; i < n; i++){
        cin >> d[i];
    }
    vt<ll> pre(n), tmp;
    pre[0] = d[0];
    for(int i = 1; i < n; i++){
        pre[i] = pre[i - 1] + d[i];
    }
    tmp = pre;
    //cout << pre;
    if(p0 >= x){
        int dif = p0 - x;
        int cnt = (-dif) / pre[n - 1];
        ll ans = p0;
        // work 1;
        p0 += cnt * pre[n - 1]; 
        for(int i = 0; i < n; i++){
            if(p0 + pre[i] >= x){
                ans = min(p0 + pre[i], ans);
            }
        }
        // work2
        p0 += pre[n - 1];
        for(int i = 0; i < n; i++){
            if(p0 + pre[i] >= x){
                ans = min(p0 + pre[i], ans);
            }
        }
        cout << ans;
    }else{
        cout << -1;
    }
}



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    /*Duck3*/
    int t = 1;
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
    #endif
    //cin >> t;
    while(t--) Duck();
    return 0;
}
/*
Test:

*/








