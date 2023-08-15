#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define pb push_back
const ll inf = 1e18;
const long double esp = 1e-12;
const ll mod = 1e9 + 7;
using namespace std;
#define ordered_set tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>
const int N = 100005;
int n, m, s, k;
vector<pair<int, ll>> g[N];
pair<ll, pair<int, int>> x;
ll dp[N][8];
int f(int x, int y)
{
    if (x < y)
        return y - x;
    else
        return 7 - x + y;
}
void Dijstra()
{
    set<pair<ll, pair<int, int>>> st;
    x.fi = dp[s][1];
    x.se.fi = 1;
    x.se.se = s;
    st.insert(x);
    while (st.size())
    {
        pair<ll, pair<int, int>> u = *st.begin();
        st.erase(*st.begin());
        for (auto v : g[u.se.se])
        {
            if (dp[v.fi][v.se] > f(u.se.fi, v.se) + dp[u.se.se][u.se.fi])
            {
                dp[v.fi][v.se] = ((u.se.se == s) ? v.se : f(u.se.fi, v.se)) + dp[u.se.se][u.se.fi];
                x.fi = dp[v.fi][v.se];
                x.se.fi = v.se;
                x.se.se = v.fi;
                st.insert(x);
            }
        }
    }
}
void solve()
{
    cin >> n >> m >> s >> k;
    for (int i = 1; i <= m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        g[u].pb({v, w});
        g[v].pb({u, w});
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            dp[i][j] = inf;
        }
    }
    dp[s][1] = 0;
    Dijstra();
    ll ans = inf;
    for (int i = 1; i <= 7; i++)
    {
        ans = min(ans, dp[k][i]);
    }
    cout << ans;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int test = 1;
    while (test--)
    {
        solve();
    }
    return 0;
}