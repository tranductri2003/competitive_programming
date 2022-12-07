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

pair<ll, ll> a[20005];

pair<ll, ll> row[20005];
ll dp[20005][2];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    while (cin >> n)
    {

        ll minx = 1e18, miny = 1e18;
        rep(i, n)
        {
            cin >> a[i].fi >> a[i].se;
            minx = min(minx, a[i].fi);
            miny = min(miny, a[i].se);
        }
        rep(i, n)
        {
            a[i].fi -= minx;
            a[i].se -= miny;
        }
        ffor(i, 2005)
        {
            row[i].fi = 1e18;
            row[i].se = -1e18;
        }
        int maxid = -1;
        rep(i, n)
        {
            int id = a[i].se;
            row[id].fi = min(row[id].fi, a[i].fi);
            row[id].se = max(row[id].se, a[i].fi);
            maxid = max(maxid, id);
        }
        for (int i = 0; i <= maxid; i++)
        {
            ll len = row[i].se - row[i].fi + 1;
            if (i == 0)
            {
                dp[i][0] = (len + 1) / 2;
                dp[i][1] = len / 2;
                continue;
            }

            if (row[i].se == row[i - 1].fi || row[i].fi == row[i - 1].se)
            {
                if (row[i].fi == row[i - 1].se)
                {
                    int len2 = row[i - 1].se - row[i - 1].fi + 1;
                    if (len2 % 2 == 1)
                    {
                        dp[i][0] = (len + 1) / 2 + dp[i - 1][1];
                        dp[i][1] = (len) / 2 + max(dp[i - 1][1], dp[i - 1][0]);
                    }
                    else
                    {
                        dp[i][0] = (len + 1) / 2 + dp[i - 1][0];
                        dp[i][1] = (len) / 2 + max(dp[i - 1][1], dp[i - 1][0]);
                    }
                }
                else if (row[i].se == row[i - 1].fi)
                {
                    int len = row[i].se - row[i].fi + 1;
                    if (len % 2 == 1)
                    {
                        dp[i][0] = (len + 1) / 2 + dp[i - 1][1];
                        dp[i][1] = len / 2 + max(dp[i - 1][0], dp[i - 1][1]);
                    }
                    else
                    {
                        dp[i][0] = (len + 1) / 2 + max(dp[i - 1][1], dp[i - 1][0]);
                        dp[i][1] = len / 2 + dp[i - 1][1];
                    }
                }
                //  cout << dp[i][0] << ' ' << dp[i][1] << '\n';
                continue;
            }

            if (abs(row[i].fi - row[i - 1].fi) % 2 == 0)
            {
                dp[i][0] = (len + 1) / 2 + dp[i - 1][1];
                dp[i][1] = len / 2 + dp[i - 1][0];
            }
            else
            {
                dp[i][0] = (len + 1) / 2 + dp[i - 1][0];
                dp[i][1] = len / 2 + dp[i - 1][1];
            }
            // cout << dp[i][0] << ' ' << dp[i][1] << '\n';
        }
        ll res = max(dp[maxid][0], dp[maxid][1]);
        cout << res << '\n';
    }

    return 0;
}