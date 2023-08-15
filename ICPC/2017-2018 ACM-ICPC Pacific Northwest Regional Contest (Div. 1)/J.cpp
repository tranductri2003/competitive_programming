#include <bits/stdc++.h>

using namespace std;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define pf push_front
#define pof pop_front
typedef long long ll;
typedef pair<ll, ll> pll;
typedef long double ld;
const ll NMAX = 1e9;
const ll N = 30;
const ll oo = 1e18;
const ll MOD = 998244353;
char a[N + 10][N + 10];
ll dp[N + 10][N + 10][3];
void tomau(ll x, ll y)
{
    for (ll i = 1; i <= x; i++)
    {
        for (ll j = 1; j <= y; j++)
        {
            if (a[i][j] == 'R')
            {
                cout << 0 << endl;
                return;
            }
            else
                a[i][j] = 'B';
        }
    }
}
void solve()
{
    ll n, m;
    cin >> n >> m;
    for (ll i = 1; i <= n; i++)
    {
        for (ll j = 1; j <= m; j++)
        {
            cin >> a[i][j];
        }
    }
    for (ll i = 1; i <= n; i++)
    {
        for (ll j = 1; j <= m; j++)
        {
            if (a[i][j] == 'B')
                tomau(i, j);
        }
    }
    for (ll i = 1; i <= n; i++)
    {
        for (ll j = 1; j <= m; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    if (a[1][1] == '.')
    {
        dp[1][1][1] = 1;
        dp[1][1][0] = 1;
    }
    if (a[1][1] == 'R')
    {
        dp[1][1][0] = 1;
    }
    if (a[1][1] = 'B')
    {
        dp[1][1][1] = 1;
    }
    for (ll i = 1; i <= n; i++)
    {
        for (ll j = 1; j <= m; j++)
        {
            if (i != 1 || j != 1)
            {
                if (a[i][j] == 'B')
                {
                    dp[i][j][1] = dp[i - 1][j][1] + dp[i][j - 1][1] - dp[i - 1][j - 1][1];
                    dp[i][j][0] = 0;
                }
                if (a[i][j] == 'R')
                {

                    dp[i][j][0] = (dp[i - 1][j][1] + dp[i][j - 1][1] - dp[i - 1][j - 1][1]) * (dp[i - 1][j][1] + dp[i][j - 1][1] > 0);
                    dp[i][j][0] += (dp[i - 1][j][0] + dp[i][j - 1][0] - dp[i - 1][j - 1][0] - dp[i - 1][j - 1][1]) * ((dp[i - 1][j][0] + dp[i][j - 1][0] > 0));
                    ll tmp = 1;
                    for (ll k = 1; k <= i - 2; k++)
                    {
                        if (a[k][j] == '.')
                            tmp *= 2;
                    }
                    if (a[i - 1][j] == 'B')
                        tmp = 0;
                    dp[i][j][0] += tmp * dp[i][j - 1][1] * (i > 1);
                    tmp = 1;
                    for (ll k = 1; k <= j - 2; k++)
                    {
                        if (a[i][k] == '.')
                            tmp *= 2;
                    }
                    if (a[i][j - 1] == 'B')
                        tmp = 0;
                    dp[i][j][0] += tmp * dp[i - 1][j][1] * (j > 1);
                }
                if (a[i][j] == '.')
                {
                    // case 1 : tren B trai B
                    dp[i][j][0] = (dp[i - 1][j][1] + dp[i][j - 1][1] - dp[i - 1][j - 1][1]) * (dp[i - 1][j][1] + dp[i][j - 1][1] > 0);
                    dp[i][j][0] += (dp[i - 1][j][0] + dp[i][j - 1][0] - dp[i - 1][j - 1][0] - dp[i - 1][j - 1][1]) * (dp[i - 1][j][0] + dp[i][j - 1][0] > 0);
                    ll tmp = 1;
                    for (ll k = 1; k <= i - 2; k++)
                    {
                        if (a[k][j] == '.')
                            tmp *= 2;
                    }
                    if (a[i - 1][j] == 'B')
                        tmp = 0;
                    dp[i][j][0] += tmp * dp[i][j - 1][1] * (i > 1);
                    tmp = 1;
                    for (ll k = 1; k <= j - 2; k++)
                    {
                        if (a[i][k] == '.')
                            tmp *= 2;
                    }
                    if (a[i][j - 1] == 'B')
                        tmp = 0;
                    dp[i][j][0] += tmp * dp[i - 1][j][1] * (j > 1);
                    dp[i][j][1] = dp[i - 1][j][1] + dp[i][j - 1][1] - dp[i - 1][j - 1][1];
                }
            }
        }
    }
    if (a[n][m] == 'R')
        cout << dp[n][m][0];
    if (a[n][m] == 'B')
        cout << dp[n][m][1];
    if (a[n][m] == '.')
        cout << dp[n][m][0] + dp[n][m][1];
}
int main()
{
    int test;
    test = 1;
    ios_base ::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    // #ifndef ONLINE_JUDGE
    //     freopen("D.inp", "r", stdin);
    //     freopen("D.out", "w", stdout);
    // #endif

    // cin >> test;
    while (test--)
    {
        solve();
    }
}