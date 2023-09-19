#include <bits/stdc++.h>
using namespace std;

#define int long long
const int N = 2e6 + 5;

void solve()
{
    int n;
    cin >> n;

    vector<int> a(n + 1), d(n + 1), F(n + 1), G(n + 1);

    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 1; i <= n; i++)
        cin >> d[i];

    for (int i = 1; i <= n; i++)
    {
        int l = max(1ll, i - d[i]);
        int r = min(n, i + d[i]);
        F[l] += a[i];
        G[r] += a[i];
    }

    for (int i = 1; i <= n; i++)
        G[i] = G[i - 1] + G[i];

    auto check = [&](int x)
    {
        int homeless = 0; // :))))
        int cnt = 0;
        for (int i = 1; i <= n; i++)
        {
            homeless += F[i];
            int now = min(homeless, x);
            homeless -= now;
            cnt += now;
            if (cnt < G[i])
                return false;
        }

        if (homeless)
            return false;
        return true;
    };

    int l = 0, r = 1e9;
    while (l < r)
    {
        int m = (l + r) / 2;
        if (check(m))
            r = m;
        else
            l = m + 1;
    }
    cout << l;
    //    for (int i = 1; i <= 10; i++)
    //        cout << check(i) << "\n";
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
