#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define pb push_back
const ll inf = 1e18;
const long double esp = 1e-12;
const ll mod = 1e9 + 7;
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>
const int N = 50000;
vector<ll> p(N + 1);
vector<ll> gt(N + 1);
vector<ll> k(N + 1);
ll powMod(ll a, ll b, ll m)
{
    ll res = 1;
    for (; b > 0; b >>= 1, a = a * a % m)
    {
        if (b & 1)
            res = res * a % m;
    }
    return res;
}
void solve()
{
    int n;
    cin >> n;
    ll ans = 0;
    for (int i = 0; 2 * i <= n; i++)
    {
        ll s = (((gt[i] * gt[i]) % mod) * gt[n - 2 * i]) % mod;
        s = powMod(s, mod - 2, mod);
        s = (s * gt[n]) % mod;
        s = (s * p[n - 2 * i]) % mod;
        ans = (ans + s) % mod;
    }
    ll t = powMod(2, mod - 2, mod);
    ll res = ((k[n] - ans) % mod + mod) % mod;
    res = (res * t) % mod;
    cout << res;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    p[0] = 1;
    k[0] = 1;
    for (int i = 1; i <= N; i++)
    {
        p[i] = (p[i - 1] * 2) % mod;
        k[i] = (k[i - 1] * 4) % mod;
    }
    gt[0] = 1;
    for (int i = 1; i <= N; i++)
    {
        gt[i] = (gt[i - 1] * i) % mod;
    }
    // cout << gt[4] <<' ' << p[4] <<' ' << k[4] <<'\n';
    int test = 1;
    // cin>>test;
    while (test--)
    {
        solve();
    }
    return 0;
}