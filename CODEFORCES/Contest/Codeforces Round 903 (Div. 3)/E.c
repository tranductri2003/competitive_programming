#include <bits/stdc++.h>
using namespace std;
#define int long long
const int INF = 1e18;
void solve()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &x : a)
        cin >> x;
    vector<int> dp(n, -1);
    auto f = [&](auto &self, int p) -> int
    {
        if (p == n)
            return 0;
        int &r = dp[p];
        if (r != -1)
            return r;
        r = INF;
        r = min(r, 1 + self(self, p + 1));
        if (p + a[p] < n)
            r = min(r, self(self, p + a[p] + 1));
        return r;
    };
    cout << f(f, 0) << endl;
}

signed main()
{
    int t;
    cin >> t;
    while (t--)
        solve();
}