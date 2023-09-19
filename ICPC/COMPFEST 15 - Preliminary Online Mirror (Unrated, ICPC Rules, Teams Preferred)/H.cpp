#include <bits/stdc++.h>
using namespace std;

#define int long long
const int N = 2e6 + 5;
const int MOD = 998244353;

int fact[N], ifact[N];

int fpow(int a, int n)
{
    int ans = 1;
    while (n)
    {
        if (n & 1)
            ans = ans * a % MOD;
        a = a * a % MOD;
        n = n / 2;
    }
    return ans;
}

int nCr(int n, int r)
{
    if (r > n)
        return 0;
    return fact[n] * ifact[n - r] % MOD * ifact[r] % MOD;
}

void solve()
{
    int n, k;
    cin >> n >> k;

    fact[0] = 1;
    for (int i = 1; i < N; i++)
        fact[i] = fact[i - 1] * i % MOD;
    for (int i = 0; i < N; i++)
        ifact[i] = fpow(fact[i], MOD - 2);

    int ans = 1;
    for (int i = 1; i <= n; i++)
    {
        int w = k - n + i;
        if (w >= 1)
        {
            int j = n - i + 1;
            int val = fpow(j + 1, w) - fpow(j, w);
            val = (val + MOD) % MOD;
            ans += val * fact[j] % MOD * fact[n] % MOD * ifact[i - 1] % MOD;
            ans %= MOD;
        }
    }
    cout << ans << '\n';
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif // ONLINE_JUDGE

    solve();
    return 0;
}
