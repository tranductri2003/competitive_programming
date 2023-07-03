#include <bits/stdc++.h>
using namespace std;
long long MillerRabin[10000005];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    MillerRabin[1] = 1;
    for (int i = 2; i * i <= 1000000; i++)
        if (MillerRabin[i] == 0)
            for (int j = i * i; j <= 1000000; j += i)
                MillerRabin[j] = 1;
    long long n, x;
    cin >> n >> x;
    long long a[n + 3];
    vector<long long> v;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        if (a[i] > 0 && a[i] <= x)
        {
            if (MillerRabin[a[i]] == 0)
                v.push_back(i);
        }
    }
    // v.push_back(n+3);
    long long minn = 1e18;
    for (int i = 1; i <= n - v.size() + 1; i++)
    {
        auto it1 = lower_bound(v.begin(), v.end(), i) - v.begin();
        auto it2 = upper_bound(v.begin(), v.end(), i + v.size() - 1) - v.begin();
        if (it2 == v.size())
            it2--;
        if (i + v.size() - 1 < v[it2])
            it2--;
        // cout<<it1<<" "<<it2<<" "<<it2-it1+1<<"\n";
        if (it1 <= it2)
            minn = min(minn, (long long)v.size() - (it2 - it1 + 1));
    }
    // for (auto x:v) cout<<x<<" ";
    cout << minn;
}
