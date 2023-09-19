#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1e9 + 7;
const int N = 305;
long long dp[N * N][N];
int n, k, p, a[N];
int main()
{
    cin >> n >> k >> p;
    dp[0][0] = 1;
    for (int i = 1; i <= k; i++)
    {
        a[i] = i;
    }
    for (int i = 1; i <= 90000; i++)
    {
        for (int j = 1; j <= k; j++)
        {
            for (int l = 1; l <= n; l++)
            {
                if (i - a[j] >= 0)
                    dp[i][l] = (dp[i][l] + dp[i - a[j]][l - 1]) % MOD;
            }
        }
    }
    long long res = 0;
    for (int x = p + 1; x <= 90000; x++)
    {
        res = (res + dp[x][n]) % MOD;
    }
    cout << res;
}