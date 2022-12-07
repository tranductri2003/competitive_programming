#include <bits/stdc++.h>
using namespace std;

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

bool check(vector<vector<int>> c, vector<int> cnt, int rm, int k, int n)
{
    bool iok = true;
    while (rm > 0)
    {
        bool canContinue = false;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if ((c[i][j] == 0) && (cnt[i] + cnt[j] >= k))
                {
                    // cout << k << '|' << i << '|' << j << endl;
                    c[i][j] = 1;
                    cnt[i]++, cnt[j]++;
                    if (cnt[i] == n - 1)
                        rm--;
                    if (cnt[j] == n - 1)
                        rm--;
                    canContinue = true;
                }
            }
        }
        if (!canContinue)
        {
            iok = false;
            break;
        }
    }
    return iok;
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m, u, v;
    cin >> n >> m;
    vector<vector<int>> c(n, vector<int>(n, 0));
    vector<int> cnt(n, 0);
    int rm = n;
    while (m--)
    {
        cin >> u >> v;
        if (u > v)
            swap(u, v);
        u--, v--;
        c[u][v] = 1;
        cnt[u]++, cnt[v]++;
        if (cnt[u] == n - 1)
            rm--;
        if (cnt[v] == n - 1)
            rm--;
    }
    int l = 0, r = 2 * n;
    while (l < r)
    {
        cout << l << " " << r << endl;
        if (l + 1 == r)
        {
            if (check(c, cnt, rm, r, n))
                l = r;
            break;
        }
        m = (l + r) / 2;
        if (check(c, cnt, rm, m, n))
            l = m;
        else
            r = m - 1;
    }
    cout << l;

    return 0;
}