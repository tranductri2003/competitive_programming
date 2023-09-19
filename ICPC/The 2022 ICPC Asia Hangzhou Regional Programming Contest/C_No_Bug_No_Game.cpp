#include <bits/stdc++.h>
using namespace std;

int dp[3005][3005][2];
int w[3005][3005];
int p[3005];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;

    for (int i = 1; i <= n; ++i)
    {
        cin >> p[i];
        for (int j = 1; j <= p[i]; ++j)
        {
            cin >> w[i][j];
        }
    }

    for (int i = 0; i <= n; ++i)
    {
        for (int j = 1; j <= k; ++j)
        {
            dp[i][j][0] = dp[i][j][1] = -1e9;
        }
    }

    dp[0][0][0] = 0;

    for (int i = 1; i <= n; ++i)
    {
        for (int j = 0; j <= k; ++j)
        {
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0]);
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][1]);

            if (j >= p[i])
            {
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - p[i]][0] + w[i][p[i]]);
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - p[i]][1] + w[i][p[i]]);
            }

            for (int h = 1; h <= p[i]; ++h)
            {
                if (j >= h)
                {
                    dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - h][0] + w[i][h]);
                }
            }
        }
    }

    int res = 0;
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 0; j <= k; ++j)
        {
            res = max(res, dp[i][j][0]);
            if (j == k)
            {
                res = max(res, dp[i][j][1]);
            }
        }
    }

    cout << res << '\n';

    return 0;
}
