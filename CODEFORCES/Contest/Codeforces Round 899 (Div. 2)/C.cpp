#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxn = 2e5 + 50;
ll a[maxn], rep[maxn];

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        for (int i = 0; i <= n + 2; i++)
        {
            rep[i] = 0;
        }
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        for (int i = n - 1; i >= 0; i--)
        {
            rep[i] = rep[i + 1] + (a[i] >= 0 ? a[i] : 0);
        }
        ll ans = 0;
        for (int i = 0; i < n; i++)
        {
            ans = max(ans, rep[i + 1] + (i % 2 == 0 ? a[i] : 0));
        }
        cout << ans << endl;
    }
}