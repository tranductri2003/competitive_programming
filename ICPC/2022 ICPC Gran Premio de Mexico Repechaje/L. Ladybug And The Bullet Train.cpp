#include <bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ordered_set tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

const int maxN = 1e6 + 3;
vector<int> c[maxN];
int f[maxN], par[maxN];

void dfs(int u)
{
    f[u] = 0;
    for (int v : c[u])
    {
        if (par[v] == -1)
        {
            par[v] = u;
            dfs(v);
            f[u] += (f[v] + 1);
        }
    }
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, x, u, v;
    cin >> n >> x;
    memset(f, 0, sizeof(f));
    memset(par, -1, sizeof(par));
    for (int i = 1; i < n; i++)
    {
        cin >> u >> v;
        c[u].push_back(v);
        c[v].push_back(u);
    }
    if (x == 1)
    {
        cout << 0 << endl;
        return 0;
    }
    par[1] = 0;
    dfs(1);
    int ans = 1;
    x = par[x];
    while (x != 1)
    {
        ans++;
        for (int u : c[par[x]])
        {
            if (u != x && u != par[par[x]])
                ans += (2 * f[u] + 2);
        }
        x = par[x];
    }
    cout << ans << endl;

    return 0;
}