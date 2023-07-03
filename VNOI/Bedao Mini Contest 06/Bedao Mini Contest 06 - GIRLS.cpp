#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    long long m, n, k;
    cin >> m >> n >> k;
    long long a[m + 3];
    for (int i = 1; i <= m; i++)
        cin >> a[i];
    sort(a + 1, a + m + 1);
    for (int i = m; i >= n; i--)
        if (a[i] - a[i - n + 1] <= k)
        {
            long long res = 0;
            for (int j = i - n + 1; j <= i; j++)
                res += a[j];
            cout << res;
            return 0;
        }
    cout << -2;
}
