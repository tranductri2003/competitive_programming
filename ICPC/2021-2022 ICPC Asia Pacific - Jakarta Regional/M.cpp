#include <bits/stdc++.h>
using namespace std;
#define int long long
int best(int n, vector<int> a)
{
    vector<int> _min(n);
    vector<int> sum(n);
    for (int i = 0; i < n; ++i)
    {
        if (i == 0)
            _min[i] = a[i];
        else
            _min[i] = min(a[i], _min[i - 1] + a[i]);
        if (i == 0)
            sum[i] = a[i];
        else
            sum[i] = sum[i - 1] + a[i];
    }
    vector<int> max_sum(n);
    for (int r = n - 1; r >= 0; --r)
    {
        if (r == n - 1)
            max_sum[r] = sum[r];
        else
            max_sum[r] = max(max_sum[r + 1], sum[r]);
    }
    int res = 0;
    for (int i = 1; i < n; ++i)
    {
        res = max(res, max_sum[i] - sum[i - 1] - _min[i - 1]);
    }
    return res;
}
void solve()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &x : a)
        cin >> x;
    int res1 = best(n, a);
    reverse(a.begin(), a.end());
    int res2 = best(n, a);
    cout << max(res1, res2);
}
int32_t main()
{
    int test = 1;
    while (test--)
        solve();
    return 0;
}
