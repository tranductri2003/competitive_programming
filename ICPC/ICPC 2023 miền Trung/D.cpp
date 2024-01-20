#include <bits/stdc++.h>
using namespace std;
int n, m, k;
bool check(vector<vector<char>> &a, vector<vector<int>> &f, int mid)
{
    int dem = 0;
    for (int i = 1; i <= n; i++)
    {
        int l_b = -1, r_b = -1;
        for (int j = 1; j <= m; j++)
            if (a[i][j] == 'x')
            {
                if (r_b < j)
                {
                    dem++;
                    l_b = j;
                    r_b = min(j + mid * 2, f[i][j]);
                    // cout << l_b << " " << r_b << endl;
                }
            }
    }
    // cout << "\n";
    return dem <= k;
}
int main()
{
    cin >> n >> m >> k;
    vector<vector<char>> a(n + 2, vector<char>(m + 2));
    vector<vector<int>> f(n + 2, vector<int>(m + 2));
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> a[i][j];
            f[i][j] = 0;
        }
        f[i][m + 1] = 1e9;
        for (int j = m; j >= 1; j--)
            if (a[i][j] == '#')
                f[i][j] = j;
            else
                f[i][j] = f[i][j + 1];
    }
    int l = 0, r = m;
    while (l < r)
    {
        int mid = (l + r) / 2;
        if (check(a, f, mid))
            r = mid - 1;
        else
            l = mid + 1;
    }
    int mid = min(max((l + r) / 2, 0), m);
    if (mid != 0)
        while (check(a, f, mid - 1))
        {
            mid--;
            if (mid == 0)
                break;
        }
    while (check(a, f, mid) == false)
    {
        mid++;
        if (mid > m)
            break;
    }

    if (mid > m)
        cout << -1;
    else
        cout << mid;
}