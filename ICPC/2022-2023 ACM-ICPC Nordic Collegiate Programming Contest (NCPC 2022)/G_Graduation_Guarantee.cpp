#include <bits/stdc++.h>

using namespace std;

int main()
{

    int n, k;
    double ans = 0;
    cin >> n >> k;
    vector<double> p(n + 1);
    for (int i = 1; i <= n; i++)
        cin >> p[i];
    sort(p.begin() + 1, p.end(), greater<double>());
    vector<vector<double>> f(n + 1, vector<double>(2 * n + 1, 0));
    f[0][n] = 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= 2 * n; j++)
        {
            double tmp = 0;
            if (j > 0)
                tmp += (f[i - 1][j - 1] * p[i]);
            if (j < 2 * n)
                tmp += (f[i - 1][j + 1] * (1.0 - p[i]));
            f[i][j] = tmp;
        }
        double tans = 0;
        for (int j = n + k; j <= 2 * n; j++)
            tans += f[i][j];
        ans = max(ans, tans);
        // cout << i << ' ' << tans << endl;
    }
    cout << setprecision(8) << fixed;
    cout << ans << endl;
    /*
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= 2 * n; j++)
            cout << f[i][j] << ' ';
        cout << endl;
    }
    */

    return 0;
}
