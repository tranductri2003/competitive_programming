#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef long double ld;
#define fi first
#define se second
#define pb push_back
#define rep(i, n) for (int i = 1; i <= int(n); i++)
#define ffor(i, n) for (int i = 0; i < int(n); i++)
#define sz(x) ((int)(x).size())
#define all(x) x.begin(), x.end()

// mt19937 rng(chrono::steady_clock::now().time_since_epoch().count()); //  rng()
ll a[101];
ll dp[101][101];

ll cal(int l, int r)
{
    if (dp[l][r] != -1)
        return dp[l][r];
    int res = 0;

    // 1
    int can = 1;
    for (int i = l; i <= r; i++)
    {
        if (a[i] != 0 && a[i] != (r - l + 1))
        {
            can = 0;
        }
    }
    if (can)
        res++;

    for (int k = l + 1; k <= r; k++)
    {
        int c = 1;
        for (int i = k; i <= r; i++)
        {
            if (a[i] != 0 && a[i] != (r - k + 1))
                c = 0;
        }
        if (c)
        {
            res += cal(l, k - 1);
            res = min(res, 1000000000);
        }
    }
    dp[l][r] = res;
    return dp[l][r];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    rep(i, n) cin >> a[i];

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            dp[i][j] = -1;
        }
    }
    if (cal(1, n) == 1)
    {
        cout << "YES" << '\n';
    }
    else
        cout << "NO" << '\n';

    return 0;
}
