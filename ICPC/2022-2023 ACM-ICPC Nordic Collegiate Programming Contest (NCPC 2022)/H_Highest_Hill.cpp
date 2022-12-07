#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    long long n;
    cin >> n;
    long long a[n + 3];
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    long long min_l[n + 3], min_r[n + 3];

    min_l[1] = a[1];
    for (int i = 2; i <= n; i++)
        if (a[i - 1] <= a[i])
            min_l[i] = min_l[i - 1];
        else
            min_l[i] = a[i];

    min_r[n] = a[n];
    for (int i = n - 1; i >= 1; i--)
        if (a[i] >= a[i + 1])
            min_r[i] = min_r[i + 1];
        else
            min_r[i] = a[i];
    long long res = -1e18;

    for (int i = 2; i < n; i++)
        if (a[i - 1] <= a[i] && a[i] >= a[i + 1])
        {
            res = max(res, min(a[i] - min_l[i - 1], a[i] - min_r[i + 1]));
        }
    cout << res;
}

 