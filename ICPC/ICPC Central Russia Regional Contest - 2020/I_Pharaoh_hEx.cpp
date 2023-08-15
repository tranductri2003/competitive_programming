#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define pb push_back
const ll inf = 1e18;
const long double esp = 1e-12;
const ll mod = 1e9 + 7;
using namespace std;
using namespace __gnu_pbds;
#define ordered_set tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>
const int N = 100000;
vector<bool> isPrime(N + 5, false);
vector<int> prime;
void solve()
{
    ll n, m;
    cin >> n;
    m = n;
    vector<int> odd;
    for (auto i : prime)
    {
        if (m % i == 0)
        {
            int cnt = 0;
            while (m % i == 0)
            {
                cnt++;
                m /= i;
            }
            if (cnt % 2 == 1)
            {
                odd.pb(i);
            }
        }
    }
    if (m != 1)
    {
        odd.pb(m);
    }
    ll t = 1;
    for (auto x : odd)
    {
        t *= x;
    }
    ll a = n / t;
    ll b = (ll)(sqrt(a)) + 1;
    cout << b * b * t - n << '\n';
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    for (int i = 2; i * i <= N; i++)
    {
        if (!isPrime[i])
        {
            for (int j = i * i; j <= N; j += i)
                isPrime[j] = true;
        }
    }
    for (int i = 2; i <= N; i++)
    {
        if (!isPrime[i])
            prime.pb(i);
    }
    // for (int i=0; i<10; i++) cout << prime[i] <<' ';
    int test = 1;
    // cin>>test;
    while (test--)
    {
        solve();
    }
    return 0;
}