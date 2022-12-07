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

long long a[20];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    for (int i = 1; i <= 20; i++)
        a[i] = 4;
    long long n;
    cin >> n;
    int x, y;

    cin >> x >> y;
    a[x]--;
    a[y]--;
    long long s1 = min(x, 10) + min(y, 10);

    cin >> x >> y;
    a[x]--;
    a[y]--;
    long long s2 = min(x, 10) + min(y, 10);

    for (int i = 1; i <= n; i++)
    {
        cin >> x;
        s1 += min(x, 10);
        s2 += min(x, 10);
        a[x]--;
    }

    long long res = -1;
    for (int i = 1; i <= 13; i++)
        if (a[i])
        {
            x = s1 + min(i, 10);
            y = s2 + min(i, 10);
            if (y > 23)
                break;
            if (y == 23)
            {
                res = i;
                break;
            }
            if (x > 23 && y < 23)
            {
                res = i;
                break;
            }
        }
    cout << res;
}