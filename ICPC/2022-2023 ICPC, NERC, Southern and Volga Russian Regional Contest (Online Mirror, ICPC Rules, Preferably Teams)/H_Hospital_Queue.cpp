#include "bits/stdc++.h"
using namespace std;

int n;
vector<vector<int>> c;
vector<int> p, ans;

void dfs(int u)
{
    int max_child = 0;
    for (int v : c[u])
    {
        dfs(v);
        max_child = max(max_child, ans[v]);
    }
    int cnt = 0;
    for (int i = 1; i <= n; i++)
    {
        if (p[i] < p[u])
            cnt++;
    }
    ans[u] = max(max_child + 1, cnt + 1);
}

int main()
{

    int m, u, v;
    cin >> n >> m;
    c.resize(n + 1);
    p.resize(n + 1);
    ans.assign(n + 1, -1);
    vector<int> cnt(n + 1, 0);
    for (int i = 1; i <= n; i++)
        cin >> p[i];
    while (m--)
    {
        cin >> u >> v;
        c[v].push_back(u);
        cnt[u]++;
    }
    vector<int> root;
    for (int i = 1; i <= n; i++)
    {
        if (cnt[i] == 0)
            root.push_back(i);
    }
    for (int r : root)
        dfs(r);
    for (int i = 1; i <= n; i++)
        cout << ans[i] << ' ';
    cout << endl;

    return 0;
}