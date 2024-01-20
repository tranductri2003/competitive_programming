#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define int long long
#define pb push_back
const int N = 1e5 + 3;
ll n;
ll a[N];
vector<ll> path[105];
ll dp[105][105][105], ind[N];
ll GCD(ll i, ll j)
{
    if (i == 0 || j == 0)
        return i + j;
    return GCD(j, i % j);
}
void Input()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
}
void solve()
{
    ll mod = 2023;
    for (int i = 1; i <= n; i++)
    {
        ind[a[i]] = i;
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = i + 1; j <= n; j++)
        {
            if (GCD(a[i], a[j]) == 1)
            {
                path[i].pb(j);
            }
        }
    }

    for (int i = 1; i <= n; i++)
        dp[i][i][1] = 1;

    for (int k = 2; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = i + 1; j <= n; j++)
            {
                for (auto i2 : path[i])
                {
                    if (i2 > j)
                        break;
                    dp[i][j][k] += dp[i2][j][k - 1];
                }
                dp[i][j][k] %= 2023;
            }
        }
    }
    ll q;
    cin >> q;
    for (int i = 1; i <= q; i++)
    {
        ll ai, aj, k;
        cin >> ai >> aj >> k;
        ai = ind[ai];
        aj = ind[aj];
        cout << dp[ai][aj][k + 1] << endl;
    }
    // cout << dp[1][4][3] << endl;
}

int32_t main()
{
    // if (fopen("input.txt", "r"))
    // {
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // }
    int t = 1;
    // cin >> t;
    while (t--)
    {
        Input();
        solve();
    }
}
