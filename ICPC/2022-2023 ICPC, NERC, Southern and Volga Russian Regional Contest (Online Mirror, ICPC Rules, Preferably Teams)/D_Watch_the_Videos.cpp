#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    long long n, m;
    cin >> n >> m;
    long long a[n + 3], b[n + 3];
    for (int i = 1; i <= n; i++)
        cin >> b[i];
    sort(b + 1, b + n + 1);
    long long l = 1, r = n;
    for (int i = 1; i <= n;)
    {
        if (b[l] + b[r] > m)
        {
            a[i] = b[r];
            r--;
            i++;
        }
        else
        {
            a[i] = b[r];
            a[i + 1] = b[l];
            i += 2;
            l++;
            r--;
        }
    }
    // for (int i=1; i<=n; i++) cout<<a[i]<<" "; cout<<"\n";
    long long time_ = a[1], dungluong = a[1];
    for (int i = 2; i <= n; i++)
    {
        if (dungluong + a[i] <= m)
        {
            time_ = time_ + a[i];
            dungluong = dungluong - a[i - 1] + a[i];
        }
        else
        {
            time_ = time_ + 1 + a[i];
            dungluong = a[i];
        }
    }
    cout << time_ + 1;
}