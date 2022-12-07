#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
long long gcd(long long x, long long y)
{
    if (y == 0)
        return x;
    return gcd(y, (long long)x % y);
}
long long lcm(long long x, long long y) { return (long long)x * y / gcd(x, y); }
long long power(long long x, long long n)
{
    long long res = 1;
    do
    {
        if (n & 1)
            res = (long long)(res * x);
        x = (long long)x * x;
        n /= 2;
    } while (n);
    return res;
}
long long power(long long x, long long n, long long mod)
{
    long long res = 1;
    x = (long long)x % mod;
    do
    {
        if (n & 1)
            res = (long long)(res * x) % mod;
        x = (long long)(x * x) % mod;
        n /= 2;
    } while (n);
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n;
    cin >> n;
    map<long long, long long> m;
    long long res = 0;
    for (int i = 1; i <= n; i++)
    {
        long long x;
        cin >> x;
        if (m[x + 1])
            m[x + 1]--;
        else
            res++;
        m[x]++;
    }
    cout << res << "\n";
    // for (auto x:m) if (x.se>1) res+=x.se-1;
    // cout<<res;
}