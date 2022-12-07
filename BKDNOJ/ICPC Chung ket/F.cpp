#include <bits/stdc++.h>
using namespace std;

int main()
{

    int n, p, k;
    cin >> n >> p;
    vector<vector<pair<int, int>>> c(n);
    for (int i = 0; i < n; i++)
    {
        cin >> k;
        c[i].resize(k);
        for (int j = 0; j < k; j++)
            cin >> c[i][j].first >> c[i][j].second;
    }
    vector<vector<vector<int>>> f(n);
    f[0] = vector<vector<int>>(c[0].size(), vector<int>(p + 1, 0));
    for (int i = 1; i < n; i++)
    {
        f[i] = vector<vector<int>>(c[i].size(), vector<int>(p + 1, 1e9));
        for (int j = 0; j < c[i].size(); j++)
        {
            for (int k = 0; k <= p; k++)
            {
                for (int l = max(i - 2, 0); l < i; l++)
                {
                    // cout << "try jump from " << l << " to " << i << " already jumped " << k << endl;
                    if (k > 0)
                        continue;

                    for (int m = 0; m < c[l].size(); m++)
                    {
                        f[i][j][k] = min(f[l][m][k - (i - l - 1)] + (c[i][j].second + c[l][m].second) * abs(c[i][j].first - c[l][m].first), f[i][j][k]);
                    }
                }
            }
        }
    }
    int ans = 2e9;
    for (int i = 0; i < c[n - 1].size(); i++)
    {
        ans = min(ans, f[n - 1][i][k]);
        // cout << f[n - 1][i][k] << ' ';
    }
    for (int i = 0; i < c[max(n - 2, 0)].size(); i++)
    {
        ans = min(ans, f[max(n - 2, 0)][i][k]);
        // cout << f[n - 1][i][k] << ' ';
    }
    // cout << endl;
    cout << ans << endl;

    return 0;
}