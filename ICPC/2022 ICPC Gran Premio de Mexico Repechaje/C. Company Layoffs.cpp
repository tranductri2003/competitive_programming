#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
long long a[N];
long long s[N];
int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    sort(a + 1, a + n + 1);
    for (int i = 1; i <= n; i++)
    {
        s[i] = s[i - 1] + a[i];
    }
    for (int i = 1; i <= m; i++)
    {
        long long q;
        cin >> q;
        long long k = upper_bound(a + 1, a + n + 1, q) - a;
        cout << (s[n]) - (s[n] - s[k - 1]) + (n - k + 1) * q << endl;
    }
}