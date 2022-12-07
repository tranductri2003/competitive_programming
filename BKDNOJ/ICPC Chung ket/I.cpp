#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long n, p;
    cin >> n >> p;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    a.push_back(0);
    vector<long long> bf(1, 0);
    for (int i = 0; i <= n; i++)
    {
        for (int j = i; j <= n; j++)
        {
            bf.push_back(a[i] + a[j]);
        }
    }
    sort(bf.begin(), bf.end());
    long long ans = 0;
    for (int i = 0; i <= n; i++)
    {
        if (a[i] > p)
            continue;
        for (int j = i; j <= n; j++)
        {
            if (a[i] + a[j] > p)
                continue;
            long long tans = a[i] + a[j];
            int k = upper_bound(bf.begin(), bf.end(), p - tans) - bf.begin();
            tans += bf[k - 1];
            ans = max(ans, tans);
        }
    }
    cout << ans << endl;

    return 0;
}