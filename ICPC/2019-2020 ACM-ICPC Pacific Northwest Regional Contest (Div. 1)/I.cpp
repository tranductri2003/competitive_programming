#include <bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ordered_set tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

vector<vector<int>> c;
vector<int> vis;
vector<vector<int>> f;
int tans;

void dfs(int u)
{

    vis[u] = f[u][1] = 1;
    for (int v : c[u])
    {
        if (vis[v])
            continue;
        dfs(v);
        f[u][1] += f[v][0];
        f[u][0] += max(f[v][1], f[v][0]);
    }
    tans = max(tans, max(f[u][0], f[u][1]));
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    c.resize(n);
    vis.assign(n, 0);
    f.assign(n, vector<int>(2, 0));
    vector<string> all_string;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        all_string.push_back(s);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            vector<int> diff_pos;
            for (int k = 0; k < all_string[i].length(); k++)
                if (all_string[i][k] != all_string[j][k])
                    diff_pos.push_back(k);
            if (diff_pos.size() == 2 && all_string[i][diff_pos[0]] == all_string[j][diff_pos[1]] && all_string[i][diff_pos[1]] == all_string[j][diff_pos[0]])
            {
                c[i].push_back(j);
                c[j].push_back(i);
                // cout << i + 1 << ' ' << j + 1 << endl;
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        if (!vis[i])
        {
            tans = 0;
            dfs(i);
            ans += tans;
        }
    }

    cout << ans << endl;

    return 0;
}
