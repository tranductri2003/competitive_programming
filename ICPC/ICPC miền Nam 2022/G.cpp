#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
const int mxN = 1e4 + 7;
int a[mxN];
bool vis[mxN];
vector<int> adj[mxN];
vector<int> comp[mxN];
int path[mxN];
void dfs(int x, vector<int> &pos)
{
    if (vis[x])
        return;
    vis[x] = true;
    pos.push_back(x);
    for (int u : adj[x])
    {
        dfs(u, pos);
    }
}

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < m; ++i)
    {
        int u, v;
        cin >> u >> v;
        u--, v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (int i = 0; i < n; ++i)
    {
        vector<int> pos;
        dfs(i, pos);
        for (int x : pos)
        {
            path[x] = i;
            comp[i].push_back(a[x]);
        }
        sort(comp[i].begin(), comp[i].end());
    }
    vector<int> h(1, 0);
    for (int i = 0; i < n; ++i)
    {
        int p = path[i];
        if (p == -1)
        {
            if (h.empty())
                h.push_back(a[i]);
            else
            {
                auto p = lower_bound(h.begin(), h.end(), a[i]);
                if (p == h.end())
                    h.push_back(a[i]);
                else
                    *p = a[i];
            }
        }
        else
        {
            vector<pair<int, int>> alter;
            int m = h.size();
            auto st = comp[p].begin();
            for (int i = 0; i < m; ++i)
            {
                auto it = lower_bound(comp[p].begin(), comp[p].end(), h[i]);
                if (it != comp[p].begin() && it != st)
                {
                    alter.push_back({i, *--it});
                    st = ++it;
                }
            }
            auto it = upper_bound(comp[p].begin(), comp[p].end(), h[m - 1]);
            if (it != comp[p].end())
            {
                h.push_back(*it);
            }
            for (auto p : alter)
            {
                h[p.first] = p.second;
            }
        }
    }
    cout << h.size() - 1;
    return 0;
}