#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> c;
vector<long long> cnt, dd;

void dfs(int u, int col)
{
    dd[u] = col;
    cnt[col]++;
    for (int v : c[u])
    {
        if (dd[v] == -1)
            dfs(v, col);
    }
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, k, u, v;
    cin >> n >> k;
    c.resize(n + 1);
    for (int i = 0; i < n; i++)
    {
        cin >> u >> v;
        c[u].push_back(v);
        c[v].push_back(u);
    }
    dd.assign(n + 1, -1);
    int cur = 0;
    for (int i = 1; i <= n; i++)
    {
        if (dd[i] == -1)
        {
            cnt.push_back(0);
            dfs(i, cur);
            cur++;
        }
    }
    vector<vector<long long>> f(cnt.size(), vector<long long>(k + 1, 0));
    for (int i = 0; i < cnt.size(); i++)
        f[i][0] = 1;
    for (int i = 1; i <= k; i++)
    {
        long long tmp = 1;
        for (int j = 0; j < i; j++)
            tmp *= cnt[j];
        f[i - 1][i] = tmp;
    }
    for (int i = 1; i <= k; i++)
    {
        for (int j = i; j < cnt.size(); j++)
        {
            f[j][i] = f[j - 1][i];
            f[j][i] += (f[j - 1][i - 1] * cnt[j]);
        }
    }
    // for (int i = 0; i <= k; i++) {
    //     for (int j = 0; j < cnt.size(); j++)
    //         cout << f[j][i] << ' ';
    //     cout << endl;
    // }
    cout << f[cnt.size() - 1][k] << endl;

    return 0;
}
