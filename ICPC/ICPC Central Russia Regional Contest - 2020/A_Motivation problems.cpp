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
const int N = 100005;
int n, k, m = 0;
vector<int> g[N];
vector<int> siz(N), h(N), tour(2 * N), st(N), en(N);
vector<pair<int, int>> ans;
void dfs(int u, int p)
{
    h[u] = h[p] + 1;
    siz[u] = 1;
    tour[++m] = u;
    st[u] = m;
    for (auto v : g[u])
    {
        dfs(v, u);
        siz[u] += siz[v];
    }
    if (siz[u] >= k)
    {
        ans.pb({h[u], u});
    }
    en[u] = m;
}
void solve()
{
    cin >> n >> k;
    for (int i = 2; i <= n; i++)
    {
        int x;
        cin >> x;
        g[x].pb(i);
    }
    dfs(1, 0);
    sort(ans.begin(), ans.end());
    int len = ans.size();
    int j = st[ans[len - 1].se];
    while (k--)
    {
        cout << tour[j++] << ' ';
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int test = 1;
    // cin>>test;
    while (test--)
    {
        solve();
    }
    return 0;
}